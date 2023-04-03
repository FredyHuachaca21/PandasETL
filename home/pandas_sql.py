import os
import pandas as pd

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo customer.csv
data_path = os.path.join(current_dir, "..", "data", "customer.csv")

# Leer el archivo CSV
dato = pd.read_csv(data_path)
dato = dato.set_index("id")

# Query
filtered_data = dato[dato['age'] > 40]
print(filtered_data)