from lectura_csv import df_base
import pandas as pd
import numpy as np




# print(df_final)

#En base a esto puedo calcular los distintos coeficientes
#voy a crear un nuevo df que se llame coeficientes

def crear_df_coeficientes(ruta_archivo):

    df_final = df_base(ruta_archivo)

    # Filtrar los registros donde ingreso_per_capita es mayor que 0
    df_filtrado = df_final[df_final['ingreso_per_capita'] > 0]
    
    # Calcular el logaritmo base 10 del ingreso per capita
    df_coeficientes = pd.DataFrame()

    print(f'el ingrweso per capita promedio es {df_filtrado["ingreso_per_capita"].mean()}')
    df_coeficientes['Xi'] = np.log10(df_filtrado['ingreso_per_capita'])

    # Agrego los coeficientes restantes
    df_coeficientes['Xp'] = df_filtrado['Xp']
    df_coeficientes['Xe'] = df_filtrado['Xe']
    df_coeficientes['Xt'] = df_filtrado['Xt']
    df_coeficientes['Xj'] = df_filtrado['Xj']

    return df_coeficientes

def coef_promediados (ruta_archivo):
    df_coeficientes = crear_df_coeficientes(ruta_archivo)
    numero_hogares = len(df_coeficientes)
    df_coeficientes_promediados = df_coeficientes.mean()
    df_coeficientes_promediados['numero_hogares'] = numero_hogares

    return df_coeficientes_promediados


