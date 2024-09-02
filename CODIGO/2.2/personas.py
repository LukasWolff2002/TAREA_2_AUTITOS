import pandas as pd

def leer_csv(archivo, delimiter=";", encoding="latin1"):
    df = pd.read_csv(archivo, delimiter=delimiter, encoding=encoding)
    return df

archivo = leer_csv("BASES_DE_DATOS/E_P_COMUNA_2002_2035.csv")

# Renombrar la columna para facilitar el trabajo
archivo.rename(columns={'Sexo\n1=Hombre\n2=Mujer': 'Sexo'}, inplace=True)

las_condes = archivo[archivo["Nombre Comuna"] == "Las Condes"]

# Filtrar solo las columnas y filas de interés (2012, 2017, 2023)
años = [2012, 2017, 2023]
rangos = {
    "0-5": range(0, 6),
    "6-22": range(6, 23),
    "23-62": range(23, 63),
    "63-80": range(63, 81)
}
resultado = {}

for año in años:
    # Crear DataFrame para almacenar los resultados agrupados por rango de edad
    resultado[año] = pd.DataFrame(index=rangos.keys(), columns=["Hombre", "Mujer", "Total"]).fillna(0)
    
    for sexo, tipo in [(1, "Hombre"), (2, "Mujer")]:
        # Filtrar por sexo y sumar la población por edad
        grupo_etario = las_condes[(las_condes["Sexo"] == sexo) & 
                                  (las_condes[f"Poblacion {año}"].notna())]
        
        # Agrupar por edad y sumar la población
        poblacion_por_edad = grupo_etario.groupby("Edad")[f"Poblacion {año}"].sum().reset_index()
        
        # Agrupar los datos por los rangos de edad especificados
        for rango, edades in rangos.items():
            poblacion_rango = poblacion_por_edad[poblacion_por_edad["Edad"].isin(edades)][f"Poblacion {año}"].sum()
            resultado[año].at[rango, tipo] += poblacion_rango
    
    # Calcular el total de personas por rango de edad
    resultado[año]["Total"] = resultado[año]["Hombre"] + resultado[año]["Mujer"]
    resultado[año]["Porcentaje Hombre"] = resultado[año]["Hombre"] / resultado[año]["Total"] * 100
    resultado[año]["Porcentaje Mujer"] = resultado[año]["Mujer"] / resultado[año]["Total"] * 100
    
    # Definir la media para cada año
    if año == 2012:
        media_año = 3.16
    elif año == 2017:
        media_año = 3.09
    elif año == 2023:
        media_año = 2.6
    
    # Calcular el total de personas
    total_personas = resultado[año]["Total"].sum()
    
    # Calcular el número total de hogares
    total_hogares = total_personas / media_año
    
    # Reemplazar la columna "Ctd hogares" con este único valor
    resultado[año]["Ctd hogares"] = total_hogares  

# Mostrar los resultados
for año, data in resultado.items():
    print(f"\nPoblación en Las Condes en el año {año} por rango de edad y sexo:")
    print(data)
