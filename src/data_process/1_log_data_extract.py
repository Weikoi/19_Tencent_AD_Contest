"""
log exp只抽取最后一天数据

drop 掉无用维度
"""
# @Time    : 2019/5/15
# @Author  : Weikoi
# @Email   : 17210240112@fudan.edu.cn
# @File    : 1_log_data_extract.py

import pandas as pd
import datetime
import time
import pickle as pk

load_all_method = True
from util.global_constant import RAW_DF_PATH

Total_Exposure_Log_Data_319 = []

# 定义曝光日志中的相关列
Exposure_Log_Data_columns = ['Ad_Request_id', 'Ad_Request_Time', 'Ad_pos_id', 'user_id', 'ad_id', 'Ad_material_size',
                             'Ad_bid', 'Ad_pctr', 'Ad_quality_ecpm', 'Ad_total_Ecpm']

# 为数据集增加列名称
# Total_Exposure_Log_Data.append(Exposure_Log_Data_columns)
op_id_set = pk.load(open("../../data/temp/" + "operation_id_set.pkl", "rb"))
static_id_set = pk.load(open("../../data/temp/" + "static_id_set.pkl", "rb"))

with open('../../data/raw/totalExposureLog.out', 'r') as f:
    num = 0
    for i, line in enumerate(f):

        line = line.strip().split('\t')

        if (i % 5000000) == 0:
            print("======= exp log 数据已经执行了", i, "条=======")

        # 如果数据集中有缺失的数据 直接跳过该条数据
        if line[0] == '0' or line[1] == '0' or line[2] == '0' or line[3] == '0' or line[4] == '0' or line[5] == '0' \
                or line[6] == '0' or line[7] == '0' or line[8] == '0' or line[9] == '0':
            # print("该条数据创建时间混乱", i, ':', line)
            continue

        # 判断广告位数据集中是否存在多值情况
        if ',' in line[2]:
            # print("该条数据中广告位存在多值情况：", line)
            continue

        if '.' in line[0]:
            # print("该条数据中广告请求ID的数据为小数：", line)
            continue

        if '.' in line[3]:
            # print("该条数据中广告请求ID的数据为小数：", line)
            continue

        if '.' in line[4]:
            print("该条数据中广告请求ID的数据为小数：", line)
            continue

        # 判断该条数据的ID信息是否在静态广告之中 存在的话就跳过该条记录
        # 注意大部分广告曝光数据集中的广告ID都不在广告操作日志之中
        tmp_ad_id = int(line[4])

        if tmp_ad_id not in op_id_set:
            # print("*********操作数据集中不存在该条记录**********", line)
            continue

        if tmp_ad_id not in static_id_set:
            # print("*********静态数据集中不存在该条记录**********", line)
            continue

        # 数据集对应的存储格式是： 2018/10/18 10:41:18
        loacl_time = int(line[1])
        time_local = time.localtime(loacl_time)
        line[1] = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        # print(line[1], type(line[1]))  该类型是str

        # 定义用于比较时间范围的数据
        tmp_line = datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")
        cmp_time_29 = datetime.datetime.strptime("2019-02-28 23:59:59", "%Y-%m-%d %H:%M:%S")
        cmp_time_31 = datetime.datetime.strptime("2019-03-01", "%Y-%m-%d")

        # 如果时间不在合法的范围之内的话 就直接删除该条记录 并给与提示
        if cmp_time_29 <= tmp_line < cmp_time_31:
            # print("*******该条记录不合法需要重新删除*********", line)
            continue
        else:
            # 定义的是16数据集

            cmp_time_319 = datetime.datetime.strptime("2019-03-19", "%Y-%m-%d")
            cmp_time_319_night = datetime.datetime.strptime("2019-03-19 23:59:59", "%Y-%m-%d %H:%M:%S")

            if cmp_time_319 <= tmp_line <= cmp_time_319_night:
                Total_Exposure_Log_Data_319.append(line)
            # else:
            #     print("该条记录不在规定的时间范围之内", line)


# 保存广告记录是3月19号的数据
Exposure_data_319 = pd.DataFrame(Total_Exposure_Log_Data_319)


Exposure_data_319.to_csv('../../data/temp2/Total_Exposure_Log_Data.csv', index=False, header=Exposure_Log_Data_columns)

Exposure_data = pd.read_csv('../../data/temp2/Total_Exposure_Log_Data.csv')
Exposure_data.drop('Ad_Request_Time', axis=1, inplace=True)
Exposure_data.drop('Ad_pos_id', axis=1, inplace=True)
Exposure_data.drop('Ad_pctr', axis=1, inplace=True)
Exposure_data.drop('Ad_quality_ecpm', axis=1, inplace=True)
Exposure_data.drop('Ad_total_Ecpm', axis=1, inplace=True)
Exposure_data.to_csv('../../data/temp2/Total_Exposure_Log_Data_drop.csv', index=False)
