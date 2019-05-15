# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 14:33
# @Author  : YYLin
# @Email   : 854280599@qq.com
# @File    : Redo_Dataload_For_Train.py
# 测试样本中的格式是
# ad_id ad_bid num_click Ad_material_size Ad_Industry_Id Commodity_type Delivery_time
# age gender area education device consuptionAbility status connectionType behavior
# 首先使用pandas将数据集划分成三个部分 分别是单独属性 人群定向文件 以及最后的投放时间
import time

import pandas as pd
from functools import reduce
import operator
import sys

data_for_train = pd.read_csv('../data/dataset/process/Dataset_For_Train.csv')
print("data_for_train info", data_for_train.info())

data_for_chose_people = data_for_train['Chose_People']

data_for_chose_time = data_for_train['Delivery_time']

data_for_train.drop('Chose_People', axis=1, inplace=True)
data_for_train.drop('Delivery_time', axis=1, inplace=True)
data_for_train = data_for_train[
    ['ad_id', 'ad_bid', 'num_click', 'Ad_material_size', 'Ad_Industry_Id', 'Commodity_type']]

data_for_chose_people.to_csv('../data/dataset/process/Chose_People.csv', index=False)
data_for_chose_time.to_csv('../data/dataset/process/Chose_Time.csv', index=False)
data_for_train.to_csv('../data/dataset/process/Data_For_Train_Test.csv', index=False)

time_line = []
count_line_of_time = 1
time_line.append('Delivery_time')

with open('../data/dataset/process/Chose_Time.csv', 'r') as f:
    for i, line in enumerate(f):
        # 测试代码的时候使用
        if i >= 1000:
            break
        count_line_of_time = count_line_of_time + 1
        tmp_line = line.strip().split(',')
        line = ' '.join(tmp_line)
        time_line.append(line)
chose_time = pd.DataFrame(time_line)
chose_time.to_csv('../data/dataset/process/Chose_Time.csv', index=False, header=False)

# 删除已经运行结束的变量 节省内存
del chose_time, time_line

"""
处理定向用户数据
"""
people_line = []
count_line_of_people = 1
people_line_columns = ['age', 'gender', 'area', 'education', 'device', 'consuptionAbility', 'status', 'connectionType',
                       'behavior']
people_line.append(people_line_columns)

# 从user_data中提取相关的属性信息
# 测试样本中人群定向是all的时候 利用原始的user.data将数据集划分
user_data = pd.read_csv('../data/dataset/process/userFeature10000.csv')
print("\n=============user_data=====================", user_data.info(), "\n")
User_age = user_data['Age'].drop_duplicates(keep='first', inplace=False)
User_age = list(User_age)
User_age = [str(x) for x in User_age]
all_age = ' '.join(User_age)
# print("all_age的样式是:\n", all_age, type(all_age))

User_Gender = user_data['Gender'].drop_duplicates(keep='first', inplace=False)
User_Gender = list(User_Gender)
User_Gender = [str(x) for x in User_Gender]
all_Gender = ' '.join(User_Gender)

# 因为地域这列属性可以取多值 所以需要对其合并成一维数组之后 然后在执行去重操作
User_Area = user_data['Area']
User_Area = list(User_Area)
for i, temp_line in enumerate(User_Area):
    User_Area[i] = temp_line.strip().split(',')

result_area = []
for i in User_Area:
    result_area += i
# User_Area = reduce(operator.add, User_Area)
# print("User_Area转化成一维数组之后前20个数据是", User_Area[0:20], type(User_Area))
User_Area_set = list(set(result_area))
# print("User_Area经过去重之后前20个数据是", User_Area_set[0:20], len(User_Area_set))
User_Area = [str(x) for x in User_Area]
all_Area = ' '.join(User_Area)
print("===================all_Area的类型是:\n=====================", type(all_Area), type(all_Area[1]), )
# print("在用户文件之中地域的取值为:\n", all_Area[0:10], len(all_Area))

