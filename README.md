# Diario

## Programa que sirve para registrar el día a día

### Esqueleto del programa:
![esqueleto_programa](https://raw.githubusercontent.com/brianreinke95/Diario/master/Diario_Diagrama.png)

Como se puede observar en el esqueleto del programa la lógica consta de 3 ramas de funcionalidades. 
1. Cargar Datos - Load
2. Ver Datos - Calendar
3. Graficar Datos - Statistics

## Cargar Datos:
Se trabaja por consola. Consta de una interfaz que por medio de inputs se accede distintas secciones de carga, corrección y visualización.
Los pasos a seguir son: 
  1. Cargar el día a cargar. Ej: 01/12/2019
  2. Cargar los límites horarios que componen a ese día. (Empieza cuando se despierta, termina cuando se va a dormir)
  3. Cargar uno a uno los eventos. [Descripcion, Aclaracion, Horario de fin de la actividad]
  4. Una vez cargados al dataframe se puede editar lo previamente cargado ingresando fila y columna a editar.
  5. Cuando se esté seguro de que los datos a cargar son correctos se carga a un csv con la opción correspondiente.
  6. En la carga se debe especificar si el día fue destacado o no (Si significó algo para usted). De serlo se cargará una aclaración y un TAG que identifique el tipo de día destacado.

De no seguir el orden pre-establecido saltarán distintos avisos de ERROR.

## Ver Datos:
Toda esta sección consiste en visualizar distintos DataFrames por consola. 
Funcionalidades:
  1. Listar días cargados con sus respectivos TAGS. 
  2. Visualizar todos los días del mes especificado uno a uno.
  3. Visualizar día seleccionado.
  
A futuro se implementará el uso de widgets para que se vea más como un calendario.

## Graficar Datos:
En esta sección se realizan distintos tipos de gráficas para analizar la data. 

Lo primero que se realiza (internamente) es la preparación del dataframe para su posterior uso. Todas las actividades que tenían un tiempo
de inicio y final se les calcula el consumo de minutos en float mediante operaciones con timestamp.

Luego entramos a la selección del tamaño de la muestra. 
Las opciones son:
  1: Todo
  2: Por Mes
  3: Entre fechas
Definiendo entonces el DataFrame a graficar se realizan 3 tipos de gráficos (hasta ahora):
  ### Pie Charts: Actividades por días en la semana:
  ![Pie_Chart](Pie_Chart.png?raw=true "Pie Chart")
  
  ### Bar Chart: Consumo total de las actividades más destacadas.
  ![Alt text](relative/path/to/img.jpg?raw=true "Title")

  ### Bar Chart: Evolución de la actividad que querramos visualizar día a día.
  ![Alt text](relative/path/to/img.jpg?raw=true "Title")

