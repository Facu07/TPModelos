import sys
import math

class Camion:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.dinero_disponible = 0
        self.ubicacion = (0,0)
        self.sucursales = []

    def __iter__(self):
        return self.capacidad.__iter__()

    def __getitem__(self, index):
        try:
            return self.capacidad
        except Exception as e:
            print('nop, te pasaste')
            print(e)

    def __repr__(self):
        return f'Camion({self.capacidad.__repr__()}, {self.dinero_disponible.__repr__()}, {self.ubicacion.__repr__()} , {self.sucursal.__repr__()})'

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_ubicacion(self):
        return self.ubicacion

    def get_dinero_disponible(self):
        return self.dinero_disponible

    def set_dinero_disponible(self, dinero):
        self.dinero_disponible += dinero

    def get_capacidad(self):
        return self.capacidad

    def set_sucursales(self,sucu):
        self.sucursales.append(sucu)

    def get_sucursales(self):
        for e in self.sucursales:
            print(e, end=' ')



def leer(file, encabezado, separador=' ', isTuple=False):
    eliminar = []
    temp = {}
    line = file.readline()
    while line.find(encabezado):
        try:
            line = line.split(separador)            
            line = [i.strip() for i in line]
            if isTuple:
                temp[int(line[0])] = (float(line[1]),float(line[2]))
            else:
                try:
                    if int(line[1]) != 0:
                        temp[int(line[0])] = int(line[1])
                    else:
                        eliminar.append(int(line[0]))
                except:
                    temp[line[0]] = int(line[1])
        except:
            continue
            line = file.readline()
        line = file.readline()       
    return temp, eliminar


def leer_archivo(archivo):
    registro = {}
    demandas = {}
    coordenadas = {}
    eliminar = []
    with open(archivo, 'rt') as file:
        registro, temp = leer(file, 'DEMANDAS', ':')
        demandas, eliminar = leer(file, 'FIN DEMANDAS')
        leer(file, 'EDGE_WEIGHT_TYPE')
        leer(file, 'NODE_COORD_SECTION')
        coordenadas, temp = leer(file, 'EOF', ' ', True)
    return registro, demandas, coordenadas, eliminar


def busca_recursiva(demandas, coordenadas, camion):
    demanda = 0
    sucursal = 1
    primero = 1000000000
    for key,value in coordenadas.items():
        segundo = math.sqrt(math.pow(camion.get_ubicacion()[0]-value[0],2)+math.pow(camion.get_ubicacion()[1]-value[1],2))
        if (primero > segundo) and (demandas[key] + camion.get_dinero_disponible() >= 0) and (demandas[key] + camion.get_dinero_disponible() <= camion.get_capacidad()):
            primero = segundo
            sucursal = key
    camion.set_ubicacion(coordenadas[sucursal])
    camion.set_dinero_disponible(demandas[sucursal])
    camion.set_sucursales(sucursal)
    del demandas[sucursal]
    del coordenadas[sucursal]


def main(archivo):
    registro, demandas, coordenadas, eliminar = leer_archivo(archivo)
    camion = Camion(registro['CAPACIDAD'])
    for e in eliminar:
        del coordenadas[e]
    while len(demandas) > 0:
        busca_recursiva(demandas, coordenadas, camion)
    camion.get_sucursales()

if __name__ == "__main__":
    archivo = sys.argv[1]
    main(archivo)