import pandas as pd
import os

def join_data(year):
    inputfile1 = f'data/data_csv/wr_standard_stats_{year}.csv'
    inputfile2 = f'data/data_csv/wr_advanced_stats_{year}.csv'
    outputfile = f'data/data_csv/wr_complete_stats_season_{year}.csv'

    df = pd.read_csv(inputfile1, sep=",", encoding="utf-8")
    df_2 = pd.read_csv(inputfile2, sep=",", encoding="utf-8")

    columnas = ['1D', 'Awards', 'Age', 'G', 'GS', 'Player', 'Pos', 'Rec', 'Team', 'Tgt', 'Yds']
    # Eliminar la columnas
    for col in columnas:
        if col in df.columns:
           df = df.drop(columns=[col])

    if '-9999' in df.columns:
        df = df.rename(columns={'-9999': 'WR_ID'})
        print('renombrado')

    if '-9999' in df_2.columns:
        df_2 = df_2.rename(columns={'-9999': 'WR_ID'})
        print('renombrado 2')

    # Agregar una columna 'Season'
    df['Season'] = year

    df_complete = pd.merge(df_2, df, on='WR_ID')

    # Guardar como CSV
    df_complete.to_csv(outputfile, index=False, encoding="utf-8")

    print(f"✅ Archivo convertido con éxito: {outputfile}")

def join_all_data():
    # Lista para almacenar los DataFrames
    qb_dataframes = []
    for year in range(2018,2025):
        join_data(year)
        inputfile = f'data/data_csv/wr_complete_stats_season_{year}.csv'
        df = pd.read_csv(inputfile,sep=",", encoding="utf-8")
        # Agregar el DataFrame a la lista
        qb_dataframes.append(df)

    # Unir todos los DataFrames en uno solo
    qb_complete = pd.concat(qb_dataframes, ignore_index=True)

    # Columnas donde NaN debe reemplazarse con 0 (ajusta según tus columnas reales)
    zero_columns = ['G', 'GS', 'Tgt', 'Rec', 'Yds', '1D', 'YBC', 'YAC', 
                    'BrkTkl', 'Drop', 'R/G', 'Y/G', 'Y/Tgt']

    # Aplicar reemplazo solo en las columnas seleccionadas
    qb_complete[zero_columns] = qb_complete[zero_columns].fillna(0)

    # Convertir columnas numéricas (esto ahora es más seguro)
    qb_complete = qb_complete.apply(pd.to_numeric, errors='ignore')

    # Guardar el DataFrame consolidado
    qb_complete.to_csv('data/qb_complete_stats.csv', index=False)

    print(qb_complete[['Tgt', 'Rec', 'TD', 'Rat']].isna().sum())

join_all_data()
