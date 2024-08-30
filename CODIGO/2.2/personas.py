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
    # Filtrar hombres y mujeres por cada rango de edad
    for sexo, tipo in [(1, "Hombres"), (2, "Mujeres")]:
        grupo_etario = las_condes[(las_condes["Sexo\n1=Hombre\n2=Mujer"] == sexo) & 
                                  (las_condes[f"Poblacion {año}"].notna())]
        
        # Agrupar por edad y sumar la población para cada grupo
        poblacion_por_edad = grupo_etario.groupby("Edad")[f"Poblacion {año}"].sum().reset_index()
        
        # Guardar los resultados en el diccionario
        if año not in resultado:
            resultado[año] = {}
        
        resultado[año][tipo] = poblacion_por_edad

# Mostrar los resultados
for año, valores in resultado.items():
    print(f"Año: {año}")
    for tipo, data in valores.items():
        print(f"{tipo}:")
        print(data)
        print("\n")
        


