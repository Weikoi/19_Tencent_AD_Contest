import pandas as pd
import numpy as np

# user_feature = pd.read_csv('../../data/temp2/test_sample_data.csv')
#
test_data = pd.read_csv("../../data/temp2/final_train_drop.csv")
test_data.drop('ad_id', axis=1, inplace=True)
test_data.drop('Ad_account_id', axis=1, inplace=True)
test_data.drop('Commodity_id', axis=1, inplace=True)
test_data.drop('Commodity_type', axis=1, inplace=True)
test_data.drop('Ad_Industry_Id', axis=1, inplace=True)
test_data.drop('Ad_material_size', axis=1, inplace=True)
print(test_data)
# test_data.to_csv("../../data/temp2/fake_train.csv")
#
# print(sorted(test_data['num_click']))

# print(user_feature['Ad_bid'])
# user_feature['num_click'] = user_feature['Ad_bid']
#
# df = pd.DataFrame(np.random.rand(38596, 2))
# df[0] = [i for i in range(1, 38597)]
# df[1] = [round(i, 4) for i in user_feature['Ad_bid']]
# print(df)
# df.to_csv("submission.csv", index=False, header=False, float_format='%.4f')
