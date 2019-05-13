import pandas as pd
import pickle as pk
from util.global_constant import RAW_DATA_PATH, RAW_DF_PATH


pd.set_option('display.max_columns', 30)

file = open(RAW_DATA_PATH + "user_data")

# lines_num 为 1396718
# count = 0
# for index, line in enumerate(file):
#     count += 1
# print(count)

# 十万条一个batch

user_id = []
age = []
area = []
gender = []
status = []
education = []
consumption_ability = []
device = []
work = []
ConnectionType = []
behavior = []

for idx in range(100000):
    line_raw = file.readline()
    line = line_raw.split()
    user_id.append(eval(line[0]))
    age.append(eval(line[1]))
    gender.append(eval(line[2]))
    area.append(eval(line[3]))
    status.append(eval(line[4]))
    education.append(eval(line[5]))
    consumption_ability.append(eval(line[6]))
    device.append(eval(line[7]))
    work.append(eval(line[8]))
    ConnectionType.append(eval(line[9]))
    behavior.append(eval(line[10]))
    if idx % 100 == 0:
        print("\r当前进度: {:.2f}%".format((idx+1) * 100 / 100000), end="")

data_dict = {
    "user_id": user_id,
    "age": age,
    "gender": gender,
    "area": area,
    "status": status,
    "education": education,
    "consumption_ability": consumption_ability,
    "device": device,
    "work": work,
    "ConnectionType": ConnectionType,
    "behavior": behavior,
}

df = pd.DataFrame(data_dict)

# print(df)

pk.dump(df, file=open(RAW_DF_PATH + "user.pkl", 'wb'))
