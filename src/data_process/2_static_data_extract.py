# @Time    : 2019/5/15
# @Author  : Weikoi
# @Email   : 17210240112@fudan.edu.cn
# @File    : 2_static_data_extract.py

import pandas as pd
import time

pd.set_option('display.max_columns', 20)
Ad_Static_Feature_Data = []

# 定义曝光日志中的相关列
Ad_Static_Feature_Data_columns = ['ad_id', 'Creation_time', 'Ad_account_id', 'Commodity_id', 'Commodity_type',
                                  'Ad_Industry_Id', 'Ad_material_size']

# 为数据集增加列名称
with open('../../data/raw/ad_static_feature.out', 'r') as f:
    for i, line in enumerate(f):
        # print(i, ':', line,'\n', len(line), type(line))
        line = line.strip().split('\t')
        # print(i, ':', line,  '\n', type(line), len(line))
        # print('每一个元素的取值类型: ', type(line[1]), type(line[2]), type(line[3]), type(line[4]))

        # 测试数据集的时候使用
        # if i > 1000:
        # break
        if len(line) != 7:
            # print("广告数据集中出现缺失数据: ", line)
            continue

        # 分别用于判断该条广告数据是否存在记录缺失 是否创建时间为0 广告行业是否存在多值
        if line[1] == '0':
            # print("数据集中创建时间为0的数据集是: ", line)
            continue
        if ',' in line[5]:
            # print("数据集中广告行业ID存在多值记录是: ", line)
            continue
        if ',' in line[6]:
            # print("数据集中广告行业ID存在多值记录是: ", line)
            continue

        # 4-19新加该功能 静态广告时间的格式是2018/6/26 4:35:50
        # print(line[1], type(line[1]), line)
        loacl_time = int(line[1])
        time_local = time.localtime(loacl_time)
        line[1] = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

        Ad_Static_Feature_Data.append(line)

print("============userFeature_data[0]:============\n", Ad_Static_Feature_Data[1])

ad_feature = pd.DataFrame(Ad_Static_Feature_Data)

ad_feature.to_csv('../../data/temp2/Ad_Static_Feature_Data.csv', index=False,
                  header=Ad_Static_Feature_Data_columns)

ad_feature_drop = pd.read_csv('../../data/temp2/Ad_Static_Feature_Data.csv')

print(ad_feature_drop)
"""
注意，两边都有素材尺寸，该如何处理？先丢掉再说。
"""
ad_feature_drop.drop('Creation_time', axis=1, inplace=True)
ad_feature_drop.drop('Ad_material_size', axis=1, inplace=True)
ad_feature_drop.to_csv('../../data/temp2/Ad_Static_Feature_Data_drop.csv', index=False,
                       header=True)
