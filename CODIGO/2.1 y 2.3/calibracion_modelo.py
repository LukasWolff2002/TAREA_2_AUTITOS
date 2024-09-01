from coeficientes import coef_promediados
import pandas as pd
import matplotlib.pyplot as plt

def promedio_hogares(df, año):
    if año == 2012:
        ponderacion = 1
    elif año == 2017:
        ponderacion = 2
    elif año == 2023:
        ponderacion = 3

    xi = df['Xi']
    y = -2.1723 + 0.3792 * df['Xi'] + 0.6221 * df['Xp'] + 1.0065 * df['Xe'] + 0.4302 * df['Xt'] + 0.1614 * df['Xj']
    hogares = df['numero_hogares']    
    return(y, hogares)

#Uso de la función
ruta_archivo = 'BASES_DE_DATOS/ESI2012-PERSONAS.csv'
df = coef_promediados(ruta_archivo)

numero_viajes, cantidad_hogares = promedio_hogares(df, 2012)
print('2012')
print(f"El promedio de viajes por hogar es de {numero_viajes:.2f} y se analizaron {cantidad_hogares} hogares.")

print('')
ruta_archivo = 'BASES_DE_DATOS/ESI2017-PERSONAS.csv'
df = coef_promediados(ruta_archivo)

numero_viajes, cantidad_hogares = promedio_hogares(df, 2017)
print('2017')
print(f"El promedio de viajes por hogar es de {numero_viajes:.2f} y se analizaron {cantidad_hogares} hogares.")

print('')
ruta_archivo = 'BASES_DE_DATOS/ESI2023-PERSONAS.csv'
df = coef_promediados(ruta_archivo)

numero_viajes, cantidad_hogares = promedio_hogares(df, 2023)
print('2023')
print(f"El promedio de viajes por hogar es de {numero_viajes:.2f} y se analizaron {cantidad_hogares} hogares.")