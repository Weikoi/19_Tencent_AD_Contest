import pandas as pd
import sys
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

pd.set_option('display.max_columns', 20)


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


trainFilePath = '../data/dataset/result/train_dataset.csv'
testFilePath = '../data/dataset/result/test_sample_data_all.csv'
print("================== 正在加载数据集 ==================")
data = loadDataset(trainFilePath)
# X_test = loadTestData(testFilePath)


print("================== 正在构建数据特征 ===============")
X, y = featureSet(data)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train 占用内存大小为：", round(sys.getsizeof(X_train) / 1024 / 1024, 2), "MB")


print("================== 正在构建模型 ================")
"""
选择训练模型
"""

model = 'rf'

"""
随机森林 单次验证 score 0.3078
"""
if model == 'rf':

    rnd_clf = RandomForestClassifier(n_estimators=1000, max_leaf_nodes=16, n_jobs=-1)
    rnd_clf.fit(X_train, y_train)
    y_pred_rf = rnd_clf.predict(X_test)

    print("RandomForest:", accuracy_score(y_test, y_pred_rf))

    for score in rnd_clf.feature_importances_:
        print(score)

"""
ada boost grid search 五折交叉 内存溢出
"""
# if mode == 'ada_gs':
#     ada_clf = AdaBoostClassifier(
#         DecisionTreeClassifier(max_depth=3), algorithm="SAMME.R", n_estimators=1000, learning_rate=.7
#     )
#
#     param_grid = {"learning_rate": [i / 10 for i in range(1, 11)],
#                   "n_estimators": [i for i in range(200, 1100, 100)]}  # 转化为字典格式，网络搜索要求
#
#     grid_search = GridSearchCV(ada_clf, param_grid, cv=5, n_jobs=-1)
#     grid_result = grid_search.fit(X_train, y_train)
#
#     print("Best: %f using %s" % (grid_result.best_score_, grid_search.best_params_))
#     print("Test set score:{:.4f}".format(grid_search.score(X_test, y_test)))

"""
ada boost 单次验证
"""
if model == 'ada':
    ada_clf = AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=3), algorithm="SAMME.R", n_estimators=1000, learning_rate=.7
    )

    ada_clf.fit(X_train, y_train)
    y_pred_ada = ada_clf.predict(X_test)

    print("ada boost:", accuracy_score(y_test, y_pred_ada))
