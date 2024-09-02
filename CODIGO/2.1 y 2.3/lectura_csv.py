import pandas as pd

#Codigo con las funciones para leer el csv y crear el df final

def filtrar_por_valor(ruta_archivo, columna, valor):

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

    # Calcular la columna Xp, que suma la cantidad de id_identificacion donde 'edad' <= 5 años
    df_filtrado_menor_5 = df_filtrado[df_filtrado['edad'] <= 5]
    xp_conteo = df_filtrado_menor_5[columna_id].value_counts().reset_index()
    xp_conteo.columns = [columna_id, 'Xp']
    df_final = df_final.merge(xp_conteo, on=columna_id, how='left')
    df_final['Xp'] = df_final['Xp'].fillna(0)

    # Calcular la columna Xe, que suma la cantidad de id_identificacion donde 'edad' está entre 6 y 22 años
    df_filtrado_6_22 = df_filtrado[(df_filtrado['edad'] >= 6) & (df_filtrado['edad'] <= 22)]
    xe_conteo = df_filtrado_6_22[columna_id].value_counts().reset_index()
    xe_conteo.columns = [columna_id, 'Xe']
    df_final = df_final.merge(xe_conteo, on=columna_id, how='left')
    df_final['Xe'] = df_final['Xe'].fillna(0)

    # Calcular la columna Xt, que suma la cantidad de id_identificacion donde 'edad' está entre 23 y 62 años
    df_filtrado_23_62 = df_filtrado[(df_filtrado['edad'] >= 23) & (df_filtrado['edad'] <= 62)]
    xt_conteo = df_filtrado_23_62[columna_id].value_counts().reset_index()
    xt_conteo.columns = [columna_id, 'Xt']
    df_final = df_final.merge(xt_conteo, on=columna_id, how='left')
    df_final['Xt'] = df_final['Xt'].fillna(0)

    # Calcular la columna Xv, que suma la cantidad de id_identificacion donde 'edad' está entre 63 y 79 años
    df_filtrado_63_79 = df_filtrado[(df_filtrado['edad'] >= 63)&(df_filtrado['edad'] <= 79)]
    xj_conteo = df_filtrado_63_79[columna_id].value_counts().reset_index()
    xj_conteo.columns = [columna_id, 'Xj']
    df_final = df_final.merge(xj_conteo, on=columna_id, how='left')
    df_final['Xj'] = df_final['Xj'].fillna(0)

    return df_final



