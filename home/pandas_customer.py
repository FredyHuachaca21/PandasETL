import os
import pandas as pd
import re

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo customer.sql
data_path = os.path.join(current_dir, "..", "data", "customer.sql")

# Leer el contenido del archivo
with open(data_path, 'r') as f:
    content = f.read()

# Eliminar los caracteres no deseados y separar las tuplas por comas
tuples = re.sub(r'[\(\),]', '', content).split('\n')

# Convertir las tuplas en listas
data_list = [tuple_.split() for tuple_ in tuples if tuple_]

# Crear un DataFrame de Pandas
data = pd.DataFrame(data_list, columns=['id', 'first_name', 'last_name', 'age', 'city'])

# Convertir la columna 'age' en tipo entero
data['age'] = data['age'].astype(int)

# Establecer el índice del DataFrame
data.set_index("id", inplace=True)

# Filtrar los datos
filtered_data = data[data['age'] > 40]

# Imprimir el resultado
print(filtered_data)
