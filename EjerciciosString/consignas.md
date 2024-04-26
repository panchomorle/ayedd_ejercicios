1. Crear una variable String que contiene el nombre de 4 animales.
2. Mostrar en patalla el nombre de todos os animales utilizando Slice de String
3. Transformar la String anterior en una lista de Strings y mostrar por pantalla utilizando la función
Split
4. Ordenar la lista anterior e mostrar por pantalla
5. La operación habitual de Python para agregar elementos a una lista se agrega al final, pero
en algunas situaciones necesitamos agregar al principio de la lista. Simule esta operación de
4 maneras diferentes:
usando insert()
usando [] and +
usando Slicing
usando extend()
6. Carrera de caballos: la pista tiene 1000 metros y corren 4 caballos. Cada metro es una
iteración. En cada iteración y por cada caballo el mismo puede avanzar de 1 a 5 metros
(import random y use la función randint). Agregar al final de la iteración una demora del
programa de 1 segundo (import time y use la función sleep()) que permita ir viendo por
pantalla en que metro está cada caballo dentro de la pista. Cuando el último caballo llegue
a los 1000 metros, mostrar cómo quedó conformado el podio.
Utilice MAPAS (diccionarios) en tu solución donde la clave deberá ser los nombres de los
caballos, analizando la solución anterior y actual cuál te pareció más sencillo?
7. Imagine un Buffer de impresión con una capacidad máxima para almacenar 20 documentos,
simule la gestión de la impresora en caso de falla a través de una fila circular del tipo FIFO
(First In First Out), asuma que los documentos que superan la capacidad máxima se pierden.
La selección del usuario será A, I o S, A para agregar documento, I imprimir y S salir del
programa. En el caso de la operación A Agregar, el usuario debe informar el nombre del
documento que ingresará a la fila.