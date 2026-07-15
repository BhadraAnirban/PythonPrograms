import pandas as pd
import numpy as np


file_name="auto.csv"

df = pd.read_csv(file_name, header=None) #it has no headers, so we set header=None

print("The first 5 rows of the dataframe") 
print(df.head(5))

print("The last 10 rows of the dataframe\n")
print(df.tail(10))

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

print("The first 10 rows with headers of the dataframe") 
print(df.head(10))

df1=df.replace('?',np.nan)

# This below line removes any rows where the "price" column has a NaN (missing) value.
# subset=["price"] — only check the "price" column for missing values
# axis=0 — drop rows (not columns)
# inplace=True — modify df1 directly instead of returning a new DataFrame

df1.dropna(subset=["price"], axis=0, inplace=True)
df = df1


# describe all the columns in "df" 
print("Description of all the columns in the dataframe")
print(df.describe(include = "all"))

# Get first 3 rows of columns make and price
print("First 3 rows of columns 'make' and 'price'")
print(df[["make", "price"]].head(3))


