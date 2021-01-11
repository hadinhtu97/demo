# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.

import pandas as pd

print(pd.__version__)
mydata = {
    'cars': ['BWM', 'Volvo', 'Ford'],
    'passing': [3, 7, 2]
}
x = pd.DataFrame(mydata)
print(x)
