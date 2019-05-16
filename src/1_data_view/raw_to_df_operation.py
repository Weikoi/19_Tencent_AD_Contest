import pandas as pd
import numpy as np
import pickle as pk
import time
from util.global_constant import RAW_DATA_PATH, RAW_DF_PATH, TEMP_DATA_PATH

pd.set_option('display.max_columns', 30)

file = open(RAW_DATA_PATH + "ad_operation.out")
lines = file.readlines()

ad_id = []
create_time = []
operation_type = []
modify_field = []
ad_status = []


count5 = 0
count6 = 0

for idx, line_raw in enumerate(lines):
    line = line_raw.split()
    ad_id.append(eval(line[0]))
    create_time.append(eval(line[1]))
    operation_type.append(eval(line[2]))
    modify_field.append(eval(line[3]))
    # ad_status.append(eval(line[4]))



    # if idx % 100 == 0:
    #     print("\r当前进度: {:.2f}%".format(idx * 100 / length), end="")


# data_dict = {
#     "ad_id": ad_id,
#     "create_time": create_time,
#     "account_id": account_id,
#     "product_id": product_id,
#     "product_type": product_type,
#     "industry_id": industry_id,
#     "size": size,
# }

# df = pd.DataFrame(data_dict)
#
# print(df)

operation_id_set = set(ad_id)

print(operation_id_set)

pk.dump(operation_id_set, file=open(TEMP_DATA_PATH + "operation_id_set.pkl", 'wb'))
