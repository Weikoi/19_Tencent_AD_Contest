
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 10, 'display.float_format', lambda x: '%.3f' % x)
np.set_printoptions(suppress=True)


data_frame = pd.read_csv("../../data/temp2/final_train.csv")

df = data_frame[(data_frame["Commodity_id"] == -1) | (data_frame["Ad_Industry_Id"] == -1)]
print(data_frame.describe())

print(df.reindex())
