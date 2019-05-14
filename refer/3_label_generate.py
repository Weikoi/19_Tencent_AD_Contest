# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 15:55
# @Author  : YYLin
# @Email   : 854280599@qq.com
# @File    : Generator_Label_For_Train.py
import pandas as pd
import datetime
import numpy as np

# 生成点击数并且暂时删除测试集中没有的属性
Total_Exposure_Log_Data = pd.read_csv('../data/dataset/process/Total_Exposure_Log_Data.csv')
print("原始数据集中的样式是:\n", Total_Exposure_Log_Data.info())
tfa = Total_Exposure_Log_Data.Ad_Request_Time.astype(str).apply(lambda x: datetime.datetime(int(x[:4]),
                                                                                            int(x[5:7]),
                                                                                            int(x[8:10]),
                                                                                            int(x[11:13]),
                                                                                            int(x[14:16]),
                                                                                            int(x[17:])))

Total_Exposure_Log_Data['tfa_year'] = np.array([x.year for x in tfa])
Total_Exposure_Log_Data['tfa_month'] = np.array([x.month for x in tfa])
Total_Exposure_Log_Data['tfa_day'] = np.array([x.day for x in tfa])
print("增加单独的年月日之后的数据形状是:\n", Total_Exposure_Log_Data.info())

Group_Exposure_Data = Total_Exposure_Log_Data.groupby(
    ['tfa_year', 'tfa_month', 'tfa_day', 'ad_id', 'Ad_bid']).size().reset_index()
Group_Exposure_Data = Group_Exposure_Data.rename(columns={0: 'num_click'})
print("按照年月日 广告id和广告竞价进行分组之后的数据是:\n", Group_Exposure_Data.head(5))

# 将曝光数据按照年月日 广告id和广告竞价删除重复的元素之后进行合并
Total_Exposure_Log_Data_one = Total_Exposure_Log_Data.drop_duplicates(
    subset=['tfa_year', 'tfa_month', 'tfa_day', 'ad_id', 'Ad_bid'], keep="first").reset_index(drop=True)
Clicks_of_Exposure_Data = pd.merge(Total_Exposure_Log_Data_one, Group_Exposure_Data,
                                   on=['tfa_year', 'tfa_month', 'tfa_day', 'ad_id', 'Ad_bid'])

# 删除测试集中没有的相关属性 并将结果进行保存
Clicks_of_Exposure_Data.drop('Ad_Request_id', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('Ad_Request_Time', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('user_id', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('Ad_material_size', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('Ad_pctr', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('Ad_quality_ecpm', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('Ad_total_Ecpm', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('tfa_year', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('tfa_month', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('tfa_day', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('Ad_pos_id', axis=1, inplace=True)
Clicks_of_Exposure_Data.drop('Ad_bid', axis=1, inplace=True)

print("==========广告数据集中需要保存的信息格式是:============\n", Clicks_of_Exposure_Data.info())
Clicks_of_Exposure_Data.to_csv('../data/dataset/process/Clicks_of_Exposure_Data.csv', index=False)

# 将曝光日志按照ID和静态广告数据进行拼接操作
Ad_Static_Data = pd.read_csv('../data/dataset/process/Ad_Static_Feature_Data.csv')
Ad_Static_Data.drop('Commodity_id', axis=1, inplace=True)
Ad_Static_Data.drop('Ad_account_id', axis=1, inplace=True)
Ad_Static_Data.drop('Creation_time', axis=1, inplace=True)
print("==========静态数据集的样式是:==========\n", Ad_Static_Data.info())
Merce_Ad_Static_and_Exposure_Data = pd.merge(Clicks_of_Exposure_Data, Ad_Static_Data, on=['ad_id'])

# 读取广告操作数据集并拼接数据集
Op_Ad_Data = pd.read_csv('../data/dataset/process/Ad_Operation_Data.csv').drop_duplicates(['ad_id'])
Op_Ad_Data.drop('Create_modify_time', axis=1, inplace=True)

Dataset_For_Train = pd.merge(Op_Ad_Data, Merce_Ad_Static_and_Exposure_Data, on=['ad_id'])
print("最后数据集保存的样式是:\n", Dataset_For_Train.info())
Dataset_For_Train.to_csv('../data/dataset/process/Dataset_For_Train.csv', index=False)


