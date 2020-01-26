from menues import menu_statistics, menu_datos, menu_calendar, menu_tools
from clear import clear
from Objetos import Registro, Calendario, Estadisticas
from Comprobacion_Seleccion import Comprobacion_formato, Comprobacion_seleccion

from Switches import switch_calendar, switch_load, switch_statistics, switch_tools
from Funciones_Carga import Cargar_a_Archivo

from Objetos import Diario, Destacado


############################################################3
### Funciones de menu

# Cada una de las funciones se encarga de acceder a las funciones de cada rama del programa
## Rama 1: Carga de datos. ---- load_data
## Rama 2: Calendario en texto plano. ---- calendar
## Rama 3: Gráficos y estadísticas. ---- statistics

def load_data():

    load_object = Registro()

    while(True):

        seleccion = menu_datos()
        clear()
        if Comprobacion_seleccion([0, 1, 2, 3, 4, 5, 9], seleccion):

            if seleccion == 0:
                if load_object.dia != None and load_object.limites != None and not load_object.eventos_df.empty:
                    respuesta = input('¿Está seguro de cancelar la carga? Sus datos se perderan.  si/no:   ')
                    if Comprobacion_seleccion(['si', 'no'], respuesta):
                        if respuesta == 'si':
                            break
                else:
                    break

            elif seleccion == 9:
                # Validar que todos los espacios estén llenos.
                # Cargar a texto plano.
                if load_object.dia != None and load_object.limites != None and not load_object.eventos_df.empty:
                    print('\n Estaría cargando \n')
                    Cargar_a_Archivo(load_object, csv_name=Diario)  # Realizar el cargado al archivo de texto.

                    y = True
                    while y:
                        option = input('\n¿Fue este día destacado? [si, no]... ')
                        if Comprobacion_seleccion(['si', 'no'], seleccion=option):
                            if option == 'si':

                                ''' Si es un día destacado se debe incluír una descripción de por qué lo es y un 
                                    símbolo que represente el tipo de destacado.
                                Ejemplo: S: Star, día importante para mi vida; P: Parcial; A: Tiempo con Amigos
                                         F: Eventos Familiares'''

                                aclaracion = input('Asunto:   ')
                                # Comprobar Selección de Tag, meterlo en un loop.
                                x = True
                                while x:
                                    tag = input('\nTAG [S, A, P, F, A + S, ...]:   ')

                                    # Funciones auxiliares para cuando hay más de 1 simbolo:
                                    multiple_tags = tag.split('+')
                                    multiple_tags = [tag.strip() for tag in multiple_tags]  # Le saco los espacios
                                    multiple_tags = [Comprobacion_seleccion(['S', 'A', 'P', 'F'], tag)
                                                     for tag in multiple_tags]

                                    if all(multiple_tags):        # Si todos los elementos son válidos.

                                        # Carga df de destacados para luego cargarlo al csv correspondiente
                                        load_object.add_destacado(dia=load_object.get_dia(), destacado='SI',
                                                             aclaracion=aclaracion, simbolo=tag)
                                        x = False
                                    else:
                                        print('Ha seleccionado mal sus opciones. Intente Nuevamente\n')

                            else:
                                load_object.add_destacado(dia=load_object.get_dia(), destacado='NO')

                            Cargar_a_Archivo(load_object, csv_name=Destacado)
                            y = False
                            input('Presione Enter para continuar...')
                        else:
                            print('Ha seleccionado mal sus opciones. Intente Nuevamente\n')

                    break
                else:
                    print('\nERROR. Algún campo está vacío. '
                          'Complete los espacios correspondientes e intente de nuevo.\n ')
                    input('Presione Enter para continuar...\n')
            else:
                func = switch_load(seleccion)
                func(load_object)  # Deberia pasarle el objeto como argumento. El objeto ya tendria que haber sido creado
                clear()
    clear()
    del load_object
    return


def calendar():
    calendario = Calendario()
    seleccion = menu_calendar()
    if seleccion != 0 and Comprobacion_seleccion([0, 1, 2, 3], seleccion):
        func = switch_calendar(seleccion)
        clear()
        func(calendario)
        input('Presione Enter para continuar...')
    clear()
    del calendario
    return


def statistics():
    data = Estadisticas()
    data.set_Etiquetas()      # Seteo un data_frame agrupado por etiquetas y con diferencias horarias en float.

    seleccion = menu_statistics()
    if seleccion != 0 and Comprobacion_seleccion([0, 1, 2, 3], seleccion):
        func = switch_statistics(seleccion)
        func(data)        # Todas las funciones que haga usarán el dataframe creado internamente como "etiquetas_df".
        input('Presione Enter para continuar al menu principal...')
    del data
    clear()


def tools():
    seleccion = menu_tools()
    if seleccion != 0 and Comprobacion_seleccion([0, 1], seleccion):
        func = switch_tools(seleccion)
        func()        # Todas las funciones que haga usarán el dataframe creado internamente como "etiquetas_df".
        input('Presione Enter para continuar al menu principal...')
    clear()
    pass



# Ideas para statistics:
#  Total de horas registradas       ✔
#  Horas en porcentaje y promedio por dia
#  Calculo aproximado de promedio de horas de sueño
# Gráficos que muestren la evolución según etiqueta     ✔
#  Plot que grafique horas por día según registro       ✔
#  Limitar la muestra entre fechas y para x mes en particular.      ✔
#  Capacidad de agrupar por mes y hacer los mismos análisis mes contra mes
#  Definir parámetros a los que se le pueda hacer una evaluación de incidencia. Como por ejemplo el roi que
#   mide retorno sobre la inversión. Querría ver por ejemplo cómo un parcial en cierta fecha modifica mis
#   patrones de comportamiento. Cuánto un parcial incide sobre mis horas de estudio por ejemplo.
#  Medir evolución dia tras dia o mes tras mes. Ejemplo: Lunes incrementé en un 3% las horas de estudio respecto
#   al lunes pasado. O En Noviembre mes de parciales decrementé 20% mis horas viendo series respecto a Septiembre.

# Utilizar el calendario para crear una columna con los días de la semana [Lunes, Martes, ...]. Agrupar por día.
# Promediar actividades por etiquetas, utilizar los 4 o 5 más significativos y al resto ponerlo otros.
# graficar por día la suma de actividades promedios en un stacked plot

# Estudios de pronóstico.
#  Utilizando cadenas de markov
#  Utilizando regresiones de ML

