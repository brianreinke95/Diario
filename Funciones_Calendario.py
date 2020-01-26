from Inputs import Inputs

def Ver_Todo(Objeto):
    '''
    Muestra un listado de todos los dias cargados. Con la particularidad de marcar con un simbolo aquellos destacados.

    :param Objeto:
    :return:
    '''

    Objeto.set_destacados()       # Carga el csv de destacados
    Objeto.print_destacados()      # Muestra el listado
    pass

def Ver_por_Mes(Objeto):
    '''
    Imprime uno por uno todos los DataFrame correspondientes al mes especificado

    Por consola se muestran los meses disponibles
    Por consola se ingresa el mes a imprimir
    '''

    meses = Objeto.get_meses_disponibles()
    flag, mes_seleccionado = Inputs('meses', meses)

    if flag:
        Objeto.print_mes_seleccionado(mes_seleccionado)


def Ver_por_Dia(Objeto):
    '''
    Imprime el DataFrame de un dia en particular

    Se muestra por consola todos los dias disponibles a imprimir
    Se ingresa por consola el dia a imprimir.
    '''

    dias, all_days_dfs = Objeto.print_dias_disponibles()
    flag, dia_seleccionado = Inputs('dia', dias)

    if flag:
        Objeto.print_dia_seleccionado(all_days_dfs, dia_seleccionado)
