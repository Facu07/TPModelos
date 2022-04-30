# TPModelos
Repositorio para el TP de Modelos Y Optimización I

## Enunciado
  - Un camión de caudales debe entregar y recibir dinero de diferentes sucursales bancarias.
  - Sale de la central vacío y en ningún momento la carga puede superar un importe definido (tampoco ser negativa).
  - Se busca encontrar el recorrido más corto pasando por todas las sucursales.
  
## Ideas
Primero parsearé el archivo
Luego voy a ir encontrando los más cercanos sin tener en cuenta si pueden descargar o cargar plata y organizarme con la recursion del problema
Por último, agregaré la confición de la capacidad del camión (positiva y negativa)

## Mejoras
Me di cuenta que hay varias sucursales que tienen 0 en demanda, osea que no cargan ni descargan plata, por lo que sería mejor ni tenerlas en cuenta para que no gaste poder de procesamiento
