import os
import pandas as pd

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo customer.csv
df_exams = os.path.join(current_dir, "..", "data", "StudentsPerformance.csv")

# Leer el archivo CSV
dato = pd.read_csv(df_exams)

# Validar cantidad de filas y columnas
# print(dato.shape)

# Muestra todas las columnas
# pd.set_option('display.max_columns', 8)

# Muestra todas las filas
# pd.set_option('display.max_rows', 1000)

# Muesta las primeras 5 filas
# print(dato.head())

# Obteniendo el acceso al atributo index
# print(dato.index)

# Obteniendo el acceso al atributo index
# print(dato.columns)

# Tipo de dato de cada columna
# print(dato.dtypes)