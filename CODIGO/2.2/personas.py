import pandas as pd

def leer_csv(archivo, delimiter=";", encoding="latin1"):
    df = pd.read_csv(archivo, delimiter=delimiter, encoding=encoding)
    return df

archivo = leer_csv("BASES_DE_DATOS/E_P_COMUNA_2002_2035.csv")

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
        grupo_etario = las_condes[(las_condes["sexo\n1=Hombre\n2=Mujer"] == sexo) & 
                                  (las_condes[f"Poblacion {año}"].notna())]
        
        # Agrupar por edad y sumar la población
        poblacion_por_edad = grupo_etario.groupby("Edad")[f"Poblacion {año}"].sum().reset_index()
        
        # Agrupar los datos por los rangos de edad especificados
        for rango, edades in rangos.items():
            poblacion_rango = poblacion_por_edad[poblacion_por_edad["Edad"].isin(edades)][f"Poblacion {año}"].sum()
            resultado[año].at[rango, tipo] += poblacion_rango
    
    # Calcular el total de personas por rango de edad
    resultado[año]["Total"] = resultado[año]["Hombres"] + resultado[año]["Mujeres"]
    resultado[año]["Porcentaje Hombres"] = resultado[año]["Hombres"]/resultado[año]["Total"] * 100
    resultado[año]["Porcentaje Mujeres"] = resultado[año]["Mujeres"]/resultado[año]["Total"] * 100
    
    #total_hogares_2012 = 104649
    #total_hogares_2017 = 118007 por falta de información proporcionada, se supone el mismo para 2023
    
    media_2023 = 2.6
    media_2012 = 3.16
    media_2017 = 3.09
    
    if año == 2012:
        resultado[año]["Ctd hogares"] = resultado[año]["Total"].sum()/media_2012
    if año == 2017:
        resultado[año]["Ctd hogares"] = resultado[año]["Total"].sum()/media_2017
    if año == 2023:
        resultado[año]["Ctd hogares"] = resultado[año]["Total"].sum()/media_2023
    

# Mostrar los resultados
for año, data in resultado.items():
    print(f"\nPoblación en Las Condes en el año {año} por rango de edad y sexo:")
    print(data)


