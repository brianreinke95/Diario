from Funciones_Carga import Cargar_dia
from Funciones_Carga import Limite_horarios
from Funciones_Carga import Carga_eventos
from Funciones_Carga import Ver_Data
from Funciones_Carga import Editar
from Funciones_Calendario import Ver_Todo
from Funciones_Calendario import Ver_por_Mes
from Funciones_Calendario import Ver_por_Dia
from Funciones_Estadisticas import Evolucion_de_Todo
from Funciones_Estadisticas import Evolucion_en_un_Mes
from Funciones_Estadisticas import Evolucion_entre_Fechas
from Funciones_Tools import search_and_replace_tags

''' Utilizando diccionarios selecciono una funcion y retorno una referencia a ella para utilizarla mas adelante '''

def switch_principal(argument):
    switcher = {
        1: load_data,
        2: calendar,
        3: statistics,
        4: tools
    }
    func = switcher.get(argument)
    func()
    return


def switch_load(argument):
    switcher = {
        1: Cargar_dia,
        2: Limite_horarios,
        3: Carga_eventos,
        4: Ver_Data,
        5: Editar
    }
    return switcher.get(argument)


def switch_calendar(argument):

    switcher = {
        1: Ver_Todo,
        2: Ver_por_Mes,
        3: Ver_por_Dia
    }
    return switcher.get(argument)


def switch_statistics(argument):

    switcher = {
        1: Evolucion_de_Todo,
        2: Evolucion_en_un_Mes,
        3: Evolucion_entre_Fechas,
    }
    return switcher.get(argument)

def switch_tools(argument):

    switcher = {
        1: search_and_replace_tags
    }
    return switcher.get(argument)

    #  Resumen:
        ## Resumen general del total de la muestra
        ## Resumen entre fechas en especial
        ## Resumen por mes
    #  Visualizaciones:
        ## Ver por etiqueta respecto al tiempo total
            # Hay que tener en cuenta que realizo más de una acción a la vez para determinado horario.
            # Por lo tanto los % sumados no darán 100% sino superior.
        ## Visualizar por longitud de la acción no por tiempo total. Es decir si en total tengo 300h de estudio y
            # 150h de Series pero cuando veo las Series realizo 4 horas seguidas vs 2hs de Estudio entonces en este
            # ordenamiento las Series irían primero.
        ## Agrupar por Etiquetas más abarcativas de las ya registradas.
            # Ej: [Entretenimiento, Universidad, Hogar, Deporte, Tiempos Muertos, etc]
            # Entretenimiento = [Series, Cel, Juegos computadora, etc]
            # Universidad = [Estudio, Parcial, Clase, Fotocopias, etc]
            # Etc...







# Los puse abajo por problemas de dependencias circulares
from Funciones_Menu_Principal import load_data
from Funciones_Menu_Principal import calendar
from Funciones_Menu_Principal import statistics
from Funciones_Menu_Principal import tools