from Comprobacion_Seleccion import Comprobacion_seleccion
from Comprobacion_Seleccion import Comprobacion_formato
from clear import clear

"""
Apartado de logica para unificar todos los inputs similares.

Argumentos:
            tipo:                  Tipo de input. Puede ser: dia-mes-hora para entrar a distintas partes del codigo.
            valores_posibles:      Lista de valores posibles para la Comprobacion de seleccion
            
Retorna:    Bool:                  Para logica futura
            seleccion:             input ingresado

"""


def Inputs(tipo, valores_posibles=None):

    if tipo == 'dia':
        redox = r'^\d{1,2}/\d{2}/\d{4}'
        # Logica general para ingresar Dia.
        seleccion = input('\nSeleccionar dia [dd/mm/yyyy]:   ')
        clear()
        if Comprobacion_formato(redox, seleccion):
            if valores_posibles is not None:
                if Comprobacion_seleccion(valores_posibles, seleccion):
                    print('\n\n')
                    return True, seleccion
                else:
                    print('\nHa seleccionado mal el dia')
                    return False, None
            else:
                return True, seleccion
        else:
            print('\nHa cargado mal el dia. Compruebe el formato e intente nuevamente.\n')
            return False, None

    elif tipo == 'meses':
        seleccion = input('Seleccionar mes (En letras):   ')

        if Comprobacion_seleccion(valores_posibles, seleccion):
            return True, seleccion
        else:
            'Ha seleccionado mal el mes'
            return False, None

    elif tipo == 'limites':
        redox = r'^\d{2}:\d{2}'
        print('Carga de limites de horarios')

        limite_inferior = input('Limite Inferior [hh:mm]:  ')
        limite_superior = input('Limite Superior [hh:mm]:  ')

        if Comprobacion_formato(redox, limite_inferior) and Comprobacion_formato(redox, limite_superior):
            return True, (limite_inferior, limite_superior)
        else:
            return False, None

    elif tipo == 'evento':
        redox = r'^\d{2}:\d{2}'
        limite_superior = input('Tiempo de finalización del evento [hh:mm]:   ')
        if Comprobacion_formato(redox, limite_superior):
            return True, limite_superior
        else:
            return False, None

    elif tipo == 'etiquetas':
        etiqueta = input('Escriba la Etiqueta para ver su evolución:  ')
        if Comprobacion_seleccion(lista_posible=valores_posibles, seleccion=etiqueta):
            return True, etiqueta
        else:
            return False, None

    elif tipo == 'entre_fechas':
        redox = r'^\d{1,2}/\d{2}/\d{4}'
        fecha_inicial = input('Fecha Inicial... ')
        fecha_final = input('Fecha final...  ')

        if Comprobacion_formato(redox, fecha_final) and Comprobacion_formato(redox, fecha_inicial):

            if Comprobacion_seleccion(valores_posibles, seleccion=fecha_inicial) and Comprobacion_seleccion(
                    valores_posibles, seleccion=fecha_final):

                return True, fecha_inicial, fecha_final
            else:
                return False, None
        else:
            return False, None

    else:
        raise ValueError('"tipo" de input incopatible.')