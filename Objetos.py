import pandas as pd
import numpy as np
from Comprobacion_Seleccion import Comprobacion_formato
from Comprobacion_Seleccion import Comprobacion_seleccion
pd.options.mode.chained_assignment = None  # default='warn'
from datetime import datetime
from clear import clear
import seaborn as sns
import matplotlib.pyplot as plt
from Inputs import Inputs
import locale




desired_width = 1000
pd.set_option("display.max_columns", 12)
pd.set_option("display.max_rows", 100)
pd.set_option('display.width', desired_width)
pd.set_option('display.colheader_justify', 'rigth')

Diario = 'Diario.csv'
Destacado = 'Destacados.csv'
Combinaciones_para_tags = ['S', 'A', 'P', r'{A, S, P} + {A, S, P}']

FALSE_VALUE = 99999

class Registro():
    def __init__(self):
        self.dia = None
        self.limites = None
        self.eventos_df = pd.DataFrame([])

    def set_dia(self, dia):
        self.dia = dia

    def set_limites(self, limite_inferior, limite_superior):
        self.limites = (limite_inferior, limite_superior)

    def add_evento(self, descripcion, aclaracion, limite_inferior, limite_superior):

        self.eventos_df = self.eventos_df.append(
            pd.DataFrame({'Dia': self.dia, 'Descripcion': descripcion, 'Comienzo': limite_inferior,
                          'Fin': limite_superior, 'Aclaracion': aclaracion}, index=[0]), ignore_index=True, sort=False)

    def add_destacado(self, dia, destacado, aclaracion=None, simbolo=None):
        self.destacados_df = pd.DataFrame({
            'Fecha': dia, 'Destacados': destacado, 'Tag': simbolo, 'Asunto': aclaracion}, index=[0])
        print(self.destacados_df)

    def Ver_DataFrame(self):
        print()
        print(self.eventos_df)
        print()



    def Editar_DataFrame(self, index, parametro, edicion):
        ## Acá con algún switch case podría validar los inputs
        self.eventos_df.loc[index][parametro] = edicion

    def Load_to_Csv(self, file, csv_name):
        if csv_name == Diario:
            self.eventos_df.to_csv(file, header=False, sep=';', index=False, encoding='latin1')
        elif csv_name == Destacado:
            self.destacados_df.to_csv(file, header=False, sep=';', index=False, encoding='latin1')
        else:
            raise ValueError('csv_name no válido')

    def check_if_not_empty(self):
        ''' Return True if dataframe isn´t empty. '''
        return not self.eventos_df.empty

    def get_data_index_and_columns(self):
        return self.eventos_df.index, self.eventos_df.columns

    def get_item_from_data(self, row, col):
        return self.eventos_df[col].iloc[row]

    def get_dia(self):
        return self.dia

    def get_limites(self, limite = None):
        if limite is None:
            return self.limites
        elif limite == 'inferior':
            return self.limites[0]
        elif limite == 'superior':
            return self.limites[1]
        else:
            raise ValueError('Descripción no válida')

    def get_last_limite_superior_cargado(self):
        return self.eventos_df['Fin'].iloc[-1]

    def get_all_days(self):

        all_days_datetime = self.eventos_df['Dia'].unique()
        all_days_string = [date.strftime('%d/%m/%Y') for date in all_days_datetime]
        return all_days_string

    def get_meses_disponibles(self):
        self.eventos_df['Mes'] = pd.to_datetime(self.eventos_df['Dia'], format='%Y-%m-%d').dt.month_name(
            locale='Spanish')
        _meses_disponibles = self.eventos_df.Mes.unique()
        print(_meses_disponibles, '\n')
        return _meses_disponibles

class Calendario(Registro):
    def __init__(self):
        super().__init__()
        self.eventos_df = pd.read_csv('C:\Brian\PYTHON\Diario\\' + Diario, sep=';', encoding='latin1')
        self.eventos_df.Dia = pd.to_datetime(self.eventos_df.Dia, dayfirst=True, format='%d/%m/%Y').dt.date

        self.eventos_df = self.eventos_df.fillna('-')

