import pandas as pd

data = {
    'value_1': [
        1, 2, 3, 4, 5
    ],
    'value_2': [
        1.1, 2.2, 3.3, 4.4, 5.5
    ],
    'value_3': [
        '1', '2', '3', '4', '5'
    ]
}
df = pd.DataFrame(data)
df.index = ['row_1', 'row_2', 'row_3', 'row_4', 'row_5']
print(df)
print(type(df))
print(df.columns)
print(df.index)
print(df.info())
print(df.size)
print(df.shape)
print(df.describe())
print(df.dtypes)

print(df)
print(df['value_1'])
print(df.loc['row_1'])
print(df.iloc[0])
print(df.iloc[0][0])
print(df.loc['row_1':'row_4'])
print(df.loc['row_1':'row_3', 'value_2'])
print(df.loc['row_3':'row_5', ['value_2', 'value_3']])

print(df['value_1'] > 3)
print(df[df['value_1'] > 3])
print(df.loc[df['value_1'] > 3, ['value_2', 'value_3']])

print(df.drop('row_1'))
print(df.drop(['row_1', 'row_3']))
print(df.drop(columns='value_1'))
print(df.drop(columns=['value_1', 'value_3']))
print(df.drop(['value_1', 'value_2'], axis=1))
s = pd.Series([1, 2], index=['value_1', 'value_2'])
print(df+s)

df['value_4'] = 1
print(df)
df = df.rename(columns={
    'value_1': 'Value_1'
}, index={
    'row_2': 'Row_2'
})
print(df)
df['value_5'] = df['value_1'] / df['value_2']
print(df)
