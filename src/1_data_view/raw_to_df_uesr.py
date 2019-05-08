import pandas as pd
import pickle as pk
from util.global_constant import RAW_DATA_PATH, RAW_DF_PATH

file = open(RAW_DATA_PATH + "user_data")

lines = file.readlines()
length = len(lines)

user_id = []
age = []
area = []
status = []
education = []
consumption_ability = []
device = []
work = []
ConnectionType = []
behavior = []

for idx, line_raw in enumerate(lines):
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
        print("\r当前进度: {:.2f}%".format(idx * 100 / length), end="")

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

pk.dump(df, file=open(RAW_DF_PATH + "exp.pkl", 'wb'))
