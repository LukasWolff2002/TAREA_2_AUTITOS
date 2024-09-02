import pandas as pd

df = pd.read_csv('BASES_DE_DATOS/ESI2017-PERSONAS.csv') #se cambia archivo

# Filtrar por la comuna de Las Condes (id = 13114)
las_condes_df = df[df['r_p_c'] == 13114]

# Agrupar por 'id_identificacion' y contar el número de personas por hogar
personas_por_hogar = las_condes_df.groupby('id_identificacion').size()

# Calcular el promedio de personas por hogar
promedio_personas_por_hogar = personas_por_hogar.mean()

print(f"El promedio de personas por hogar en Las Condes es: {promedio_personas_por_hogar:.2f}")