#######################################  Ver_Todo   ##################################################
    def set_destacados(self):

        ''' Carga el csv de destacados a un dataframe y lo setea para su uso.

        asd'''

        self.eventos_destacados = pd.read_csv('C:\Brian\PYTHON\Diario\\' + Destacado, sep=';', encoding='latin1')
        self.eventos_destacados.Fecha = pd.to_datetime(self.eventos_destacados.Fecha,
                                                       dayfirst=True, format='%d/%m/%Y').dt.date
        self.eventos_destacados = self.eventos_destacados.fillna('-')


        self.eventos_destacados['Fecha'] = pd.to_datetime(self.eventos_destacados['Fecha'],
                                                          format='%Y-%m-%d')
        self.eventos_destacados = self.eventos_destacados.sort_values(by='Fecha', ascending=True)
        self.eventos_destacados['Fecha'] = self.eventos_destacados['Fecha'].dt.strftime('%d/%m/%Y')
        self.eventos_destacados = self.eventos_destacados.replace(['SI', 'NO'], [True, False])

    def print_destacados(self):

        ''' Muestra todos los días que se han registrado en el diario

            A futuro se visualizará un widget que utilizará google calendar o algo así
        '''

        def _mostrar_dias(dia, destacado, tag):
            if destacado:
                tag = tag.replace(' ', '')
                tag = tag.replace('+', ' ')
                print(dia + ' ' + tag)
            else:
                print(dia)

        self.eventos_destacados.apply(lambda _row: _mostrar_dias(dia=_row['Fecha'], destacado=_row['Destacados'],
                                                                 tag=_row['Tag']), axis=1)

###########################################################################################################
################################## Ver_por_Mes  #########################################################3

    def print_mes_seleccionado(self, mes_seleccionado):

        '''
        Imprime todos los DataFrame correspondientes al mes especificado

        asd
        '''

        _group = self.eventos_df.groupby('Mes')
        _data_del_mes = _group.get_group(mes_seleccionado)

        _data_del_mes['Dia'] = pd.to_datetime(_data_del_mes['Dia'], format='%Y-%m-%d').dt.strftime('%d/%m/%Y')

        _all_days_df = _data_del_mes.groupby('Dia')  # Separo por día

        for dia, data in _all_days_df:
            data.set_index('Descripcion', inplace=True)
            del data['Dia']
            del data['Mes']
            print('\n' + dia)
            print(data)
            input('\nEnter para continuar...')
            clear()
            print('\n')

##################################################################################################################3

    def print_dias_disponibles(self):

        '''
        Muestra el listado de todos los dias cargados y devuelve una lista y un dataframe con todos ellos.

        Utiliza el csv de destacados para mostrar los dias.

        :return: dias: listado de todos los dias disponibles a seleccionar
                 all_days_df: GROUPBY dataframe por dia, compuesto de toda la data cargada hasta el momento.
        '''

        self.eventos_df['Dia'] = pd.to_datetime(self.eventos_df['Dia'], format='%Y-%m-%d').dt.strftime('%d/%m/%Y')
        all_days_dfs = self.eventos_df.groupby('Dia')
        dias = self.eventos_df['Dia'].unique()

        self.set_destacados()
        self.print_destacados()

        return dias, all_days_dfs

    def print_dia_seleccionado(self, all_days_dfs, dia_seleccionado):

        '''
        A partir de la seleccion se sustrae el dataframe correspondiente y se lo imprime en pantalla.

        :param all_days_dfs: Grupos de dataframes por dia.
        :param dia_seleccionado
        :return: None
        '''

        _day_df = all_days_dfs.get_group(dia_seleccionado)
        del _day_df['Dia']
        _day_df.set_index('Descripcion', inplace=True)
        print(_day_df)




