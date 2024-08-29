from coeficientes import crear_df_coeficientes
import pandas as pd
import matplotlib.pyplot as plt

# Uso de la función
ruta_archivo = 'BASES_DE_DATOS/ESI2017-PERSONAS.csv'
df = crear_df_coeficientes(ruta_archivo)


def promedio(df):

    x = df['Xi'] #Aun no se que usar en el eje X
    y = -2.1723 + 0.3792 * df['Xi'] + 0.6221 * df['Xp'] + 1.0065 * df['Xe'] + 0.4302 * df['Xt'] + 0.1614 * df['Xj']

    lista = []
    for elementos in y:
        lista.append(elementos)
        
    promedio = sum(lista) / len(lista)

    return(promedio)

# Graficar
print(promedio(df))