import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name="usedcars.csv"

df = pd.read_csv(file_name, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(file_name, names = headers)

# To see what the data set looks like, we'll use the head() method.
print(df.head())

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)

print("DataOperation Result: ")
for column in df.columns:
    print(column)
    print(df[column].value_counts())
    print("")

print("Missing Data Result: ")

missing_data = df.isnull() #it converts all data either to True or False. True if the data is missing, False if it is not missing.
# .notnull() is the opposite of .isnull() and returns True for non-missing values and False for missing values.
print(missing_data.head(5))

for column in missing_data.columns.values.tolist():
    print("Columne Name: ",column)
    print (missing_data[column].value_counts())
    print("")  




avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg_norm_loss)

print("Data Result After Replacing NaN with Average: ", df.head())


print("Data Types of 'bore' and 'stroke':")
print(df[["bore", "stroke"]].dtypes)

# Convert data types to proper format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")



print("Column Data Types after converting:")
# print(df.dtypes)
for col, dtype in df.dtypes.items():
    print(f"Column Name: {col}, Data Type: {dtype}")

# Data Standardization

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]


df['highway-mpg'] = 235/df["highway-mpg"]
df.rename(columns = {'highway-mpg': 'highway-L/100km'}, inplace=True)

print("Data Result After Column change: ", df.head())

for col, dtype in df.dtypes.items():
    print(f"Column Name: {col}, Data Type: {dtype}")

print("Data Result before Column value normalization change: ", df[['length','width']].head(10))
# replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()

print("Data Result After Column value normalization change: ", df[['length','width']].head(10))

# Binning Data (group data into bins) In Pandas
df[["horsepower"]] = df[["horsepower"]].astype(float)
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
# 4 — produces 4 equally spaced points, which creates 3 bins (Low, Medium, High)

group_names = ['Low', 'Medium', 'High']
# Apply the function "cut" to determine what each value of df['horsepower'] belongs to.
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
print("Data Result After Binning 'horsepower': ", df[['horsepower', 'horsepower-binned']].head(10))
print("Value Counts of 'horsepower-binned': ", df["horsepower-binned"].value_counts())

# Plotting the binned data (Visualize the distribution of horsepower)
plt.figure(figsize=(10,6))
df['horsepower-binned'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Horsepower Bins')
plt.ylabel('Frequency')
plt.title('Horsepower Distribution')
plt.show()