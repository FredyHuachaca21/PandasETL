import pandas as pd
dato = pd.read_csv("../data/customer.csv")
dato = dato.set_index("id")

print(dato)