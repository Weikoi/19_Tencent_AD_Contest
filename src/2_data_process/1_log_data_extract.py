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
import sys

sys.path.append("../../")
sys.path.append("../")

load_all_method = True
from util.global_constant import RAW_DF_PATH

Total_Exposure_Log_Data_16 = []
Total_Exposure_Log_Data_17 = []
Total_Exposure_Log_Data_18 = []
Total_Exposure_Log_Data_19 = []
Total_Exposure_Log_Data_20 = []
Total_Exposure_Log_Data_21 = []
Total_Exposure_Log_Data_22 = []
Total_Exposure_Log_Data_23 = []
Total_Exposure_Log_Data_24 = []
Total_Exposure_Log_Data_25 = []
Total_Exposure_Log_Data_26 = []
Total_Exposure_Log_Data_27 = []
Total_Exposure_Log_Data_28 = []
Total_Exposure_Log_Data_301 = []
Total_Exposure_Log_Data_302 = []
Total_Exposure_Log_Data_303 = []
Total_Exposure_Log_Data_304 = []
Total_Exposure_Log_Data_305 = []
Total_Exposure_Log_Data_306 = []
Total_Exposure_Log_Data_307 = []
Total_Exposure_Log_Data_308 = []
Total_Exposure_Log_Data_309 = []
Total_Exposure_Log_Data_310 = []
Total_Exposure_Log_Data_311 = []
Total_Exposure_Log_Data_312 = []
Total_Exposure_Log_Data_313 = []
Total_Exposure_Log_Data_314 = []
Total_Exposure_Log_Data_315 = []
Total_Exposure_Log_Data_316 = []
Total_Exposure_Log_Data_317 = []
Total_Exposure_Log_Data_318 = []
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
            # 定义的是16数据集
            cmp_time_16 = datetime.datetime.strptime("2019-02-16", "%Y-%m-%d")
            cmp_time_16_night = datetime.datetime.strptime("2019-02-16 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_17 = datetime.datetime.strptime("2019-02-17", "%Y-%m-%d")
            cmp_time_17_night = datetime.datetime.strptime("2019-02-17 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_18 = datetime.datetime.strptime("2019-02-18", "%Y-%m-%d")
            cmp_time_18_night = datetime.datetime.strptime("2019-02-18 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_19 = datetime.datetime.strptime("2019-02-19", "%Y-%m-%d")
            cmp_time_19_night = datetime.datetime.strptime("2019-02-19 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_20 = datetime.datetime.strptime("2019-02-20", "%Y-%m-%d")
            cmp_time_20_night = datetime.datetime.strptime("2019-02-20 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_21 = datetime.datetime.strptime("2019-02-21", "%Y-%m-%d")
            cmp_time_21_night = datetime.datetime.strptime("2019-02-21 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_22 = datetime.datetime.strptime("2019-02-22", "%Y-%m-%d")
            cmp_time_22_night = datetime.datetime.strptime("2019-02-22 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_23 = datetime.datetime.strptime("2019-02-23", "%Y-%m-%d")
            cmp_time_23_night = datetime.datetime.strptime("2019-02-23 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_24 = datetime.datetime.strptime("2019-02-24", "%Y-%m-%d")
            cmp_time_24_night = datetime.datetime.strptime("2019-02-24 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_25 = datetime.datetime.strptime("2019-02-25", "%Y-%m-%d")
            cmp_time_25_night = datetime.datetime.strptime("2019-02-25 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_26 = datetime.datetime.strptime("2019-02-26", "%Y-%m-%d")
            cmp_time_26_night = datetime.datetime.strptime("2019-02-26 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_27 = datetime.datetime.strptime("2019-02-27", "%Y-%m-%d")
            cmp_time_27_night = datetime.datetime.strptime("2019-02-27 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_28 = datetime.datetime.strptime("2019-02-28", "%Y-%m-%d")
            cmp_time_28_night = datetime.datetime.strptime("2019-02-28 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_01 = datetime.datetime.strptime("2019-03-01", "%Y-%m-%d")
            cmp_time_01_night = datetime.datetime.strptime("2019-03-01 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_02 = datetime.datetime.strptime("2019-03-02", "%Y-%m-%d")
            cmp_time_02_night = datetime.datetime.strptime("2019-03-02 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_03 = datetime.datetime.strptime("2019-03-03", "%Y-%m-%d")
            cmp_time_03_night = datetime.datetime.strptime("2019-03-03 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_04 = datetime.datetime.strptime("2019-03-04", "%Y-%m-%d")
            cmp_time_04_night = datetime.datetime.strptime("2019-03-04 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_05 = datetime.datetime.strptime("2019-03-05", "%Y-%m-%d")
            cmp_time_05_night = datetime.datetime.strptime("2019-03-05 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_06 = datetime.datetime.strptime("2019-03-06", "%Y-%m-%d")
            cmp_time_06_night = datetime.datetime.strptime("2019-03-06 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_07 = datetime.datetime.strptime("2019-03-07", "%Y-%m-%d")
            cmp_time_07_night = datetime.datetime.strptime("2019-03-07 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_08 = datetime.datetime.strptime("2019-03-08", "%Y-%m-%d")
            cmp_time_08_night = datetime.datetime.strptime("2019-03-08 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_09 = datetime.datetime.strptime("2019-03-09", "%Y-%m-%d")
            cmp_time_09_night = datetime.datetime.strptime("2019-03-09 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_310 = datetime.datetime.strptime("2019-03-10", "%Y-%m-%d")
            cmp_time_310_night = datetime.datetime.strptime("2019-03-10 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_311 = datetime.datetime.strptime("2019-03-11", "%Y-%m-%d")
            cmp_time_311_night = datetime.datetime.strptime("2019-03-11 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_312 = datetime.datetime.strptime("2019-03-12", "%Y-%m-%d")
            cmp_time_312_night = datetime.datetime.strptime("2019-03-12 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_313 = datetime.datetime.strptime("2019-03-13", "%Y-%m-%d")
            cmp_time_313_night = datetime.datetime.strptime("2019-03-13 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_314 = datetime.datetime.strptime("2019-03-14", "%Y-%m-%d")
            cmp_time_314_night = datetime.datetime.strptime("2019-03-14 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_315 = datetime.datetime.strptime("2019-03-15", "%Y-%m-%d")
            cmp_time_315_night = datetime.datetime.strptime("2019-03-15 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_316 = datetime.datetime.strptime("2019-03-16", "%Y-%m-%d")
            cmp_time_316_night = datetime.datetime.strptime("2019-03-16 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_317 = datetime.datetime.strptime("2019-03-17", "%Y-%m-%d")
            cmp_time_317_night = datetime.datetime.strptime("2019-03-17 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_318 = datetime.datetime.strptime("2019-03-18", "%Y-%m-%d")
            cmp_time_318_night = datetime.datetime.strptime("2019-03-18 23:59:59", "%Y-%m-%d %H:%M:%S")

            cmp_time_319 = datetime.datetime.strptime("2019-03-19", "%Y-%m-%d")
            cmp_time_319_night = datetime.datetime.strptime("2019-03-19 23:59:59", "%Y-%m-%d %H:%M:%S")

            if cmp_time_16 <= tmp_line <= cmp_time_16_night:
                Total_Exposure_Log_Data_16.append(line)
                continue
            elif cmp_time_17 <= tmp_line <= cmp_time_17_night:
                Total_Exposure_Log_Data_17.append(line)
                continue
            elif cmp_time_18 <= tmp_line <= cmp_time_18_night:
                Total_Exposure_Log_Data_18.append(line)
                continue
            elif cmp_time_19 <= tmp_line <= cmp_time_19_night:
                Total_Exposure_Log_Data_19.append(line)
                continue
            elif cmp_time_20 <= tmp_line <= cmp_time_20_night:
                Total_Exposure_Log_Data_20.append(line)
                continue
            elif cmp_time_21 <= tmp_line <= cmp_time_21_night:
                Total_Exposure_Log_Data_21.append(line)
                continue
            elif cmp_time_22 <= tmp_line <= cmp_time_22_night:
                Total_Exposure_Log_Data_22.append(line)
                continue
            elif cmp_time_23 <= tmp_line <= cmp_time_23_night:
                Total_Exposure_Log_Data_23.append(line)
                continue
            elif cmp_time_24 <= tmp_line <= cmp_time_24_night:
                Total_Exposure_Log_Data_24.append(line)
                continue
            elif cmp_time_25 <= tmp_line <= cmp_time_25_night:
                Total_Exposure_Log_Data_25.append(line)
                continue
            elif cmp_time_26 <= tmp_line <= cmp_time_26_night:
                Total_Exposure_Log_Data_26.append(line)
                continue
            elif cmp_time_27 <= tmp_line <= cmp_time_27_night:
                Total_Exposure_Log_Data_27.append(line)
                continue
            elif cmp_time_28 <= tmp_line <= cmp_time_28_night:
                Total_Exposure_Log_Data_28.append(line)
                continue
            elif cmp_time_01 <= tmp_line <= cmp_time_01_night:
                Total_Exposure_Log_Data_301.append(line)
                continue
            elif cmp_time_02 <= tmp_line <= cmp_time_02_night:
                Total_Exposure_Log_Data_302.append(line)
                continue
            elif cmp_time_03 <= tmp_line <= cmp_time_03_night:
                Total_Exposure_Log_Data_303.append(line)
                continue
            elif cmp_time_04 <= tmp_line <= cmp_time_04_night:
                Total_Exposure_Log_Data_304.append(line)
                continue
            elif cmp_time_05 <= tmp_line <= cmp_time_05_night:
                Total_Exposure_Log_Data_305.append(line)
                continue
            elif cmp_time_06 <= tmp_line <= cmp_time_06_night:
                Total_Exposure_Log_Data_306.append(line)
                continue
            elif cmp_time_07 <= tmp_line <= cmp_time_07_night:
                Total_Exposure_Log_Data_307.append(line)
                continue
            elif cmp_time_08 <= tmp_line <= cmp_time_08_night:
                Total_Exposure_Log_Data_308.append(line)
                continue
            elif cmp_time_09 <= tmp_line <= cmp_time_09_night:
                Total_Exposure_Log_Data_309.append(line)
                continue
            elif cmp_time_310 <= tmp_line <= cmp_time_310_night:
                Total_Exposure_Log_Data_310.append(line)
                continue
            elif cmp_time_311 <= tmp_line <= cmp_time_311_night:
                Total_Exposure_Log_Data_311.append(line)
                continue
            elif cmp_time_312 <= tmp_line <= cmp_time_312_night:
                Total_Exposure_Log_Data_312.append(line)
                continue
            elif cmp_time_313 <= tmp_line <= cmp_time_313_night:
                Total_Exposure_Log_Data_313.append(line)
                continue
            elif cmp_time_314 <= tmp_line <= cmp_time_314_night:
                Total_Exposure_Log_Data_314.append(line)
                continue
            elif cmp_time_315 <= tmp_line <= cmp_time_315_night:
                Total_Exposure_Log_Data_315.append(line)
                continue
            elif cmp_time_316 <= tmp_line <= cmp_time_316_night:
                Total_Exposure_Log_Data_316.append(line)
                continue
            elif cmp_time_317 <= tmp_line <= cmp_time_317_night:
                Total_Exposure_Log_Data_317.append(line)
                continue
            elif cmp_time_318 <= tmp_line <= cmp_time_318_night:
                Total_Exposure_Log_Data_318.append(line)
                continue
            elif cmp_time_319 <= tmp_line <= cmp_time_319_night:
                Total_Exposure_Log_Data_319.append(line)
                continue
            else:
                print("该条记录不在规定的时间范围之内", line)

# 保存广告记录是16号的数据
Exposure_data_16 = pd.DataFrame(Total_Exposure_Log_Data_16)
Exposure_data_16.to_csv('../../data/temp2/Total_Exposure_Log_Data_16.csv'
                        , index=False, header=None)
del Exposure_data_16, Total_Exposure_Log_Data_16

# 保存广告记录是17号的数据
Exposure_data_17 = pd.DataFrame(Total_Exposure_Log_Data_17)
Exposure_data_17.to_csv('../../data/temp2/Total_Exposure_Log_Data_17.csv'
                        , index=False, header=None)
del Exposure_data_17, Total_Exposure_Log_Data_17

# 保存广告记录是18号的数据
Exposure_data_18 = pd.DataFrame(Total_Exposure_Log_Data_18)
Exposure_data_18.to_csv('../../data/temp2/Total_Exposure_Log_Data_18.csv'
                        , index=False, header=None)
del Exposure_data_18, Total_Exposure_Log_Data_18

# 保存广告记录是19号的数据
Exposure_data_19 = pd.DataFrame(Total_Exposure_Log_Data_19)
Exposure_data_19.to_csv('../../data/temp2/Total_Exposure_Log_Data_19.csv'
                        , index=False, header=None)
del Exposure_data_19, Total_Exposure_Log_Data_19

# 保存广告记录是20号的数据
Exposure_data_20 = pd.DataFrame(Total_Exposure_Log_Data_20)
Exposure_data_20.to_csv('../../data/temp2/Total_Exposure_Log_Data_20.csv'
                        , index=False, header=None)
del Exposure_data_20, Total_Exposure_Log_Data_20

# 保存广告记录是21号的数据
Exposure_data_21 = pd.DataFrame(Total_Exposure_Log_Data_21)
Exposure_data_21.to_csv('../../data/temp2/Total_Exposure_Log_Data_21.csv'
                        , index=False, header=None)
del Exposure_data_21, Total_Exposure_Log_Data_21

# 保存广告记录是22号的数据
Exposure_data_22 = pd.DataFrame(Total_Exposure_Log_Data_22)
Exposure_data_22.to_csv('../../data/temp2/Total_Exposure_Log_Data_22.csv'
                        , index=False, header=None)
del Exposure_data_22, Total_Exposure_Log_Data_22

# 保存广告记录是23号的数据
Exposure_data_23 = pd.DataFrame(Total_Exposure_Log_Data_23)
Exposure_data_23.to_csv('../../data/temp2/Total_Exposure_Log_Data_23.csv'
                        , index=False, header=None)
del Exposure_data_23, Total_Exposure_Log_Data_23

# 保存广告记录是24号的数据
Exposure_data_24 = pd.DataFrame(Total_Exposure_Log_Data_24)
Exposure_data_24.to_csv('../../data/temp2/Total_Exposure_Log_Data_24.csv'
                        , index=False, header=None)
del Exposure_data_24, Total_Exposure_Log_Data_24

# 保存广告记录是25号的数据
Exposure_data_25 = pd.DataFrame(Total_Exposure_Log_Data_25)
Exposure_data_25.to_csv('../../data/temp2/Total_Exposure_Log_Data_25.csv'
                        , index=False, header=None)
del Exposure_data_25, Total_Exposure_Log_Data_25

# 保存广告记录是26号的数据
Exposure_data_26 = pd.DataFrame(Total_Exposure_Log_Data_26)
Exposure_data_26.to_csv('../../data/temp2/Total_Exposure_Log_Data_26.csv'
                        , index=False, header=None)
del Exposure_data_26, Total_Exposure_Log_Data_26

# 保存广告记录是27号的数据
Exposure_data_27 = pd.DataFrame(Total_Exposure_Log_Data_27)
Exposure_data_27.to_csv('../../data/temp2/Total_Exposure_Log_Data_27.csv'
                        , index=False, header=None)
del Exposure_data_27, Total_Exposure_Log_Data_27

# 保存广告记录是28号的数据
Exposure_data_28 = pd.DataFrame(Total_Exposure_Log_Data_28)
Exposure_data_28.to_csv('../../data/temp2/Total_Exposure_Log_Data_28.csv'
                        , index=False, header=None)
del Exposure_data_28, Total_Exposure_Log_Data_28

# 保存广告记录是3月1号的数据
Exposure_data_301 = pd.DataFrame(Total_Exposure_Log_Data_301)
Exposure_data_301.to_csv('../../data/temp2/Total_Exposure_Log_Data_0301.csv'
                         , index=False, header=None)
del Exposure_data_301, Total_Exposure_Log_Data_301

# 保存广告记录是3月2号的数据
Exposure_data_302 = pd.DataFrame(Total_Exposure_Log_Data_302)
Exposure_data_302.to_csv('../../data/temp2/Total_Exposure_Log_Data_0302.csv'
                         , index=False, header=None)
del Exposure_data_302, Total_Exposure_Log_Data_302

# 保存广告记录是3月3号的数据
Exposure_data_303 = pd.DataFrame(Total_Exposure_Log_Data_303)
Exposure_data_303.to_csv('../../data/temp2/Total_Exposure_Log_Data_0303.csv'
                         , index=False, header=None)
del Exposure_data_303, Total_Exposure_Log_Data_303

# 保存广告记录是3月4号的数据
Exposure_data_304 = pd.DataFrame(Total_Exposure_Log_Data_304)
Exposure_data_304.to_csv('../../data/temp2/Total_Exposure_Log_Data_0304.csv'
                         , index=False, header=None)
del Exposure_data_304, Total_Exposure_Log_Data_304

# 保存广告记录是3月5号的数据
Exposure_data_305 = pd.DataFrame(Total_Exposure_Log_Data_305)
Exposure_data_305.to_csv('../../data/temp2/Total_Exposure_Log_Data_0305.csv'
                         , index=False, header=None)
del Exposure_data_305, Total_Exposure_Log_Data_305

# 保存广告记录是3月6号的数据
Exposure_data_306 = pd.DataFrame(Total_Exposure_Log_Data_306)
Exposure_data_306.to_csv('../../data/temp2/Total_Exposure_Log_Data_0306.csv'
                         , index=False, header=None)
del Exposure_data_306, Total_Exposure_Log_Data_306

# 保存广告记录是3月7号的数据
Exposure_data_307 = pd.DataFrame(Total_Exposure_Log_Data_307)
Exposure_data_307.to_csv('../../data/temp2/Total_Exposure_Log_Data_0307.csv'
                         , index=False, header=None)
del Exposure_data_307, Total_Exposure_Log_Data_307

# 保存广告记录是3月8号的数据
Exposure_data_308 = pd.DataFrame(Total_Exposure_Log_Data_308)
Exposure_data_308.to_csv('../../data/temp2/Total_Exposure_Log_Data_0308.csv'
                         , index=False, header=None)
del Exposure_data_308, Total_Exposure_Log_Data_308

# 保存广告记录是3月9号的数据
Exposure_data_309 = pd.DataFrame(Total_Exposure_Log_Data_309)
Exposure_data_309.to_csv('../../data/temp2/Total_Exposure_Log_Data_0309.csv'
                         , index=False, header=None)
del Exposure_data_309, Total_Exposure_Log_Data_309

# 保存广告记录是3月10号的数据
Exposure_data_310 = pd.DataFrame(Total_Exposure_Log_Data_310)
Exposure_data_310.to_csv('../../data/temp2/Total_Exposure_Log_Data_0310.csv'
                         , index=False, header=None)
del Exposure_data_310, Total_Exposure_Log_Data_310

# 保存广告记录是3月11号的数据
Exposure_data_311 = pd.DataFrame(Total_Exposure_Log_Data_311)
Exposure_data_311.to_csv('../../data/temp2/Total_Exposure_Log_Data_0311.csv'
                         , index=False, header=None)
del Exposure_data_311, Total_Exposure_Log_Data_311

# 保存广告记录是3月12号的数据
Exposure_data_312 = pd.DataFrame(Total_Exposure_Log_Data_312)
Exposure_data_312.to_csv('../../data/temp2/Total_Exposure_Log_Data_0312.csv'
                         , index=False, header=None)
del Exposure_data_312, Total_Exposure_Log_Data_312

# 保存广告记录是3月13号的数据
Exposure_data_313 = pd.DataFrame(Total_Exposure_Log_Data_313)
Exposure_data_313.to_csv('../../data/temp2/Total_Exposure_Log_Data_0313.csv'
                         , index=False, header=None)
del Exposure_data_313, Total_Exposure_Log_Data_313

# 保存广告记录是3月14号的数据
Exposure_data_314 = pd.DataFrame(Total_Exposure_Log_Data_314)
Exposure_data_314.to_csv('../../data/temp2/Total_Exposure_Log_Data_0314.csv'
                         , index=False, header=None)
del Exposure_data_314, Total_Exposure_Log_Data_314

# 保存广告记录是3月15号的数据
Exposure_data_315 = pd.DataFrame(Total_Exposure_Log_Data_315)
Exposure_data_315.to_csv('../../data/temp2/Total_Exposure_Log_Data_0315.csv'
                         , index=False, header=None)
del Exposure_data_315, Total_Exposure_Log_Data_315

# 保存广告记录是3月16号的数据
Exposure_data_316 = pd.DataFrame(Total_Exposure_Log_Data_316)
Exposure_data_316.to_csv('../../data/temp2/Total_Exposure_Log_Data_0316.csv'
                         , index=False, header=None)
del Exposure_data_316, Total_Exposure_Log_Data_316

# 保存广告记录是3月17号的数据
Exposure_data_317 = pd.DataFrame(Total_Exposure_Log_Data_317)
Exposure_data_317.to_csv('../../data/temp2/Total_Exposure_Log_Data_0317.csv'
                         , index=False, header=None)
del Exposure_data_317, Total_Exposure_Log_Data_317

# 保存广告记录是3月18号的数据
Exposure_data_318 = pd.DataFrame(Total_Exposure_Log_Data_318)
Exposure_data_318.to_csv('../../data/temp2/Total_Exposure_Log_Data_0318.csv'
                         , index=False, header=None)
del Exposure_data_318, Total_Exposure_Log_Data_318

# 保存广告记录是3月19号的数据
Exposure_data_319 = pd.DataFrame(Total_Exposure_Log_Data_319)
Exposure_data_319.to_csv('../../data/temp2/Total_Exposure_Log_Data_0319.csv'
                         , index=False, header=None)
del Exposure_data_319, Total_Exposure_Log_Data_319


# 拼接操作
Exposure_Log_Data_columns = ['Ad_Request_id', 'Ad_Request_Time', 'Ad_pos_id', 'user_id', 'ad_id',
                             'Ad_material_size',
                             'Ad_bid', 'Ad_pctr', 'Ad_quality_ecpm', 'Ad_total_Ecpm']

Total_Exposure_Log_Data_February = pd.concat(
    [pd.read_csv('../../data/temp2/Total_Exposure_Log_Data_' + str(i) + '.csv', names=Exposure_Log_Data_columns)
     for i in range(16, 29)]).reset_index(drop=True)

Total_Exposure_Log_Data_February.to_csv('../../data/temp2/Total_Exposure_Log_Data_February.csv', index=False,
                                        header=Exposure_Log_Data_columns)

Total_Exposure_Log_Data_March = pd.concat(
    [pd.read_csv('../../data/temp2/Total_Exposure_Log_Data_03' + str(i).zfill(2) + '.csv',
                 names=Exposure_Log_Data_columns) for i
     in range(1, 20)]).reset_index(drop=True)

Total_Exposure_Log_Data_March.to_csv('../../data/temp2/Total_Exposure_Log_Data_March.csv', index=False)


# 拼接
df_February = pd.read_csv('../../data/temp2/Total_Exposure_Log_Data_February.csv')
df_March = pd.read_csv('../../data/temp2/Total_Exposure_Log_Data_March.csv')

Total_Exposure_Log_Data = pd.concat([df_February, df_March]).reset_index(drop=True)
Total_Exposure_Log_Data.to_csv('../../data/temp2/Total_Exposure_Log_Data.csv', index=False,
                               header=Exposure_Log_Data_columns)


Exposure_data = pd.read_csv('../../data/temp2/Total_Exposure_Log_Data.csv')
Exposure_data.drop('Ad_pos_id', axis=1, inplace=True)
Exposure_data.drop('Ad_pctr', axis=1, inplace=True)
Exposure_data.drop('Ad_quality_ecpm', axis=1, inplace=True)
Exposure_data.drop('Ad_total_Ecpm', axis=1, inplace=True)
Exposure_data.to_csv('../../data/temp2/Total_Exposure_Log_Data_drop.csv', index=False)
