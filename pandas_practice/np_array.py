import pandas as pd
import numpy as np

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                    columns=['c', 'b', 'a'])
print(df2)