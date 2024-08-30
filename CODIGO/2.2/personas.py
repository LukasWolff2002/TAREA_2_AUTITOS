import pandas as pd

def leer_csv(archivo, delimiter = ";", encoding="latin1"):
    df = pd.read_csv(archivo, delimiter=delimiter, encoding=encoding)
    return df

archivo = leer_csv("BASES_DE_DATOS/E_P_COMUNA_2002_2035.csv")

las_condes = archivo[archivo["Nombre Comuna"] == "Las Condes"]

# Filtrar solo las columnas y filas de interés (2012, 2017, 2023)
años = [2012, 2017, 2023]
resultado = {}

for año in años:
    # Sumar la población para hombres
    hombres = las_condes[(las_condes[f"Poblacion {año}"].notna()) & (las_condes["Sexo\n1=Hombre\n2=Mujer"] == 1)][f"Poblacion {año}"].sum()
    
    # Sumar la población para mujeres
    mujeres = las_condes[(las_condes[f"Poblacion {año}"].notna()) & (las_condes["Sexo\n1=Hombre\n2=Mujer"] == 2)][f"Poblacion {año}"].sum()
    
    # Guardar los resultados en el diccionario
    resultado[año] = {"Hombres": hombres, "Mujeres": mujeres}

# Mostrar los resultados
for año, valores in resultado.items():
    print(f"Año: {año}")
    print(f"Hombres: {valores['Hombres']}, Mujeres: {valores['Mujeres']}\n")



