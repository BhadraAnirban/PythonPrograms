
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'Salary': [50000.0, 60000.0]
})

print(df.dtypes)
print(df.info())
print(df.head(1))
print('Describe:', df.describe())