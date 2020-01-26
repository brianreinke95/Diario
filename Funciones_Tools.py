from Inputs import Inputs
import pandas as pd

def search_and_replace_tags():
    df = pd.read_csv('C:\Brian\PYTHON\Diario\\Diario-copia.csv', sep=';', encoding='latin1')
    df = df.fillna('-')
    print(df)

#search_and_replace_tags()