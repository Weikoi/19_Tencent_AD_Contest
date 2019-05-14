# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 8:53
# @Author  : YYLin
# @Email   : 854280599@qq.com
# @File    : Redo_Dataload_Sample_Data.py
import pandas as pd
import pickle as pk
import sys

Test_Sample_Data = []
Test_Sample_Data_columns = ['ad_id', 'ad_bid', 'num_click', 'Ad_material_size', 'Ad_Industry_Id', 'Commodity_type',
                            'Delivery_time', 'age', 'gender', 'area', 'education', 'device', 'consuptionAbility',
                            'status', 'connectionType', 'behavior']

# 为数据集增加列名称 其中的num_click全部设置成-3
Test_Sample_Data.append(Test_Sample_Data_columns)
int_num_click = -3


"""
用户数据信息处理
"""
# 测试样本中人群定向是all的时候 利用原始的user.data将数据集划分
# 注意数据集的选取决定了训练集的数据量大小
user_data = pd.read_csv('../data/dataset/process/userFeature.csv')
print("=============user_data==============", user_data.info())

"""
用户年龄
"""
User_age = user_data['Age'].drop_duplicates(keep='first', inplace=False)
User_age = list(User_age)
User_age = [str(x) for x in User_age]
all_age = ' '.join(User_age)
# print("all_age的样式是:\n", all_age, type(all_age))

"""
用户性别
"""
User_Gender = user_data['Gender'].drop_duplicates(keep='first', inplace=False)
User_Gender = list(User_Gender)
User_Gender = [str(x) for x in User_Gender]
all_Gender = ' '.join(User_Gender)

"""
用户地域
"""
# 因为地域这列属性可以取多值 所以需要对其合并成一维数组之后 然后在执行去重操作
User_Area = user_data['Area']
User_Area = list(User_Area)
for i, temp_line in enumerate(User_Area):
    User_Area[i] = temp_line.strip().split(',')
print(User_Area)

result = []
for idx, i in enumerate(User_Area):
    result += i
    if idx % 100 == 0:
        print("\r当前进度: {:.2f}%".format((idx + 1) * 100 / 1396718), end="")
# print("User_Area转化成一维数组之后前20个数据是", User_Area[0:20], type(User_Area))
User_Area_set = list(set(result))
# print("User_Area经过去重之后前20个数据是", User_Area_set[0:20], len(User_Area_set))
User_Area = [str(x) for x in User_Area]
all_Area = ' '.join(User_Area)
# print("all_Area的类型是:\n", type(all_Area), type(all_Area[1]), )
# print("在用户文件之中地域的取值为:\n", all_Area[0:10], len(all_Area))

"""
用户学历
"""
User_Education = user_data['Education'].drop_duplicates(keep='first', inplace=False)
User_Education = list(User_Education)
User_Education = [str(x) for x in User_Education]
all_Education = ' '.join(User_Education)
# print("all_Education的类型是:\n", len(all_Education), type(all_Education), type(all_Education[1]))

"""
用户消费级别
"""
User_Consuption_Ability = user_data['Consuption_Ability'].drop_duplicates(keep='first', inplace=False)
User_Consuption_Ability = list(User_Consuption_Ability)
User_Consuption_Ability = [str(x) for x in User_Consuption_Ability]
all_Consuption_Ability = ' '.join(User_Consuption_Ability)

"""
用户年登录设备
"""
User_Device = user_data['Device'].drop_duplicates(keep='first', inplace=False)
User_Device = list(User_Device)
User_Device = [str(x) for x in User_Device]
all_Device = ' '.join(User_Device)

"""
用户工作信息
"""
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
print("User_Work_Status")
status_result = []
for idx, i in enumerate(User_Work_Status):
    status_result += i
User_Work_Status = list(set(status_result))
User_Work_Status = [str(x) for x in User_Work_Status]
all_Work_Status = ' '.join(User_Work_Status)
# print("最后User_Work_Status的取值范围是:\n", all_Work_Status)

