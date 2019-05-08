import pandas as pd

a_dict = {1: {'A': 1, 'B': 2},
          2: {'A': 1.1, 'B': 2.1}}
df = pd.DataFrame(a_dict)

print(df)
