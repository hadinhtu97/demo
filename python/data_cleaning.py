import numpy as np
import pandas as pd

# The data set contains some empty cells("Date" in row 22, and "Calories" in row 18 and 28).
# The data set contains wrong format("Date" in row 26).
# The data set contains wrong data("Duration" in row 7).
# The data set contains duplicates(row 11 and 12).
data = pd.read_csv('./data/examBadData.csv')
print(data)
print(data.info())

# cleaning null data
# drop row has na
print(data.dropna())
# fill all na with value
print(data.fillna(1))
# fill all na with value of above row
print(data.fillna(method='ffill'))
# fill all na with value of below row
print(data.fillna(method='bfill'))
print(data['Date'].fillna(method='bfill'))

# cleaning wrong format
print(data['Date'])  # Date format is object
data['Date'] = pd.to_datetime(data['Date'])
print(data['Date'])  # Date for mat is datetime64u
print(data['Date'].dropna())

# cleaning wrong data
print(data)
data.loc[7, 'Duration'] = 45
print(data)

# cleaning duplicate
print(data.duplicated())
print(data.drop_duplicates())

print(data.corr())
