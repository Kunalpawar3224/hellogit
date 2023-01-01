import pandas as pd

d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[1, 3])}

df= pd.DataFrame(data=d, index=[0, 1, 2, 3])

print(df)