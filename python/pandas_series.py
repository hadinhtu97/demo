import pandas as pd
import numpy as np

a = pd.Series([1, 2, 3, 4, 5, 6])
print(a)
print(type(a))
a.name = 'pandas series test'
print(a)
print(a.dtype)
print(a.values)
print(a[0])
print(a[5])
print(a.index)
a.index = [
    'index_1',
    'index_2',
    'index_3',
    'index_4',
    'index_5',
    'index_6'
]
print(a)
print(a.index)
print(a[0])
print(a['index_1'])

# or sort:
b = pd.Series({
    'index_1': 1,
    'index_2': 2,
    'index_3': 3,
    'index_4': 4,
    'index_5': 5,
    'index_6': 6,
}, name='Test pandas series')
print(b)

c = pd.Series(
    [1, 2, 3, 4, 5, 6],
    index=['index_1', 'index_2', 'index_3', 'index_4', 'index_5', 'index_6'],
    name='Test pandas series'
)
print(c)

print(c[1])
print(c[-1])
print(c.iloc[1])
print(c[['index_2', 'index_5']])
print(c[[0, 1]])

print(c.sum())
print(c.std())
print(c.mean())
print(c.min())
print(c.max())

print(c * 1000000)
print(c > 3)
print(c[c > 3])
print(c[(c < 3) | (c > 5)])
print(c[(c > 2) & (c < 4)])


c['index_1'] = 23
print(c)
c.iloc[-2] = 14
print(c)
c[c < 6] = 10
print(c)