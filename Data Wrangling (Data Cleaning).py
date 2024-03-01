import pandas as pd
import numpy as np

'''
    a) Check with the data collection source
    (b) Drop the missing values
      -  Drop the variable / the data entry
    (c) Replace the missing values
     - replace it with an average(of similar datapoints
    - replace it by frequency
    - replace it based on other function
    (d) leave it as missing data
'''
# Dataframe.dropna()

df = pd.read_csv('automobile.csv')
print(df.describe())
print(df.info)

# Dealing with missing data by dropping it
df.dropna(subset=["price"], axis=0, inplace=True)
# axis=0 drops the entire row, axis=1 drops the entire column
# If you want to change the original DataFrame, use the inplace = True argument:
df = df.dropna(subset=["price"], axis=0)

# replace missing value
# dataframe.replace(missing_value, new_value)
mean = df["normalized-loses"].mean()
df["normalized-loses"].replace(np.nan, mean)

# Data Formatting
# (Converting 'mpg' to 'L/100km' in car dataset
df["city-mpg"]= 235/df["city-mpg"]
df.rename(columns=("city-mpg:city-L/1ookm"), inplace=True)
# incorrect data types
# dtype - to identify
# astype - to convert
df["price"] = df["price"].astype(int)

