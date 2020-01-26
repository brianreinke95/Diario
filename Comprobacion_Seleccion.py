
def Comprobacion_seleccion(lista_posible, seleccion):

    if seleccion not in lista_posible:
        print('\nERROR. No ha ingresado correctamente la opción.\nPor favor seleccione nuevamente\n')
        input('Presione Enter para continuar...\n')
        return False
    else:
        return True


import re as regex

def Comprobacion_formato(RegEx, seleccion):
    # La selección debe seguir el mismo formato que la Regular Expression

    if regex.search(RegEx, seleccion):

        if RegEx == r'^\d{2}:\d{2}':
            lista = seleccion.split(':')
            lista = [int(elemento) for elemento in lista]
            if lista[0] > 23 or lista[0] < 00:
                return False
            if lista[1] > 59 or lista[1] < 00:
                return False
            return True

        if RegEx == r'^\d{1,2}/\d{2}/\d{4}':
            lista = seleccion.split('/')
            lista = [int(elemento) for elemento in lista]
            if lista[0] > 31 or lista[0] < 0:
                return False
            if lista[1] > 12 or lista[1] < 1:
                return False
            if lista[2] > 2020 or lista[2] < 2019:
                # Sujeto a cambios. Usar funciones cronómetro que tengan el año actual
                return False
            return True
        return False

    else:
        return False

        # r'^\d{3}-\d{3}-\d{4}'
