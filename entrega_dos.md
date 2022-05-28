# Entrega dos

## Modelo Matemático
--------------------------------------------------------
### Variables
***Y<sub>ij</sub>*** = si va de la sucursal i a la j (∀i,j= 1,...,150) (Bivalente)

***C<sub>ij</sub>*** = Distancia entre sucursak i y j (∀i,j= 1,...,150)

***U<sub>i</sub>*** = Orden de visita de las sucursales (∀i= 1,...,150)

***CC<sub>i</sub>*** = Capacidad del Camión en la Sucursal i (∀i= 1,...,150) (Enteras)

***Demanda<sub>i</sub>*** = Demanda de la sucursal i (∀i= 1,...,150) (Enteras)

### Restricciones

#### ***Salida***
Σ<sup>150</sup><sub>i=0</sub>  Y<sub>ij</sub> = 1  Para todo i = 0, 1,..., 150            i <> j

#### ***Llegada***
Σ<sup>150</sup><sub>j=0</sub> Y<sub>ij</sub> = 1  Para todo i = 0, 1,..., 150             i <> j

#### ***Evitar subtours***
U<sub>i</sub> - U<sub>j</sub> + 150Y<sub>ij</sub> = 149                                   i <> j  ∀i,j= 1,...,150

#### ***Capacidades***
0 <= CC<sub>i</sub> <= $MAX_DINERO

CC<sub>i</sub> = Demanda<sub>j</sub> + CC<sub>i-1</sub>

#### ***Funcional***
Z(MIN) = Σ<sup>150</sup><sub>i=0</sub>Σ<sup>150</sup><sub>j=0</sub> C<sub>ij</sub> Y<sub>ij</sub>
