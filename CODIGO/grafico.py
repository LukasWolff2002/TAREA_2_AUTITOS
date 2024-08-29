from coeficientes import crear_df_coeficientes
import pandas as pd
import matplotlib.pyplot as plt

# Uso de la función
ruta_archivo = 'BASES_DE_DATOS/ESI2017-PERSONAS.csv'
df = crear_df_coeficientes(ruta_archivo)

print(df)

def graficar_xe_vs_10xe(df_list, etiquetas):
    """
    Crea gráficos donde cada punto tiene las coordenadas (Xi, Yi) para múltiples DataFrames.

    :param df_list: Lista de DataFrames que contienen las columnas 'Xi', 'Xp', 'Xe', 'Xt', y 'Xj'
    :param etiquetas: Lista de etiquetas para cada DataFrame, usadas en la leyenda
    """
    plt.figure(figsize=(8, 6))
    
    for df, etiqueta in zip(df_list, etiquetas):
        x = df['Xi']
        y = -2.1723 + 0.3792 * df['Xi'] + 0.6221 * df['Xp'] + 1.0065 * df['Xe'] + 0.4302 * df['Xt'] + 0.1614 * df['Xj']
        plt.plot(x, y, marker='o', linestyle='-', alpha=0.6, label=etiqueta)
    
    plt.title('Gráfico de Xi vs Yi con líneas')
    plt.xlabel('Xi')
    plt.ylabel('Yi')
    plt.grid(True)
    plt.legend()
    plt.show()

# Ejemplo de uso
# Suponiendo que df1, df2, y df3 son los DataFrames que ya tienes:
# df1 = df_base(ruta_archivo1)
# df2 = df_base(ruta_archivo2)
# df3 = df_base(ruta_archivo3)

# Para este ejemplo, simplemente utilizaré df_resultado como si fueran 3 DataFrames diferentes.
df1 = df.copy()
df2 = df.copy()
df3 = df.copy()

# Etiquetas para las leyendas
etiquetas = ['Dataset 1', 'Dataset 2', 'Dataset 3']

# Graficar
graficar_xe_vs_10xe([df1, df2, df3], etiquetas)
