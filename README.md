# Explicacion Codigo Bases de Datos

El analisis esta en el siguiente [INFORME](INFOMRE/informe.pdf)

## Lectura y Filtrado de Datos

[lectura_csv.py](CODIGO/2.1%20y%202.3/lectura_csv.py)

En primer lugar se lee la base de datos

```python
def filtrar_por_valor(ruta_archivo, columna, valor):

    df = pd.read_csv(ruta_archivo)
    df_filtrado = df.loc[df[columna] == valor]
    return df_filtrado
```

Luego se filtra segun comuna (comuna = 'r_p_c') y el valor debe ser 13114. En base a esto, se generan los distintos coeficientes:

```python
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
```

## Calculo Xi y Data Frame Coeficientes Finales

Para obtener el dataframe final, se utiliza el siguiente codigo:

[coeficientes.py](CODIGO/2.1%20y%202.3/coeficientes.py)

Donde:

```python
def crear_df_coeficientes(ruta_archivo):

    df_final = df_base(ruta_archivo)

    # Filtrar los registros donde ingreso_per_capita es mayor que 0
    df_filtrado = df_final[df_final['ingreso_per_capita'] > 0]
    
    # Calcular el logaritmo base 10 del ingreso per capita
    df_coeficientes = pd.DataFrame()

    print(f'el ingrweso per capita promedio es {df_filtrado["ingreso_per_capita"].mean()}')
    df_coeficientes['Xi'] = np.log10(df_filtrado['ingreso_per_capita'])

    # Agrego los coeficientes restantes
    df_coeficientes['Xp'] = df_filtrado['Xp']
    df_coeficientes['Xe'] = df_filtrado['Xe']
    df_coeficientes['Xt'] = df_filtrado['Xt']
    df_coeficientes['Xj'] = df_filtrado['Xj']

    return df_coeficientes
```

Finalmente promedio los coeficientes:

```python
def coef_promediados (ruta_archivo):
    df_coeficientes = crear_df_coeficientes(ruta_archivo)
    numero_hogares = len(df_coeficientes)
    df_coeficientes_promediados = df_coeficientes.mean()
    df_coeficientes_promediados['numero_hogares'] = numero_hogares

    return df_coeficientes_promediados
```

## Ajuste por Inflacion

Para ajustar Xi por inflacion, se utiliza la siguiente funcio ([calibracion_modelo.py](CODIGO/2.1%20y%202.3/calibracion_modelo.py)):

```python
def promedio_hogares(df, año):
    if año == 2012:
        ponderacion = 1
    elif año == 2017:
        ponderacion = 1.182
    elif año == 2023:
        ponderacion = 1.615

    xi = df['Xi']
    xi = 10**xi
    xi = xi / ponderacion
    xi = np.log10(xi)
```
## Aplicacion Regrecion Lineal

Luego, con los coeficientes promediados, se aplica la regrecion lineal:\

```python
y = -2.1723 + 0.3792 * df['Xi'] + 0.6221 * df['Xp'] + 1.0065 * df['Xe'] + 0.4302 * df['Xt'] + 0.1614 * df['Xj']
```




