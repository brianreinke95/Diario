from Inputs import Inputs
from clear import clear
from Comprobacion_Seleccion import Comprobacion_seleccion, Comprobacion_formato

# LOAD:
# Luego de que se ingresa el día y los límites se entra a un loop que te permite ir cargando de a principio a fin
# las actividades. Es decir, el horario inicial es el final anterior y uno fija el horario final. Junto a una
# descripción del evento.

# Los eventos tendrán etiquetas características para una mejor identificación para luego poder analizar la data.

# La carga termina cuando se llega al límite del horario.

# Los datos se cargarán en texto plano.


def Cargar_dia(Objeto):

    while True:
        flag, dia = Inputs('dia')
        if flag:
            Objeto.set_dia(dia)
            break
        else:
            input('Presione Enter para continuar...\n')


def Limite_horarios(Objeto):

    while True:

        flag, limites = Inputs('limites')

        if flag:
            limite_inferior = limites[0]
            limite_superior = limites[1]
            Objeto.set_limites(limite_inferior, limite_superior)
            break
        else:
            print('\nHa ingresado mal el formato, intente nuevamente\n')
            input('Presione Enter para continuar....\n')


def Carga_eventos(Objeto):

    '''
    Carga evento uno por uno en loop desde que comienza el día hasta que termina.

    Los límites de horarios identifican el momento en que me despierto y el momento en el que me duermo

    :param Objeto: Utiliza las funciones del objeto para ir cargando mediante inputs toda la data necesaria para
                   completar el dataframe
    :return: None
    '''

    print(Objeto.get_dia())
    print(Objeto.get_limites())
    y = True

    # Loop general. Terminará al llegar al límite superior.
    while y:
        # Previamente debo haber cargado el día en cuestión y la banda horaria.
        if Objeto.get_dia() is not None and Objeto.get_limites() is not None:
            x = True
            descripcion = input('Etiqueta:   ')
            aclaracion = input('Aclaracion/Opcional:   ')

            # Loop para ingresar con un correcto formato el horario.
            while x:
                flag, limite_superior = Inputs('evento')
                if flag:
                    x = False
                else:
                    print('\nHa ingresado mal el horario. Intente nuevamente.\n')

                # Acá se cambia el flag para salir del loop general.
                if limite_superior == Objeto.get_limites(limite='superior'):
                    y = False
                    print('\nSe han cargado todos los eventos del día\n')

            if not Objeto.check_if_not_empty():     # Si está vacío devuelve False. Por lo cual niego el False.
                # Si no había nada cargado utilizo el límite inferior cargado previamente.
                limite_inferior = Objeto.get_limites(limite='inferior')
            else:
                # El horario de finalización del evento anterior es el horario de comienzo del evento actual.
                limite_inferior = Objeto.get_last_limite_superior_cargado()

            Objeto.add_evento(descripcion, aclaracion, limite_inferior, limite_superior)  # Cargo datos en el df

        else:
            print('Imposible de cargar, algún campo anterior está vacío')
            # Muestro los valores para visualizar cuál de los dos está vacío.
            print(f'Día: {Objeto.get_dia()}')
            print(f'Límites Horarios: {Objeto.get_limites()}')
            break


    input('\nPresione Enter para volver al menú de carga...\n ')

    # Se debe corroborar que el día y los límites están completos
    # El horario inicial es el límite inferior para el primer caso
    # while loop ingresando inputs hasta llegar al límite superior.


def Ver_Data(Objeto):
    Objeto.Ver_DataFrame()
    input('\nPresione enter para salir.')


def Editar(Objeto):
    # Si modifico los horarios límites no debería modificar todos los otros datos cargados?
    if Objeto.check_if_not_empty():
        y = True
        while y:
            Objeto.Ver_DataFrame()

            fila = input('¿Qué Fila desea editar?...    ')
            columna = input('¿Qué campo desea editar? [Descripcion, Comienzo, Fin, Aclaracion]...    ')
            # Comprobar que fila es un número y no un string.

            data_index, data_columns = Objeto.get_data_index_and_columns()

            if not fila: b_i = False
            else:
                try:
                    fila = int(fila)
                    b_i = Comprobacion_seleccion(data_index, fila)  # Si existe la fila en cuestión.
                except ValueError:
                    b_i = Comprobacion_seleccion(data_index, fila)

            b_c = Comprobacion_seleccion(data_columns, columna)

            if b_i and b_c:
                x = True
                while(x):
                    seleccion = input(f'¿Desea modificar este valor {Objeto.get_item_from_data(fila, columna)}'
                                      f' ? [si/no]...   ')
                    if Comprobacion_seleccion(['si', 'no'], seleccion):
                        x = False
                        if seleccion == 'si':
                            edicion = input('Edición:   ')
                            ### Faltan las comprobaciones de todos tipo de formato.
                            Objeto.Editar_DataFrame(fila, columna, edicion)

            # Opción para seguir modificando:
            x = True
            while x:
                opcion = input('¿Desea Seguir Editando? [si, no]...')
                if Comprobacion_seleccion(['si', 'no'], opcion):
                    x = False
                    if opcion == 'no':
                        y = False
            clear()
    else:
        print('\nNo existen datos para modificar\n')
        input('Presione enter para continuar...\n')


def Cargar_a_Archivo(Objeto, csv_name):
    ''' Cargo el DataFrame a un csv.

    De ya existir actualizo el csv agregando filas al fondo '''
    from pathlib import Path

    my_file = Path('C:\Brian\PYTHON\Diario\\' + csv_name)

    if my_file.is_file():
        print('El archivo existe')
        # Completar si existe archivo
        with open(my_file, 'a') as file:
            Objeto.Load_to_Csv(file, csv_name)
        print('El archivo ha sido cargado\n')
        del Objeto  ## Luego de este punto ya finalizo la etapa de carga así que el objeto utilizado debe limpiarse

    else:
        print('El archivo no existe')
        Objeto.Load_to_Csv(my_file, csv_name)
        print('El archivo ha sido cargado')
        del Objeto
