import pandas as pd

data = pd.read_csv("submission.csv")

for idx, i in enumerate(data.iloc[:, 1]):
    data.iloc[idx, 1] = round(i, 4)
#
# print(data)
data.to_csv("submission2.csv", index=False)
print(data)
