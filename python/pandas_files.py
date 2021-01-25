import pandas as pd

data = pd.read_csv('./data/examCSV.csv')
print(data)
print(type(data))
print(data.info())
print(data.describe())
print(data.head())
print(data.tail())
print(data.dtypes)

data.columns = ['date', 'timestamp', 'value']
print(data.dtypes)
data['date'] = pd.to_datetime(data['date'])
print(data.dtypes)
print(data.plot())
