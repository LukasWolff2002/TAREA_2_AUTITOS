import pandas as pd

def leer_csv(archivo, delimiter=";", encoding="latin1"):
    df = pd.read_csv(archivo, delimiter=delimiter, encoding=encoding)
    return df

archivo = leer_csv("BASES_DE_DATOS/E_P_COMUNA_2002_2035.csv")

las_condes = archivo[archivo["Nombre Comuna"] == "Las Condes"]

# Filtrar solo las columnas y filas de interés (2012, 2017, 2023)
años = [2012, 2017, 2023]
edades = list(range(81))  # Rango de edades de 0 a 80
resultado = {}

for año in años:
    # Crear DataFrame para almacenar los resultados de este año
    resultado[año] = pd.DataFrame(index=edades, columns=["Hombres", "Mujeres"]).fillna(0)
    
    for sexo, tipo in [(1, "Hombres"), (2, "Mujeres")]:
        # Filtrar por sexo y sumar la población por edad
        grupo_etario = las_condes[(las_condes["Sexo\n1=Hombre\n2=Mujer"] == sexo) & 
                                  (las_condes[f"Poblacion {año}"].notna())]
        
        # Agrupar por edad y sumar la población
        poblacion_por_edad = grupo_etario.groupby("Edad")[f"Poblacion {año}"].sum().reset_index()
        
        # Colocar los valores en el DataFrame resultado
        for index, row in poblacion_por_edad.iterrows():
            edad = int(row['Edad'])
            if edad in resultado[año].index:
                resultado[año].at[edad, tipo] = row[f"Poblacion {año}"]

    # Calcular el total de personas por edad
    resultado[año]["Total"] = resultado[año]["Hombres"] + resultado[año]["Mujeres"]
    
    # Calcular el porcentaje de personas de esa edad
    resultado[año]["% Hombres"] = resultado[año]["Hombres"] / resultado[año]["Total"] * 100
    resultado[año]["% Mujeres"] = resultado[año]["Mujeres"] / resultado[año]["Total"] * 100

# Mostrar los resultados
for año, data in resultado.items():
    print(f"\nPoblación en Las Condes en el año {año} por edad y sexo:")
    print(data)

prom_personas2012 = 3.16
prom_personas2017 = 3.09
prom_personas2023 = 2.6