User_Education = user_data['Education'].drop_duplicates(keep='first', inplace=False)
User_Education = list(User_Education)
User_Education = [str(x) for x in User_Education]
all_Education = ' '.join(User_Education)
print("===================all_Education的类型是:\n================", len(all_Education), type(all_Education), type(all_Education[1]))

User_Consuption_Ability = user_data['Consuption_Ability'].drop_duplicates(keep='first', inplace=False)
User_Consuption_Ability = list(User_Consuption_Ability)
User_Consuption_Ability = [str(x) for x in User_Consuption_Ability]
all_Consuption_Ability = ' '.join(User_Consuption_Ability)

User_Device = user_data['Device'].drop_duplicates(keep='first', inplace=False)
User_Device = list(User_Device)
User_Device = [str(x) for x in User_Device]
all_Device = ' '.join(User_Device)

# 对于工作可能是取多值的情况 所以参照地域的取值方式
User_Work_Status = user_data['Work_Status']
User_Work_Status = list(User_Work_Status)
for i, temp_line in enumerate(User_Work_Status):
    if ',' in temp_line:
        # print("temp_line是:", temp_line)
        User_Work_Status[i] = temp_line.strip().split(',')
    else:
        User_Work_Status[i] = list(temp_line)
# print("经过修改操作之后的User_Work_Status是:", User_Work_Status[0:10], type(User_Work_Status))

result_status = []

for i in User_Work_Status:
    result_status += i
# User_Work_Status = reduce(operator.add, User_Work_Status)
User_Work_Status = list(set(result_status))
User_Work_Status = [str(x) for x in User_Work_Status]
all_Work_Status = ' '.join(User_Work_Status)
# print("最后User_Work_Status的取值范围是:\n", all_Work_Status)

User_Connection_Type = user_data['Connection_Type'].drop_duplicates(keep='first', inplace=False)
User_Connection_Type = list(User_Connection_Type)
User_Connection_Type = [str(x) for x in User_Connection_Type]
all_Connection_Type = ' '.join(User_Connection_Type)

# 该方法的目的是找到Behavior中所有唯一值，当出现all的时候 将Behavior的值赋值给该条数据，
# 但是发现数据集中Behavior太多 暂时不执行该操作
User_Behavior = user_data['Behavior']
User_Behavior = list(User_Behavior)
print("=================原始数据集中用户行为的结果为:=================\n", type(User_Behavior[0:-1]))
# 将二维数组转化成一维数组
for i, temp_line in enumerate(User_Behavior):
    if ',' in temp_line:
        User_Behavior[i] = temp_line.strip().split(',')
    else:
        # print("Behavior中异常的数据是:", User_Behavior[i])
        User_Behavior[i] = list(temp_line)
        # del User_Behavior[i]

# User_Behavior.pop(0)
# 首先将数据降维到一维数组 然后去掉list中重复的元素
result_behavior = []
for i in User_Behavior:
    result_behavior += i
# User_Behavior = reduce(operator.add, User_Behavior)
User_Behavior = list(set(result_behavior))
Str_User_Behavior = [str(x) for x in User_Behavior]
all_Behavior = ' '.join(Str_User_Behavior)
print("=================用户数据集中Behavior的取值范围是==================", len(User_Behavior))

