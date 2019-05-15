# # -*- coding: utf-8 -*-
# # @Time    : 2019/5/4 10:29
# # @Author  : YYLin
# # @Email   : 854280599@qq.com
# # @File    : Code_For_Tencent_Improve_V2.py
#
# # 该模型的提升方案是首先使用均值对数据集进行补齐操作 然后对于特殊的字段使用独特的编码方式
# import pandas as pd
# import matplotlib.pyplot as plt
# import xgboost as xgb
# from sklearn import preprocessing
# import numpy as np
# from xgboost import plot_importance
# from sklearn.preprocessing import Imputer
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.preprocessing import OneHotEncoder, LabelEncoder
# import sys
#
#
# def featureSet(data):
#     # 首先是对缺失数据使用均值进行填充 缺失数据集中的属性大多是多值 使用均值填充效果应该不好 暂时不使用
#
#     '''
#     imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
#     imputer.fit(data.loc[:, ['area', 'status', 'behavior',  'age', 'gender', 'education','device', 'consuptionAbility',
#                              'connectionType']])
#     x_new = imputer.transform(data.loc[:, ['area', 'status', 'behavior',  'age', 'gender', 'education','device',
#                                            'consuptionAbility',  'connectionType']])
#     '''
#
#     # 对不同的属性列使用不同编码方式 下列属性使用one-hot encoding的数据类型
#     att_ad_bid = LabelEncoder().fit_transform(data['ad_bid'].apply(int))
#     att_Ad_Industry_Id = LabelEncoder().fit_transform(data['Ad_Industry_Id'].apply(int))
#     att_Commodity_type = LabelEncoder().fit_transform(data['Commodity_type'].apply(int))
#     att_Ad_material_size = LabelEncoder().fit_transform(data['Ad_material_size'].apply(int))
#
#     # 开始处理多值属性 参考代码见
#     cv = CountVectorizer()
#     # cv.fit(data['Delivery_time'])
#     # train_Delivery_time = cv.transform(data['Delivery_time'])
#
#     train_area = cv.fit_transform(data['area']).values.astype('U')
#
#     cv.fit(data['status'])
#     train_status = cv.transform(data['status'])
#
#     cv.fit(data['behavior'])
#     train_behavior = cv.transform(data['behavior'])
#
#     cv.fit(data['age'])
#     train_age = cv.transform(data['age'])
#
#     cv.fit(data['gender'])
#     train_gender = cv.transform(data['gender'])
#
#     cv.fit(data['education'])
#     train_education = cv.transform(data['education'])
#
#     cv.fit(data['device'])
#     train_device = cv.transform(data['device'])
#
#     cv.fit(data['consuptionAbility'])
#     train_consuptionAbility = cv.transform(data['consuptionAbility'])
#
#     cv.fit(data['connectionType'])
#     train_connectionType = cv.transform(data['connectionType'])
#
#     data_num = len(data)
#     XList = []
#     for row in range(0, data_num):
#         tmp_list = []
#         tmp_list.append(att_ad_bid[row])
#         tmp_list.append(att_Ad_Industry_Id[row])
#         tmp_list.append(att_Commodity_type[row])
#         tmp_list.append(att_Ad_material_size[row])
#
#         # 以下属性为多值属性
#         tmp_list.append(train_Delivery_time[row])
#         tmp_list.append(train_area[row])
#         tmp_list.append(train_status[row])
#         tmp_list.append(train_behavior[row])
#         tmp_list.append(train_age[row])
#         tmp_list.append(train_gender[row])
#         tmp_list.append(train_education[row])
#         tmp_list.append(train_device[row])
#         tmp_list.append(train_consuptionAbility[row])
#         tmp_list.append(train_connectionType[row])
#         XList.append(tmp_list)
#     yList = data.num_click.values
#     return XList, yList
#
#
# def loadTestData(filePath):
#     data = pd.read_csv(filepath_or_buffer=filePath)
#     # 对不同的属性列使用不同编码方式 下列属性使用one-hot encoding的数据类型
#     att_ad_bid = LabelEncoder().fit_transform(data['ad_bid'].apply(int))
#     att_Ad_Industry_Id = LabelEncoder().fit_transform(data['Ad_Industry_Id'].apply(int))
#     att_Commodity_type = LabelEncoder().fit_transform(data['Commodity_type'].apply(int))
#     att_Ad_material_size = LabelEncoder().fit_transform(data['Ad_material_size'].apply(int))
#
#     # 开始处理多值属性 参考代码见
#     cv = CountVectorizer()
#     cv.fit(data['Delivery_time'])
#     train_Delivery_time = cv.transform(data['Delivery_time'])
#
#     cv.fit(data['area'])
#     train_area = cv.transform(data['area'])
#
#     cv.fit(data['status'])
#     train_status = cv.transform(data['status'])
#
#     cv.fit(data['behavior'])
#     train_behavior = cv.transform(data['behavior'])
#
#     cv.fit(data['age'])
#     train_age = cv.transform(data['age'])
#
#     cv.fit(data['gender'])
#     train_gender = cv.transform(data['gender'])
#
#     cv.fit(data['education'])
#     train_education = cv.transform(data['education'])
#
#     cv.fit(data['device'])
#     train_device = cv.transform(data['device'])
#
#     cv.fit(data['consuptionAbility'])
#     train_consuptionAbility = cv.transform(data['consuptionAbility'])
#
#     cv.fit(data['connectionType'])
#     train_connectionType = cv.transform(data['connectionType'])
#
#     data_num = len(data)
#     XList = []
#     for row in range(0, data_num):
#         tmp_list = []
#         tmp_list.append(att_ad_bid[row])
#         tmp_list.append(att_Ad_Industry_Id[row])
#         tmp_list.append(att_Commodity_type[row])
#         tmp_list.append(att_Ad_material_size[row])
#
#         # 以下属性为多值属性
#         tmp_list.append(train_Delivery_time[row])
#         tmp_list.append(train_area[row])
#         tmp_list.append(train_status[row])
#         tmp_list.append(train_behavior[row])
#         tmp_list.append(train_age[row])
#         tmp_list.append(train_gender[row])
#         tmp_list.append(train_education[row])
#         tmp_list.append(train_device[row])
#         tmp_list.append(train_consuptionAbility[row])
#         tmp_list.append(train_connectionType[row])
#         XList.append(tmp_list)
#         XList.append(tmp_list)
#     return XList
#
#
# def trainandTest(X_train, y_train, X_test):
#     # XGBoost训练过程
#     model = xgb.XGBRegressor(max_depth=6, learning_rate=0.05, n_estimators=500, silent=False, objective='reg:gamma')
#     model.fit(X_train, y_train)
#
#     # 对测试集进行预测
#     ans = model.predict(X_test)
#     ans_len = len(ans)
#     id_list = np.arange(1, len(ans) + 1)
#     data_arr = []
#
#     # 增加一个判断语句 判断标签和测试集中的长度是否相同 如果不同的话 则报错
#     if ans_len == len(id_list):
#         for row in range(0, ans_len):
#             data_arr.append([int(id_list[row]), ans[row]])
#     else:
#         print("！！！！！测试数据的长度和定义的标签长度不一致！！！！！")
#         sys.exit()
#
#     # 写入文件
#     np_data = np.array(data_arr)
#     pd_data = pd.DataFrame(np_data)
#     pd_data.to_csv('submission.csv', index=None, header=None)
#
#     # 显示重要特征
#     # plot_importance(model)
#     # plt.show()
#
#
# if __name__ == '__main__':
#     trainFilePath = '../data/dataset/result/train_dataset.csv'
#     testFilePath = '../data/dataset/result/Test_Sample_Data_all.csv'
#     print("=================正在加载数据集=============！")
#     data = pd.read_csv(trainFilePath)
#     print("训练集中的数据信息是:\n", data.info())
#
#     print("======================正在构建模型的特征=============")
#     X_train, y_train = featureSet(data)
#     print("=====================正在训练中====================")
#     X_test = loadTestData(testFilePath)
#     trainandTest(X_train, y_train, X_test)
#