class Estadisticas(Registro):
    def __init__(self):
        super().__init__()
        self.eventos_df = pd.read_csv('C:\Brian\PYTHON\Diario\\' + Diario, sep=';', encoding='latin1')
        self.eventos_df.Dia = pd.to_datetime(self.eventos_df.Dia, dayfirst=True, format='%d/%m/%Y').dt.date
        self.eventos_df = self.eventos_df.fillna('-')

    def min_float_to_hh_mm(self, minutes):
        res = int(minutes / 60)
        coma = int(minutes % 60)
        return '{}:{:02d}'.format(res, coma)

    def set_Etiquetas(self):

        '''
        Función que prepara el dataframe para poder realizar cálculos y gráficas:

            Separa todas las etiquetas en filas únicas
            Obtiene la duración de cada evento

        :param: self
        :return self.etiquetas_df: DataFrame utilizado por las demás funciones de la clase.
        '''

        # Función dentro de etiquetas que devuelve la diferencia entre los horarios para obtener la duración del evento
        def DiffTime(Start, End):

            '''
            Obtendré el valor float de los minutos entre el horario de inicio y final del evento.

            Y pasaré este valor a una representación string "hh:mm"

            :param Start: Horario inicial del evento
            :param End: Horario final del evento
            :return: Retorno el valor Float y su representación en string
            '''

            minutes_float = pd.Timedelta((End - Start)).seconds / 60
            minutes_string = self.min_float_to_hh_mm(minutes_float)
            return minutes_float, minutes_string

        # Se genera una lista de strings en la descripción con etiquetas múltiples
        # que luego separaré en 2 filas distintas:
        self.eventos_df.Descripcion = self.eventos_df.Descripcion.str.split('+')
        # Nota: Podría modificar el formato de las Aclaraciones para tambien separar por split

        # Obteniendo los duplicados:
        new_df = pd.DataFrame({
            'Dia': self.eventos_df.Dia.repeat(self.eventos_df.Descripcion.apply(len)),
            'Descripcion': np.concatenate(self.eventos_df.Descripcion.values),
            'Comienzo': self.eventos_df.Comienzo.repeat(self.eventos_df.Descripcion.apply(len)),
            'Fin': self.eventos_df.Fin.repeat(self.eventos_df.Descripcion.apply(len)),
            'Aclaracion': self.eventos_df.Aclaracion.repeat(self.eventos_df.Descripcion.apply(len))
        })
        new_df.Descripcion = new_df.Descripcion.apply(lambda x: x.strip())   # Le saco espacios en blanco.

        # Utilizo un dataframe auxiliar para aplicar funciones solo a los horarios:
        df_aux = new_df[['Comienzo', 'Fin']]
        df_aux = df_aux.apply(pd.to_datetime, axis=1)
        df_aux = df_aux.apply(pd.to_timedelta, axis=1)     # TimeDelta para poder obtener diferencias

        # Para cada fila del dataframe se calculará la duración del evento.
        # Devuelve dos columnas: [valor float, representacion string]
        Diferencia = df_aux.apply(lambda x: DiffTime(Start=x['Comienzo'], End=x['Fin']), axis=1)

        Diferencia = pd.DataFrame(Diferencia.tolist())
        Diferencia.columns = ['Float', 'String']

        # Cargo estas nuevas columnas al Df expandido (con las etiquetas separadas)
        new_df['Diff_Float'] = Diferencia['Float']
        new_df['Diff_String'] = Diferencia['String']

        new_df = new_df.sort_values('Dia', ascending=True)

        self.etiquetas_df = new_df


    ######################  Funciones Auxiliares  #########################
    def get_etiquetas_mas_frecuentes(self):
        clear()

        print('Apariciones más frecuentes:\n\n')
        etiquetas = self.etiquetas_df['Descripcion'].value_counts().head(15)
        print(etiquetas, '\n')
        return etiquetas

    def get_meses_disponibles(self):
        self.etiquetas_df['Mes'] = pd.to_datetime(self.eventos_df['Dia'],
                                                  format='%Y-%m-%d').dt.month_name(locale='Spanish')
        _meses_disponibles = self.etiquetas_df.Mes.unique()
        print(_meses_disponibles, '\n')
        return _meses_disponibles

    def set_dias_de_la_semana(self):
        """
        Utilizando las funciones de datetime agrego una columna al dataframe con el nombre del dia de la semana

            Ademas se debió utilizar un par de lineas mas para ordenar de lunes a domingo.
        :return: None
        """

        locale.setlocale(locale.LC_TIME, '')        # En cada llamado a Objetos se debería ejecutar para que aplique.
        order = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

        self.etiquetas_df['Week_Day'] = self.etiquetas_df.apply(lambda row: row['Dia'].strftime('%A'), axis=1)
        category_day = pd.api.types.CategoricalDtype(categories=order, ordered=True)
        self.etiquetas_df['Week_Day'] = self.etiquetas_df['Week_Day'].astype(category_day)
        print(self.etiquetas_df)
        # %a retorna una abreviatura del nombre del dia de la semana.

    #################  Funciones que modifican el tamaño del DataFrame  ##########################
    def modify_etiquetas_df_by_month(self, mes_seleccionado):
        '''
        Modifico el DF para quedarme solo con el mes seleccionado

        :param mes_seleccionado:
        :return:
        '''

        self.etiquetas_df = self.etiquetas_df.groupby('Mes').get_group(mes_seleccionado)

    def modify_etiquetas_df_by_fechas(self, fecha_inicial, fecha_final):
        '''
        Modifico el DF para quedarme solo con la data entre las fechas seleccionadas

        :param fecha_inicial:
        :param fecha_final:
        :return:
        '''

        fecha_inicial = datetime.strptime(fecha_inicial, '%d/%m/%Y').date()
        fecha_final = datetime.strptime(fecha_final, '%d/%m/%Y').date()

        self.etiquetas_df = self.etiquetas_df.loc[
            (self.etiquetas_df['Dia'] >= fecha_inicial) & (self.etiquetas_df['Dia'] <= fecha_final)]