"""
用户网络信息
"""
print("User_Connection_Type")
User_Connection_Type = user_data['Connection_Type'].drop_duplicates(keep='first', inplace=False)
User_Connection_Type = list(User_Connection_Type)
User_Connection_Type = [str(x) for x in User_Connection_Type]
all_Connection_Type = ' '.join(User_Connection_Type)


"""
用户行为信息，此维度数据量巨大，难以处理
"""
# 该方法的目的是找到Behavior中所有唯一值，当出现all的时候 将Behavior的值赋值给该条数据，
# 但是发现数据集中Behavior太多 暂时不执行该操作
User_Behavior = user_data['Behavior']

temp_result = []

print("原始数据集中用户行为的结果为:\n", type(User_Behavior))
# 将二维数组转化成一维数组
for i, temp_line in enumerate(User_Behavior):
    if ',' in temp_line:
        temp_result.append(temp_line.strip().split(','))
    else:
        temp_result.append(list(temp_line))
        # del User_Behavior[i]


# User_Behavior.pop(0)
# 首先将数据降维到一维数组 然后去掉list中重复的元素
result_behavior = []
for idx, i in enumerate(temp_result):
    result_behavior += i
    # if idx % 1000 == 0:
    #     print("\r当前进度: {:.2f}%".format((idx + 1) * 100 / len(User_Behavior)), end="")

User_Behavior = list(set(result_behavior))
Str_User_Behavior = [str(x) for x in User_Behavior]
all_Behavior = ' '.join(Str_User_Behavior)
# print("用户数据集中Behavior的取值范围是", len(User_Behavior))
print("用户数据集中所有的属性值已加载完毕！！！！")


# 需要重写测试集中的人群定向
with open('../data/raw/test_sample.dat', 'r') as f:
    for i, line in enumerate(f):
        # if i % 100 == 0:
        #     print("\r当前进度: {:.2f}%".format((i + 1) * 100 / 20290), end="")


        # 测试的时候使用的数据
        # sys.exit()

        # 原始数据每列属性的含义 修改数据之后每列属性的含义
        # Sample_id ad_id Creation_time Ad_material_size Ad_Industry_Id Commodity_type Commerce_id Account_id
        # Delivery_time Chose_People ad_bid
        # 'ad_id', 'ad_bid', 'num_click', 'Ad_material_size', 'Ad_Industry_Id', 'Commodity_type', 'Delivery_time',

        # 定义一个临时的数组用于缓存数据集 首先加载的属性是直接能够从原始数据中
        save_line = []
        line = line.strip().split('\t')
        # print("line:", line, '\n', 'line[9]:', line[9], type(line))

        save_line.append(line[1])
        save_line.append(line[10])
        save_line.append(int_num_click)
        save_line.append(line[3])
        save_line.append(line[4])
        save_line.append(line[5])

        # 对于属性中存在的多值属性将其中的逗号转化成空格 验证成功
        tmp_line_6 = line[8].strip().split(',')
        line[8] = ' '.join(tmp_line_6)
        save_line.append(line[8])
        # print("最后用于保存的数据的格式:\n", save_line)

        # 对文件中存在的人群定向分离出各个子节点
        tmp_line = line[9].strip().split('|')
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

        # 当定向人群是all的时候 因为Behavior的数据比较大， 所以在使用Behavior值使用-2代替
        value_all = 'all'

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
        # print(save_line)
        # 保存最后的结果数据集
        Test_Sample_Data.append(save_line)
        if i == 2:
            print("=========最后用于保存结果的数据格式是:======\n", Test_Sample_Data[3][10], '\n', len(Test_Sample_Data[3][10]))

# 测试成功！！！！！数据集保存正确
user_feature = pd.DataFrame(Test_Sample_Data)
print(user_feature.info())
user_feature.to_csv('../data/dataset/result/Test_Sample_Data_all.csv', index=False, header=None)
