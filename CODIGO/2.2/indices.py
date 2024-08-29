import pandas as pd

import pandas as pd

def leer_df(ruta_archivo):

    df = pd.read_csv(ruta_archivo, nrows=20)
    return df


df = leer_df('BASES_DE_DATOS/ESI2017-SEXO.csv')
def verificar_columna(df, columna):

    return columna in df.columns
# Uso de la función
# Ejemplo con un DataFrame existente, como df_final o df_coeficientes
columna = 'sexo'
print(verificar_columna(df, columna))

#OK, la columna edad existe en el df

#Hay una columna denominada sexo
#hay una colmna denominada proyectada

print(df[columna])