with open('../data/dataset/process/Chose_People.csv', 'r') as f:
    for i, line in enumerate(f):
        # 测试代码的时候使用
        # if i >= 2:
        #     break
        if i >= 1000:
            break
        count_line_of_people = count_line_of_people + 1

        if i % 10000 == 0:
            print("我已经执行了%d条数据了" % (i))
        # 开始处理人群定向数据集 定向人群属性列的格式是:
        #  'age', 'gender', 'area', 'education', 'device',
        #  'consuptionAbility', 'status', 'connectionType', 'behavior'

        # 对文件中存在的人群定向分离出各个子节点
        tmp_line = line.strip().split('|')
        userFeature_dict = {}

        for each in tmp_line:
            each_list = each.split(':')
            userFeature_dict[each_list[0]] = ' '.join(each_list[1:])

        # print(result_of_line_9)
        value_age = ''
        value_gender = ''
        value_area = ''
        value_education = ''
        value_device = ''
        value_consuptionAbility = ''
        value_status = ''
        value_connectionType = ''
        value_behavior = ''

        # 当定向人群是all的时候 需要特殊处理
        value_all = 'all'
        save_line = []

        if value_all in userFeature_dict.keys():
            value_age = all_age
            value_gender = all_Gender
            value_area = all_Area
            value_education = all_Education
            value_consuptionAbility = all_Consuption_Ability
            value_device = all_Device
            value_status = all_Work_Status
            value_connectionType = all_Connection_Type
            value_behavior = all_Behavior
        else:
            if 'age' in userFeature_dict.keys():
                value_age = userFeature_dict['age']
                # print(userFeature_dict['age'], type(userFeature_dict['age']))
            if 'gender' in userFeature_dict.keys():
                value_gender = userFeature_dict['gender']
                # print(userFeature_dict['gender'], type(userFeature_dict['gender']))
            if 'area' in userFeature_dict.keys():
                value_area = userFeature_dict['area']
                # print(userFeature_dict['area'], type(userFeature_dict['area']))
            if 'education' in userFeature_dict.keys():
                value_education = userFeature_dict['education']
                # print(userFeature_dict['education'], type(userFeature_dict['education']))
            if 'device' in userFeature_dict.keys():
                value_device = userFeature_dict['device']
                # print(userFeature_dict['device'], type(userFeature_dict['device']))
            if 'consuptionAbility' in userFeature_dict.keys():
                value_consuptionAbility = userFeature_dict['consuptionAbility']
                # print(userFeature_dict['consuptionAbility'], type(userFeature_dict['consuptionAbility']))
            if 'status' in userFeature_dict.keys():
                value_status = userFeature_dict['status']
                # print(userFeature_dict['value_status'], type(userFeature_dict['value_status']))
            if 'connectionType' in userFeature_dict.keys():
                value_connectionType = userFeature_dict['connectionType']
            if 'behavior' in userFeature_dict.keys():
                value_behavior = userFeature_dict['behavior']
        # 对于人群定向列属性 指定的属性列是: 'age', 'gender', 'area', 'education',
        # 'device', 'consuptionAbility', 'status', 'connectionType', 'behavior'
        save_line.append(value_age)
        save_line.append(value_gender)
        save_line.append(value_area)
        save_line.append(value_education)
        save_line.append(value_device)
        save_line.append(value_consuptionAbility)
        save_line.append(value_status)
        save_line.append(value_connectionType)
        save_line.append(value_behavior)
        people_line.append(save_line)

if count_line_of_people != count_line_of_time:
    print("数据集中的人群定向和指定时间行数不相等，系统退出")
    sys.exit()

print("=========================程序已经加载完毕，正在保存数据=====================")
print(len(people_line))
chose_people = pd.DataFrame(people_line)
print(chose_people.info())
print("\n->->->->->占用内存空间：",sys.getsizeof(chose_people) / 1024 / 1024 / 1024, 'GB')

# print(data_for_chose_people.info())
# chose_people.to_csv('../dataset/data/Chose_people_demo.csv', index=False)
# chose_people.to_csv('../dataset/data/Chose_people_demo.csv', index=False)

print("已经保存好人群定向的数据，开始将三个数据进行拼接操作")
# 最后将三个已保存的数据进行拼接即可
Test_Sample_Data_time = pd.read_csv('../data/dataset/process/Chose_Time.csv')
Test_Sample_Data_train = pd.read_csv('../data/dataset/process/Data_For_Train_Test.csv')

result = pd.concat([Test_Sample_Data_train, Test_Sample_Data_time, chose_people], axis=1)
result.to_csv('../data/dataset/result/train_dataset.csv', index=False)
