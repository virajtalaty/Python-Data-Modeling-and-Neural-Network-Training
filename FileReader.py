import pandas as pd

data = pd.read_table('data.sas', usecols=[14, 2, 5])

print(data)

