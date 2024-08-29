from lectura_csv import df_base
import pandas as pd
import numpy as np

# Uso de la función
ruta_archivo = 'BASES_DE_DATOS/ESI2017-PERSONAS.csv'

df_final = df_base(ruta_archivo)

print(df_final)

#En base a esto puedo calcular los distintos coeficientes
#voy a crear un nuevo df que se llame coeficientes

def crear_df_coeficientes(df_final):
    """
    Crea un DataFrame df_coeficientes con una columna Xi que es el logaritmo base 10
    del ingreso per capita, ignorando los hogares donde el ingreso per capita es 0.

    :param df_final: DataFrame que contiene la columna 'ingreso_per_capita'
    :return: DataFrame con la columna Xi
    """
    # Filtrar los registros donde ingreso_per_capita es mayor que 0
    df_filtrado = df_final[df_final['ingreso_per_capita'] > 0]
    
    # Calcular el logaritmo base 10 del ingreso per capita
    df_coeficientes = pd.DataFrame()
    df_coeficientes['Xi'] = np.log10(df_filtrado['ingreso_per_capita'])

    # Agrego los coeficientes restantes
    df_coeficientes['Xp'] = df_filtrado['Xp']
    df_coeficientes['Xe'] = df_filtrado['Xe']
    df_coeficientes['Xt'] = df_filtrado['Xt']
    df_coeficientes['Xj'] = df_filtrado['Xj']

    return df_coeficientes

# Uso de la función
df_coeficientes = crear_df_coeficientes(df_final)

print(df_coeficientes)