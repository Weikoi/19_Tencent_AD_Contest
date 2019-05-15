import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from xgboost import plot_importance
import xgboost as xgb
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
    new_df = data.drop("num_click", axis=1)
    XList = new_df
    yList = data.num_click.values
    return XList, yList


def loadTestData(filePath):
    data = pd.read_csv(filepath_or_buffer=filePath)

    return data


trainFilePath = '../../data/temp2/final_train.csv'
testFilePath = '../../data/temp2/test_sample_data.csv'
print("================== 正在加载数据集 ==================")
data = loadDataset(trainFilePath)
X_sample = loadTestData(testFilePath)

print("================== 正在构建数据特征 ===============")
X, y = featureSet(data)

# print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print("X_train 占用内存大小为：", round(sys.getsizeof(X_train) / 1024 / 1024, 2), "MB")


print("================== 正在构建模型 ================")
"""
选择训练模型
"""

model = 'xgb'

"""
随机森林 单次验证 score 0.7678
"""
if model == 'rf':
    rnd_clf = RandomForestClassifier(n_estimators=1200, max_leaf_nodes=38, n_jobs=-1)
    rnd_clf.fit(X_train, y_train)
    y_pred_rf = rnd_clf.predict(X_sample)
    print(len(y_pred_rf))

    df = pd.DataFrame(np.random.rand(20290, 2))
    df[0] = [i for i in range(1, 20291)]
    df[1] = y_pred_rf
    print(df)
    df.to_csv("submission.csv", index=False, header=False)
    # print("RandomForest:", accuracy_score(y_test, y_pred_rf))
    #
    # for score in rnd_clf.feature_importances_:
    #     print(score)

"""
随机森林 grid search 五折交叉
Best: 0.762338 using {'max_leaf_nodes': 38, 'n_estimators': 1200}
"""
if model == 'rf_gs':
    rnd_clf = RandomForestClassifier(n_jobs=-1)
    param_grid = {"max_leaf_nodes": [i for i in range(6, 40, 2)],
                  "n_estimators": [i for i in range(200, 2000, 200)]}  # 转化为字典格式，网络搜索要求

    grid_search = GridSearchCV(rnd_clf, param_grid, cv=5, n_jobs=-1)
    grid_result = grid_search.fit(X_train, y_train)

    rnd_clf.fit(X_train, y_train)
    y_pred_rf = rnd_clf.predict(X_test)
    print("RandomForest:", accuracy_score(y_test, y_pred_rf))

    for score in rnd_clf.feature_importances_:
        print(score)
    print("Best: %f using %s" % (grid_result.best_score_, grid_search.best_params_))
    print("Test set score:{:.4f}".format(grid_search.score(X_test, y_test)))

"""
ada boost grid search 五折交叉
Best: 0.684740 using {'learning_rate': 0.1, 'n_estimators': 200}
"""
if model == 'ada_gs':
    ada_clf = AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=3), algorithm="SAMME.R", n_estimators=1000, learning_rate=.7
    )

    param_grid = {"learning_rate": [i / 10 for i in range(1, 11)],
                  "n_estimators": [i for i in range(200, 1100, 100)]}  # 转化为字典格式，网络搜索要求

    grid_search = GridSearchCV(ada_clf, param_grid, cv=5, n_jobs=-1)
    grid_result = grid_search.fit(X_train, y_train)

    print("Best: %f using %s" % (grid_result.best_score_, grid_search.best_params_))
    print("Test set score:{:.4f}".format(grid_search.score(X_test, y_test)))

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

"""
xg boost 单次验证
"""
if model == 'xgb':
    xg_model = xgb.XGBRegressor(max_depth=9, learning_rate=0.3, n_jobs=-1, n_estimators=300, silent=False,
                                objective='reg:gamma')
    xg_model.fit(X_train, y_train)
    y_pred_xg = xg_model.predict(X_sample)
    print(len(y_pred_xg))
    df = pd.DataFrame(np.random.rand(20290, 2))
    df[0] = [i for i in range(1, 20291)]
    df[1] = y_pred_xg
    print(df)
    df.to_csv("submission.csv", index=False, header=False)

    # 显示重要特征
    # plot_importance(xg_model)
    # plt.show()

"""
xg boost 五折交叉
Best: 0.953996 using {'learning_rate': 0.3, 'max_depth': 9, 'n_estimators': 300}
"""
if model == 'xgb_gs':
    xg_model = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_jobs=-1, n_estimators=1000, silent=False,
                                objective='reg:gamma')

    param_grid = {
        "max_depth": [i for i in range(3, 10)],
        "learning_rate": [i / 10 for i in range(1, 11, 2)],
        "n_estimators": [i for i in range(200, 1100, 100)]}  # 转化为字典格式，网络搜索要求

    grid_search = GridSearchCV(xg_model, param_grid, cv=5, n_jobs=-1)
    grid_result = grid_search.fit(X_train, y_train)

    # xg_model.fit(X_train, y_train)
    # y_pred_xg = xg_model.predict(X_test)
    #
    # print("xg boost:", accuracy_score(y_test, y_pred_xg))
    print("Best: %f using %s" % (grid_result.best_score_, grid_search.best_params_))
    print("Test set score:{:.4f}".format(grid_search.score(X_test, y_test)))
    # 显示重要特征
    # plot_importance(model)
    # plt.show()
