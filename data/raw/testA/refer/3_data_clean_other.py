# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:49
# @Author  : YYLin
# @Email   : 854280599@qq.com
# @File    : Dataload_Ad_Data.py
import pandas as pd
import time

# 当load_ad值为 Static_Ad 表示清洗的是静态数据集
load_ad = 'Static_Ad'

if load_ad == 'Static_Ad':
    # 将静态广告(ad_static_feature)转化成csv格式 对于创建时间这一列的数据集没有转化时间 待做 未完成
    # 19-04-19 已经将静态广告数据中的时间戳转化成对应的时间
    Ad_Static_Feature_Data = []

    # 定义曝光日志中的相关列
    Ad_Static_Feature_Data_columns = ['ad_id', 'Creation_time', 'Ad_account_id', 'Commodity_id', 'Commodity_type',
                                      'Ad_Industry_Id', 'Ad_material_size']

    # 为数据集增加列名称
    Ad_Static_Feature_Data.append(Ad_Static_Feature_Data_columns)
    with open('../Dataset/tencent-dataset-19/ad_static_feature.out', 'r') as f:
        for i, line in enumerate(f):
            # print(i, ':', line,'\n', len(line), type(line))
            line = line.strip().split('\t')
            # print(i, ':', line,  '\n', type(line), len(line))
            # print('每一个元素的取值类型: ', type(line[1]), type(line[2]), type(line[3]), type(line[4]))

            # 测试数据集的时候使用
            # if i > 1000:
            # break

            # 分别用于判断该条广告数据是否存在记录缺失 是否创建时间为0 广告行业是否存在多值
            if line[1] == '0':
                # print("数据集中创建时间为0的数据集是: ", line)
                continue
            if ',' in line[5]:
                # print("数据集中广告行业ID存在多值记录是: ", line)
                continue
            if len(line) != 7:
                # print("广告数据集中出现缺失数据: ", line)
                continue

            # 4-19新加该功能 静态广告时间的格式是2018/6/26 4:35:50
            # print(line[1], type(line[1]), line)
            loacl_time = int(line[1])
            time_local = time.localtime(loacl_time)
            line[1] = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

            Ad_Static_Feature_Data.append(line)
    print("***********userFeature_data[0]:\n", Ad_Static_Feature_Data[1])
    print("***********userFeature_data[0][1]:\n", Ad_Static_Feature_Data[1][0])

    user_feature = pd.DataFrame(Ad_Static_Feature_Data)
    user_feature.to_csv('../Dataset/tencent-dataset-19/dataset-for-train/Ad_Static_Feature_Data.csv', index=False,
                        header=False)

    '''
    # 使用pandas删除不需要的列元素 测试完成 暂时不使用
    remove_data = pd.read_csv('../Dataset/tencent-dataset-19/dataset-for-train/Ad_Static_Feature_Data_redo.csv')
    print(remove_data.info())
    remove_data = remove_data.drop(['Ad_account_id'], axis=1)
    remove_data = remove_data.drop(['Commodity_id'], axis=1)
    remove_data.to_csv('../Dataset/tencent-dataset-19/dataset-for-train/Ad_Static_Feature_Data_redo.csv', index=False)
    '''
