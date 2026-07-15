import pandas as pd
import numpy as np


file_name="laptops.csv"

df = pd.read_csv(file_name, header=None)
print("The first 5 rows of the dataframe")
print(df.head(5))

headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
df.columns = headers

print(df.columns)

df.replace('?',np.nan, inplace = True)

print(df.describe(include='all'))

print("Information about the dataframe")
print(df.info())