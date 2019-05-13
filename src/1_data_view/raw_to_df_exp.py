import pandas as pd
import pickle as pk
from util.global_constant import RAW_DATA_PATH, RAW_DF_PATH

pd.set_option('display.max_columns', 20)

file = open(RAW_DATA_PATH + "totalExposureLog.out")


# lines_num 为 102386695
# count = 0
# for index, line in enumerate(file):
#     count += 1
# print(count)

# 一百万条一个batch

ad_request_id = []
ad_request_time = []
ad_location_id = []
user_id = []
exp_ad_id = []
exp_ad_size = []
bid = []
pctr = []
quality_ecpm = []
totalEcpm = []

for idx in range(1000000):
    line_raw = file.readline()
    line = line_raw.split()
    ad_request_id.append(eval(line[0]))
    ad_request_time.append(eval(line[1]))
    ad_location_id.append(eval(line[2]))
    user_id.append(eval(line[3]))
    exp_ad_id.append(eval(line[4]))
    exp_ad_size.append(eval(line[5]))
    bid.append(eval(line[6]))
    pctr.append(eval(line[7]))
    quality_ecpm.append(eval(line[8]))
    totalEcpm.append(eval(line[9]))
    if idx % 100 == 0:
        print("\r当前进度: {:.2f}%".format((idx+1) * 100 / 1000000), end="")

data_dict = {
    "ad_request_id": ad_request_id,
    "ad_request_time": ad_request_time,
    "ad_location_id": ad_location_id,
    "user_id": user_id,
    "exp_ad_id": exp_ad_id,
    "exp_ad_size": exp_ad_size,
    "bid": bid,
    "pctr": pctr,
    "quality_ecpm": quality_ecpm,
    "totalEcpm": totalEcpm,
}

df = pd.DataFrame(data_dict)
print(df)
#
pk.dump(df, file=open(RAW_DF_PATH+"exp.pkl", 'wb'))