else:
    import linecache
    import sys
    # 用于将二维数组转化成一维数组
    import operator
    from functools import reduce


    def get_next_line(i_row):
        line = linecache.getline('../Dataset/tencent-dataset-19/ad_operation.dat', (i_row))
        line = line.strip().split('\t')
        # print("当前数据行的值是:", line)

        line_next = linecache.getline('../Dataset/tencent-dataset-19/ad_operation.dat', (i_row + 1))
        line_next = line_next.strip().split('\t')

        return line_next


    # 读取静态广告数据集中的广告ID将其转化成list数据
    Exposure_Log_Data = pd.read_csv('data/Ad_Static_Feature_Data.csv')

    Ad_id_in_static = Exposure_Log_Data['ad_id']
    Ad_time_in_static = Exposure_Log_Data['Creation_time']
    # print("静态广告数据集中的广告id和时间分别是:\n", Ad_id_in_static.head(5), '\n', Ad_time_in_static.head(5))

    # 保存静态广告中广告ID和对应的时间  注意时间类型是str()
    list_Ad_id_in_static = list(Ad_id_in_static)
    # print('静态广告数据集中广告ID的取值和数据类型分别是：',
    # len(list_Ad_id_in_static), list_Ad_id_in_static[0:5], type(list_Ad_id_in_static[0]))
    list_Ad_time_in_static = list(Ad_time_in_static)

    # print('静态广告数据集中创建时间的取值和数据类型分别是：', len(list_Ad_time_in_static), list_Ad_time_in_static[0:5],
    # type(list_Ad_time_in_static[0]))

    # 将广告操作对应的数据集(ad_operation.dat)进行清洗 清洗的内容包括一下几个部分
    Ad_Operation_Data = []
    # 定义操作数据对应的序列
    Ad_Operation_Data_columns = ['ad_id', 'Create_modify_time', 'ad_bid', 'Chose_People', 'Delivery_time']

    # 为数据集增加列名称
    Ad_Operation_Data.append(Ad_Operation_Data_columns)

    All_kind_ad = []
    with open('../Dataset/tencent-dataset-19/ad_operation.dat', 'r') as f:
        for i, line in enumerate(f):
            # print(i, ':', line, '\n', len(line), type(line))
            line = line.strip().split('\t')
            # print(i, ':', line, '\n', len(line), type(line[2]))

            if (i % 10000) == 0:
                print("***********我已经执行了%d行" % (i))

            # 首先需要判断该条数据是否在静态数据集之中 不存在则删除
            if int(line[0]) not in list_Ad_id_in_static:
                # print("*******该条数据不存在于静态数据集之中，需要删除*******", line)
                continue

            # 使用line[2]修改广告操作数据集中的时间选项 并进行保存 验证成功
            if '20190230' in line[1]:
                # print('数据集中出现2月30号的数据已删除', line)
                continue

            # 首先需要广告操作数据集中的训练时间
            if len(line[1]) == 14:
                data_list = list(line[1])
                data_list.insert(4, '-')
                data_list.insert(7, '-')
                data_list.insert(10, ' ')
                data_list.insert(13, ':')
                data_list.insert(16, ':')
                line[1] = ''.join(data_list)
                # print(line[1])

            if line[2] == '2':
                # 修改广告的操作时间
                ad_id_index = list_Ad_id_in_static.index(int(line[0]))
                line[1] = list_Ad_time_in_static[ad_id_index]

                # 修改曝光广告位置的值
                All_kind_ad.append(line[4])
                list_next_data = get_next_line(i + 1)

                if list_next_data[2] == '1':
                    tmp_value_ad_list = '?'.join(All_kind_ad)
                    tmp_value_ad_list = tmp_value_ad_list.strip().split('?')
                    # print("tmp_value_ad_list中的值是:\n", tmp_value_ad_list)
                    line = line[0:2]
                    line.append(tmp_value_ad_list[0])
                    line.append(tmp_value_ad_list[1])
                    line.append(tmp_value_ad_list[2])
                    All_kind_ad = []
                elif list_next_data[2] == '2' and list_next_data[0] != line[0]:
                    tmp_value_ad_list = '?'.join(All_kind_ad)
                    tmp_value_ad_list = tmp_value_ad_list.strip().split('?')
                    line = line[0:2]
                    line.append(tmp_value_ad_list[0])
                    line.append(tmp_value_ad_list[1])
                    line.append(tmp_value_ad_list[2])
                    All_kind_ad = []
                else:
                    continue
            elif line[2] == '1':
                continue

            else:
                print("广告操作类型既不是新建，也不是修改，:\n", line)
                sys.exit()

            Ad_Operation_Data.append(line)

            # if i >= 100:
            # break
            # sys.exit()
    # print("***********use Feature_data[0]:\n", Ad_Operation_Data[9])
    # print("***********userFeature_data[0][1]:\n", Ad_Operation_Data[9][1])

    Ad_Operation_Data = pd.DataFrame(Ad_Operation_Data)
    Ad_Operation_Data.to_csv('data/Ad_Operation_Data.csv', index=False, header=False)
