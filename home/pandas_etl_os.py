import os
import pandas as pd
import pandasql as ps

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo customer.csv
data_path = os.path.join(current_dir, "..", "data", "customer.csv")

# Leer el archivo CSV
dato = pd.read_csv(data_path)
dato = dato.set_index("id")

#Query
sql_query = "SELECT * FROM dato WHERE age > 30"
print(ps.sqldf(sql_query, {"dato": dato}))
