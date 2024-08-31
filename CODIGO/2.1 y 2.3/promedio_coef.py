from coeficientes import coef_promediados
import pandas as pd

# Uso de la función
ruta_archivo = 'BASES_DE_DATOS/ESI2012-PERSONAS.csv'
df = coef_promediados(ruta_archivo)

print('2012')
print(f'Xi = {df["Xi"]}')
print(f'Xp = {df["Xp"]}')
print(f'Xe = {df["Xe"]}')
print(f'Xt = {df["Xt"]}')
print(f'Xj = {df["Xj"]}')
print(f'numero_hogares = {df["numero_hogares"]}')

ruta_archivo = 'BASES_DE_DATOS/ESI2017-PERSONAS.csv'
df = coef_promediados(ruta_archivo)
print('')
print('2017')
print(f'Xi = {df["Xi"]}')
print(f'Xp = {df["Xp"]}')
print(f'Xe = {df["Xe"]}')
print(f'Xt = {df["Xt"]}')
print(f'Xj = {df["Xj"]}')
print(f'numero_hogares = {df["numero_hogares"]}')

print('')
ruta_archivo = 'BASES_DE_DATOS/ESI2023-PERSONAS.csv'
df = coef_promediados(ruta_archivo)

print('2023')
print(f'Xi = {df["Xi"]}')
print(f'Xp = {df["Xp"]}')
print(f'Xe = {df["Xe"]}')
print(f'Xt = {df["Xt"]}')
print(f'Xj = {df["Xj"]}')
print(f'numero_hogares = {df["numero_hogares"]}')