##################################  Funciones que grafican  ###########################################
    def Graph_Horas_por_Etiqueta(self):

        '''
        Agrupar por etiquetas y plotear un gráfico que muestre las horas acumuladas por cada etiqueta.

        Esta función puede ser llamada para plotear ttodo el dataframe o fragmentos según conveniencia.
        Por ejemplo se podría plotear el acumulado solo para el mes de Noviembre.

        :param new_df: DataFrame a visualizar
        :return None
        '''

        clear()
        plt.figure(figsize=(14, 5))

        _etiquetas_df = self.etiquetas_df.groupby('Descripcion').sum().sort_values(by='Diff_Float', ascending=False)
        _etiquetas_df = _etiquetas_df.apply(lambda x: round(x/60, 2))     # Ploteo en horas

        # Utilizo Seaborn para los gráficos
        sns.barplot(x=_etiquetas_df.head(10).index, y=_etiquetas_df.head(10).Diff_Float, data=_etiquetas_df)
        plt.ylabel('Horas')
        plt.tight_layout()
        plt.show()

        # Mostrar por consola todos los resultados:
        g_string = _etiquetas_df.apply(lambda x: self.min_float_to_hh_mm(x), axis=1)  # float a repr string.
        print(g_string)


    def Graph_Evolucion_por_Dia(self, etiqueta):

        ''' Evolución por día de una etiqueta en particular.

        Es decir que día a día se graficará la cantidad de horas invertidas en cierta actividad.

        Al igual que con "Horas_por_etiqueta" la muestra a visualizar dependerá del dataframe ingresado.

        :param new_df: DataFrame a visualizar
        :return None
        '''

        plt.figure(figsize=(10, 5))
        plt.style.use('seaborn-dark')

        _etiqueta_seleccionada_df = self.etiquetas_df.groupby('Descripcion').get_group(etiqueta)
        _etiqueta_seleccionada_por_dia = _etiqueta_seleccionada_df.groupby('Dia').sum()
        _etiqueta_seleccionada_por_dia['Diff_Float'] = _etiqueta_seleccionada_por_dia['Diff_Float'] / 60

        plt.bar(_etiqueta_seleccionada_por_dia.index, _etiqueta_seleccionada_por_dia['Diff_Float'], label=etiqueta)
        plt.ylabel('Horas')
        plt.title('Evolución por Día')
        plt.grid(True)
        plt.legend()

        # Roto los ejes para mejor visibilidad de los textos.
        ax = plt.gca()
        for tick in ax.get_xticklabels():
            tick.set_rotation(30)

        for tick in ax.get_yticklabels():
            tick.set_rotation(0)

        plt.tight_layout()
        plt.show()

        print(_etiqueta_seleccionada_por_dia)


    def Graph_actividades_por_dia_de_la_semana(self):

        '''
        Agrupa las actividades por dia de la semana. Saca un porcentaje aproximado y hace un pie chart de cada dia

        :return: None
        '''

        plt.style.use('fivethirtyeight')
        group_by_day_of_week = self.etiquetas_df.groupby('Week_Day')

        # Subplots por cada día de la semana.
        for i, day_data in enumerate(group_by_day_of_week, 1):

            day_name = day_data[0]
            day_df = day_data[1]

            if not day_df.empty:
                number_days = len(day_df['Dia'].unique())

                day_group = day_df.groupby('Descripcion').sum().sort_values(by='Diff_Float', ascending=False)

                day_group = day_group.reset_index()

                day_group.Descripcion = day_group.Descripcion.astype('category')

                day_group['promedio_por_dia'] = round(day_group['Diff_Float'] / number_days, 3)

                minutos_totales = day_group['promedio_por_dia'].sum()



                day_group['porcentaje_por_etiqueta'] = day_group.apply(lambda x: round(x['promedio_por_dia'] / minutos_totales, 3),
                                                                       axis=1)

                # Para que el pie chart no se llene de actividades agrupo todas las de menor incidencia en
                # categoria "Others"
                small_categorys = day_group[day_group['porcentaje_por_etiqueta'] <= 0.050]

                day_group = day_group.replace({
                    'Descripcion': list(small_categorys['Descripcion'].values),
                    'porcentaje_por_etiqueta': list(small_categorys['porcentaje_por_etiqueta'].values),
                    'promedio_por_dia': list(small_categorys['promedio_por_dia'].values),
                    'Diff_Float': list(small_categorys['Diff_Float'].values)
                }, {
                    'Descripcion': 'Others',
                    'porcentaje_por_etiqueta': small_categorys['porcentaje_por_etiqueta'].sum(),
                    'promedio_por_dia': small_categorys['promedio_por_dia'].sum(),
                    'Diff_Float': small_categorys['Diff_Float'].sum()})


                day_group = day_group.drop_duplicates(['Descripcion'])


                plt.subplot(2, 4, i)

                plt.pie(day_group['promedio_por_dia'], labels=day_group['Descripcion'], wedgeprops={'edgecolor': 'black'},
                        autopct='%1.1f%%', pctdistance=0.76, textprops={'fontsize': 7}, radius=.9,
                        labeldistance=1.15, explode=[0.05]*len(day_group.index))

                plt.title(f'{day_name}')
            else:
                plt.subplot(2, 4, i)
                plt.axis('off')

        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.show()









