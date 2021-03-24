# Genetic Algorithm :dna:
Código de Algoritmo Genético simple para la resolución de la función: f(x) = (x/coef)^2 en el dominio [0,2^30-1] donde coef=2^30-1
## Descripción
El propósito u objetivo de este mini-proyecto es más personal que general, se basa unicamente en reforzar algunos de los conocimientos adquiridos en 2018 cuando formé parte de la clase de Algoritmos Genéticos en la Universidad Tecnológica Nacional (Frro). También volver a aplicar las técnicas y nociones teóricas a los mismos ejemplos (y seguramente nuevos también) trabajados ese año, con el agregado de trabajar sobre el paradigma de programacion orientado a objetos (OOP) sobre el lenguaje Python. Este documento al igual que el contenido del repositorio irá cambiando a lo largo del tiempo a medida que agregue o cambie de direccion al emplear técnicas o prácticas distintas para la resolución de la misma u otra función. Esos cambios se irán documentando.
## Contenido
El mini-proyecto está compuesto por cuatro archivos, tres archivos con código python y un archivo de texto. Los tres archivos python actuan en conjunto para plasmar los resultados en el archivo de texto y poder ser analizados más facilmente.
### algoritmo-genetico-v1.2.py :snake:
Este archivo contiene el flujo del programa principal, que hará uso de los otros dos módulos (clss y fncs) para realizar su función.
### clss.py :snake:
Este archivo contiene la definición de las clases que representarán a la Población y a sus correspondientes cromosomas, junto con sus atributos y métodos.
### fncs.py :snake:
Este archivo contiene las funciones que me permiten escribir en el archivo de texto (.csv) los datos de cada Poblacion a lo largo de las "tiradas".
### registro.csv :page_facing_up:
Este archivo contiene los resultados obtenidos del trabajo de los anteriores módulos a lo largo de su ejecución. Estos resultados son: El valor máximo, mínimo y promedio de cada Poblacion de Cromosomas a lo largo de X cantidad de "tiradas".
## Ejecución :arrow_forward:
Para la ejecución del algoritmo basta con ejecutar el programa principal desde una terminal o el interprete preferido.
Debo aclarar que para hacer referencia a la ruta del archivo de texto dentro del modulo fncs.py hago uso del separador de directorios "/" usado en sistemas tipo Unix, por lo que si se ejecuta el algoritmo bajo entornos Windows se debe cambiar las líneas que hacen referencia a esa ruta por la correspondiente.
