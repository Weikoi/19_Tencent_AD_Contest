# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 9:11
# @Author  : YYLin
# @Email   : 854280599@qq.com
# @File    : Code_For_Tencent.py
import pandas as pd

import xgboost as xgb
import numpy as np
import sys
import matplotlib.pyplot as plt
from xgboost import plot_importance
from sklearn.preprocessing import Imputer

pd.set_option('precision', 4)


def loadDataset(filePath):
    df = pd.read_csv(filepath_or_buffer=filePath)
    return df


def featureSet(data):
    data_num = len(data)
    XList = []
    for row in range(0, data_num):
        tmp_list = []
        tmp_list.append(data.iloc[row]['ad_bid'])
        tmp_list.append(data.iloc[row]['Ad_material_size'])
        tmp_list.append(data.iloc[row]['Ad_Industry_Id'])
        tmp_list.append(data.iloc[row]['Commodity_type'])

        # 该参数用来表示投放时间 暂时不使用
        # tmp_list.append(data.iloc[row]['Delivery_time'])
        XList.append(tmp_list)
    yList = data.num_click.values
    return XList, yList


def loadTestData(filePath):
    data = pd.read_csv(filepath_or_buffer=filePath)
    data_num = len(data)
    XList = []
    for row in range(0, data_num):
        tmp_list = []
        tmp_list.append(data.iloc[row]['ad_bid'])
        tmp_list.append(data.iloc[row]['Ad_material_size'])
        tmp_list.append(data.iloc[row]['Ad_Industry_Id'])
        tmp_list.append(data.iloc[row]['Commodity_type'])

        # 该参数用来表示投放时间 暂时不使用
        # tmp_list.append(data.iloc[row]['Delivery_time'])
        XList.append(tmp_list)
    return XList


def trainandTest(X_train, y_train, X_test):
    # XGBoost训练过程
    model = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_jobs=-1, n_estimators=160, silent=False,
                             objective='reg:gamma')
    model.fit(X_train, y_train)

    # 对测试集进行预测 并且对预测结果保留四位有效数字
    ans = model.predict(X_test)
    print(ans)

    ans_len = len(ans)
    id_list = np.arange(1, ans_len + 1)
    data_arr = []

    # 如果预测的数据长度和定义的数据长度一致 则将其合并保存
    if ans_len == len(id_list):
        for row in range(0, ans_len):
            data_arr.append([int(id_list[row]), round(ans[row], 4)])
            # print(data_arr)
    else:
        print("！！！！！测试数据的长度和定义的标签长度不一致！！！！！")
        sys.exit()

    # np_data = np.array(data_arr)
    # 保存结果
    pd_data = pd.DataFrame(data_arr)
    # print(pd_data)
    pd_data.to_csv('submission.csv', index=None, header=None)

    # 显示重要特征
    # plot_importance(model)
    # plt.show()


if __name__ == '__main__':
    trainFilePath = '../data/dataset/result/train_dataset.csv'
    testFilePath = '../data/dataset/result/Test_Sample_Data_all.csv'
    print("==================正在加载数据集==================")
    data = loadDataset(trainFilePath)
    # print("训练集中的数据信息是:\n", data.info())
    X_test = loadTestData(testFilePath)

    print("==================正在构建模型的特征===============")
    X_train, y_train = featureSet(data)
    for i in range(len(X_train)):
        print(y_train[i])
    # print(X_train)
    # print()
    # print(y_train)
    print("==================正在训练中======================")
    trainandTest(X_train, y_train, X_test)
