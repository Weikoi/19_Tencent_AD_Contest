# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:40
# @Author  : YYLin
# @Email   : 854280599@qq.com
# @File    : Dataload_User.py

"""
关于用户数量：
"""
import pandas as pd

userFeature_data = []

user_Feature_columns = ['user_id', 'Age', 'Gender', 'Area', 'Marriage_Status', 'Education', 'Consuption_Ability',
                        'Device',
                        'Work_Status', 'Connection_Type', 'Behavior']

# 为数据集增加列名称 对于userFeature_data不需要对某一列的数据进行处理

"""
选择用户的数量
"""

mode = "10000"

if mode == 'all':
    userFeature_data.append(user_Feature_columns)
    with open('../user_data', 'r') as f:
        for i, line in enumerate(f):
            # print(i, ':', line,'\n', len(line), type(line))
            line = line.strip().split('\t')
            # print(i, ':', line, type(line),'\n', len(line))
            # if i > 10000:
            #     break
            userFeature_data.append(line)

    print("***********userFeature_data[0]:\n", userFeature_data[1])
    print("***********userFeature_data[0][1]:\n", userFeature_data[1][0])
    user_feature = pd.DataFrame(userFeature_data)
    print("***********正在保存数据集************")
    user_feature.to_csv('../Dataset/dataset_for_train/userFeature.csv', index=False, header=False)

if mode == '10000':
    userFeature_data.append(user_Feature_columns)
    with open('../user_data', 'r') as f:
        for i, line in enumerate(f):
            # print(i, ':', line,'\n', len(line), type(line))
            line = line.strip().split('\t')
            # print(i, ':', line, type(line),'\n', len(line))
            if i > 10000:
                break
            userFeature_data.append(line)

    print("***********userFeature_data[0]:\n", userFeature_data[1])
    print("***********userFeature_data[0][1]:\n", userFeature_data[1][0])
    user_feature = pd.DataFrame(userFeature_data)
    print("***********正在保存数据集************")
    user_feature.to_csv('../Dataset/dataset_for_train/userFeature10000.csv', index=False, header=False)

