import pandas as pd
import numpy as np
import pickle as pk
import time
from util.global_constant import RAW_DATA_PATH, RAW_DF_PATH

pd.set_option('display.max_columns', 30)

file = open(RAW_DATA_PATH + "ad_static_feature.out")
lines = file.readlines()

ad_id = []
create_time = []
account_id = []
product_id = []
product_type = []
industry_id = []
size = []

count5 = 0
count6 = 0

for idx, line_raw in enumerate(lines):
    line = line_raw.split()
    if len(line) == 7:
        ad_id.append(eval(line[0]))
        create_time.append(eval(line[1]))
        account_id.append(eval(line[2]))
        product_id.append(eval(line[3]))
        product_type.append(eval(line[4]))
        industry_id.append(eval(line[5]))
        size.append(eval(line[6]))

    if len(line) == 6:
        ad_id.append(eval(line[0]))
        create_time.append(eval(line[1]))
        account_id.append(eval(line[2]))
        product_id.append(None)
        product_type.append(eval(line[3]))
        industry_id.append(eval(line[4]))
        size.append(eval(line[5]))

    # if idx % 100 == 0:
    #     print("\r当前进度: {:.2f}%".format(idx * 100 / length), end="")


data_dict = {
    "ad_id": ad_id,
    "create_time": create_time,
    "account_id": account_id,
    "product_id": product_id,
    "product_type": product_type,
    "industry_id": industry_id,
    "size": size,
}

df = pd.DataFrame(data_dict)

print(df)

pk.dump(df, file=open(RAW_DF_PATH + "static.pkl", 'wb'))
