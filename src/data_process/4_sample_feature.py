import pandas as pd

Test_Sample_Data = []
Test_Sample_Data_columns = ['ad_id', 'Ad_material_size', 'Ad_bid', 'Ad_account_id', 'Commodity_id',
                            'Commodity_type', 'Ad_Industry_Id']
with open('../../data/raw/Btest_sample_new.dat', 'r') as f:
    for i, line in enumerate(f):
        save_line = []
        line = line.strip().split('\t')
        # print("line:", line, '\n', 'line[9]:', line[9], type(line))
        print(len(line))
        save_line.append(eval(line[1]))
        save_line.append(eval(line[3]))
        save_line.append(eval(line[-1]))
        save_line.append(eval(line[-4]))
        save_line.append(eval(line[-5]))
        save_line.append(eval(line[-6]))
        save_line.append(eval(line[-7]))

        #
        Test_Sample_Data.append(save_line)
        # if i == 2:
        #     print("=========最后用于保存结果的数据格式是:======\n", Test_Sample_Data[3][10], '\n', len(Test_Sample_Data[3][10]))

user_feature = pd.DataFrame(Test_Sample_Data)
print(user_feature.info())
user_feature.to_csv('../../data/temp2/test_sample_data.csv', index=False, header=Test_Sample_Data_columns)
