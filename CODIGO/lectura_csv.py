import pandas as pd

#Codigo con las funciones para leer el csv y crear el df final

def filtrar_por_valor(ruta_archivo, columna, valor):
    """
    Filtra los datos de un archivo CSV para incluir solo las filas donde 
    la columna especificada tenga el valor dado.

    :param ruta_archivo: Ruta al archivo CSV
    :param columna: Nombre de la columna por la cual filtrar
    :param valor: Valor que debe tener la columna para incluir la fila
    :return: DataFrame filtrado
    """
    df = pd.read_csv(ruta_archivo)
    df_filtrado = df.loc[df[columna] == valor]
    return df_filtrado

#df_filtrado en un df con todas las personas de las condes

#el ingreso lo encuentro en la columna ing_t_t
#luego tengo que considerar todas las personas que viven en la casa id_identificacion
#con eso puedo crear un nuevo df que tenga ingreso total de la casa, cantidad de personas e id_identificacion

def df_base (ruta_archivo):

    #Filtro para personas de las condes
    columna = 'r_p_c'
    valor = 13114

    df_filtrado = filtrar_por_valor(ruta_archivo, columna, valor)

    columna_id = 'id_identificacion'
    columna_ingreso = 'ing_t_t'

    """
    Agrega una columna 'ingreso_total' al DataFrame que contiene la suma de 
    todos los ingresos correspondientes a cada id_identificacion.

    :param df_filtrado: DataFrame filtrado con valores únicos de id_identificacion
    :param columna_id: Nombre de la columna de id_identificacion
    :param columna_ingreso: Nombre de la columna de ingresos
    :return: DataFrame con las columnas 'numero_de_personas' e 'ingreso_total'
    """
    # Contar las ocurrencias de cada id_identificacion
    conteo = df_filtrado[columna_id].value_counts().reset_index()
    conteo.columns = [columna_id, 'numero_de_personas']
    
    # Sumar los ingresos para cada id_identificacion
    ingreso_total = df_filtrado.groupby(columna_id)[columna_ingreso].sum().reset_index()
    ingreso_total.columns = [columna_id, 'ingreso_total']
    
    # Crear el df_final con la columna id_identificacion, numero_de_personas, y ingreso_total
    df_final = df_filtrado[[columna_id]].drop_duplicates()
    df_final = df_final.merge(conteo, on=columna_id, how='left')
    df_final = df_final.merge(ingreso_total, on=columna_id, how='left')

    # Calcular ingreso_per_capita
    df_final['ingreso_per_capita'] = df_final['ingreso_total'] / df_final['numero_de_personas']
    
    return df_final



