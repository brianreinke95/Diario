from Objetos import FALSE_VALUE

def menu():
    print('Cargar Datos. Press 1')
    print('Ver Calendario. Press 2')
    print('Ver estadísticas. Press 3')
    print('Herramientas. Press 4')
    print('Exit. Press 0')
    print()

    x = input('Ingresar opción:  ')
    if not x:
        x = 999999
    else:
        try:
            return int(x)
        except ValueError:
            return x


def menu_datos():
    print()
    print('Cargar día. Press 1')
    print('Cargar límites de horarios. Press 2')
    print('Comenzar a cargar eventos. Press 3')
    print('Ver estado de la carga. Press 4')
    print('Editar algún campo. Press 5')
    print('\nFinalizar Carga. Press 9')
    print('Cancelar. Press 0')
    print()

    x = input('Ingresar Opción:   ')
    try:
        x = int(x)
        if x is None:
            x = FALSE_VALUE
    except ValueError:
        x = FALSE_VALUE
    return x


def menu_calendar():
    print()
    print('Ver todo el calendario. Press 1')
    print('Ver registros por mes. Press 2')
    print('Ver dia en especial. Press 3')

    print('\nCancelar. Press 0')
    print()

    x = input('Ingresar Opción:   ')

    try:
        x = int(x)
        if x is None:
            x = FALSE_VALUE
    except ValueError:
        x = FALSE_VALUE
    return x


def menu_statistics():
    print()
    print('Evolución de TODO. Press 1')
    print('Evolución por Mes. Press 2')
    print('Evolución entre Fechas. Press 3')

    print('\nCancelar. Press 0')
    print()

    x = input('Ingresar Opción:   ')

    try:
        x = int(x)
        if x is None:
            x = FALSE_VALUE
    except ValueError:
        x = FALSE_VALUE
    return x


def menu_tools():
    print()
    print('Search and replace TAGS. Press 1')
    print('\nCancelar. Press 0')

    x = input('Ingresar Opción:   ')

    try:
        x = int(x)
        if x is None:
            x = FALSE_VALUE
    except ValueError:
        x = FALSE_VALUE
    return x
