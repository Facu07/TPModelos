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
        return self.sucursales


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
                    temp[int(line[0])] = int(line[1])
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


def busco_punto_medio(demandas, coordenadas, camion):
    maximo = (0.0,0.0)
    minimo = (1000000.0,1000000.0)
    medio = (0,0)
    for value in coordenadas.values():
        if math.sqrt(math.pow(value[0],2)+math.pow(value[1],2)) < math.sqrt(math.pow(minimo[0],2)+math.pow(minimo[1],2)):
            minimo = value
        elif math.sqrt(math.pow(value[0],2)+math.pow(value[1],2)) > math.sqrt(math.pow(maximo[0],2)+math.pow(maximo[1],2)):
            maximo = value
    medio = (math.sqrt(math.pow(maximo[0]-minimo[0],2)),math.sqrt(math.pow(maximo[1]-minimo[1],2)))
    print(medio)
    for value in coordenadas.values():
        if value[0] > medio[0] - 10 and value[0] < medio[0] + 10 and value[1] > medio[1] - 10 and value[0] < medio[0] + 10:
            medio = value
    print(medio)
    return maximo, minimo, medio


def busca_recursiva(demandas, coordenadas, camion):
    demanda = 0
    sucursal = 1
    primero = 1000000000
    for key,value in coordenadas.items():
        segundo = ((camion.get_ubicacion()[0]-value[0])**2+(camion.get_ubicacion()[1]-value[1])**2)**(1/2)
        if (primero > segundo): #and (demandas[key] + camion.get_dinero_disponible() >= 0) and (demandas[key] + camion.get_dinero_disponible() <= camion.get_capacidad()):
            primero = segundo
            sucursal = key
    camion.set_ubicacion(coordenadas[sucursal])
    #camion.set_dinero_disponible(demandas[sucursal])
    camion.set_sucursales(sucursal)
    del demandas[sucursal]
    del coordenadas[sucursal]


archivo = 'problema_tres.txt'
registro, demandas, coordenadas, eliminar = leer_archivo(archivo)
camion = Camion(registro['CAPACIDAD'])
maximo, minimo, medio = busco_punto_medio(demandas, coordenadas, camion)
camion.set_ubicacion(minimo)
while len(demandas) > 0:
    busca_recursiva(demandas, coordenadas, camion)
f = open("resultados.txt", "w+")
for e in camion.get_sucursales():
    f.write("%d, " % (e))

