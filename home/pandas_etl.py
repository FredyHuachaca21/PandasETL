import pandas as pd
import pandasql as ps

dato = pd.read_csv("../data/customer.csv")
dato = dato.set_index("id")

print(dato)