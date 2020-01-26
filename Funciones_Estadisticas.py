from Inputs import Inputs

#################### Funciones que acceden a los gráficos #######################

def Horas_por_Etiqueta(Objeto):
    Objeto.Graph_Horas_por_Etiqueta()


def Evolucion_segun_etiqueta(Objeto):
    etiquetas = Objeto.get_etiquetas_mas_frecuentes()

    flag, etiqueta = Inputs('etiquetas', etiquetas)

    if flag:
        Objeto.Graph_Evolucion_por_Dia(etiqueta)


def Acumulado_segun_Dia_de_la_Semana(Objeto):

    Objeto.set_dias_de_la_semana()
    Objeto.Graph_actividades_por_dia_de_la_semana()     # Stacked Plot  [Etiqueta 1, 2, 3, 4, others]
    input('...')


#################### Funciones que modifican el DataFrame ############################

def Evolucion_de_Todo(Objeto):
    Acumulado_segun_Dia_de_la_Semana(Objeto)
    Horas_por_Etiqueta(Objeto)
    Evolucion_segun_etiqueta(Objeto)


def Evolucion_en_un_Mes(Objeto):

    meses_disponibles = Objeto.get_meses_disponibles()

    flag, mes_seleccionado = Inputs('meses', meses_disponibles)

    if flag:
        Objeto.modify_etiquetas_df_by_month(mes_seleccionado)       # Obtengo un Objeto donde etiquetas_df está limitada
                                                                    # al mes seleccionado
        Acumulado_segun_Dia_de_la_Semana(Objeto)
        Horas_por_Etiqueta(Objeto)
        Evolucion_segun_etiqueta(Objeto)       # Trabajo con el Objeto modificado.

def Evolucion_entre_Fechas(Objeto):

    fechas_disponibles = Objeto.get_all_days()
    print(fechas_disponibles)

    flag, fecha_inicial, fecha_final = Inputs('entre_fechas', fechas_disponibles)

    print(flag, fecha_inicial, fecha_final)

    if flag:
        Objeto.modify_etiquetas_df_by_fechas(fecha_inicial, fecha_final)
        Acumulado_segun_Dia_de_la_Semana(Objeto)
        Horas_por_Etiqueta(Objeto)
        Evolucion_segun_etiqueta(Objeto)






