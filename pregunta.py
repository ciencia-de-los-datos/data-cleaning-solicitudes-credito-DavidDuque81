"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    #Leer el archivo
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    #Eliminar innecesarios
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df.dropna(how='any', inplace=True)
    df.drop_duplicates(inplace=True)
    #Sexo
    df['sexo'] = df['sexo'].apply(lambda x: x.lower().strip())
    #Tipo de emprendimiento
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(lambda x: x.lower().strip())
    #Idea Negocio
    df['idea_negocio'] = df['idea_negocio'].apply(lambda x: x.lower().strip())
    df['idea_negocio'] = df['idea_negocio'].str.replace('-', ' ')
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ')
    df['idea_negocio'] = df['idea_negocio'].str.strip()
    #Barrio
    df['barrio'] = df['barrio'].astype(str)
    df['barrio'] = df['barrio'].apply(str.lower)
    df.barrio = df.barrio.str.replace("_", " ", regex=False)
    df.barrio = df.barrio.str.replace("-", " ", regex=False)
    df.barrio = df.barrio.str.replace(".", " ", regex=False)
    df.barrio = df['barrio'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    #Fecha
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)
    #Monto del crredito
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: int(x.split('$ ')[-1].split('.')[0].replace(',','')))
    #Linea de credito
    df['línea_credito'] = df['línea_credito'].apply(lambda x: x.lower().strip())
    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.strip()
    #df['línea_credito'] = df['línea_credito'].str.replace('soli diaria', 'solidaria')
    #df['línea_credito'] = df['línea_credito'].str.replace('empresarial ed. ', 'empresarial ed.')
    #Eliminar duplicados e innecesarios
    df.dropna(how='any', inplace=True)
    df.drop_duplicates(inplace=True)

    return df
