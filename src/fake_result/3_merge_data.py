import datetime
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 20)

log_df = pd.read_csv('../../data/temp2/Total_Exposure_Log_Data.csv')
static_df = pd.read_csv('../../data/temp2/Ad_Static_Feature_Data_drop.csv')


# 给 log pd 生成月日标签
tfa = log_df.Ad_Request_Time.astype(str).apply(lambda x: datetime.datetime(int(x[:4]),
                                                                           int(x[5:7]),
                                                                           int(x[8:10]),
                                                                           int(x[11:13]),
                                                                           int(x[14:16]),
                                                                           int(x[17:])))

log_df['tfa_month'] = np.array([x.month for x in tfa])
log_df['tfa_day'] = np.array([x.day for x in tfa])

tran_df = log_df.merge(static_df)

tran_df.drop("Ad_Request_id", axis=1, inplace=True)
tran_df.drop("user_id", axis=1, inplace=True)


Group_Exposure_Data = tran_df.groupby(
    ['tfa_month', 'tfa_day', 'ad_id', 'Ad_bid']).size().reset_index()
Group_Exposure_Data = Group_Exposure_Data.rename(columns={0: 'num_click'})
# print("按照年月日 广告id和广告竞价进行分组之后的数据是:\n", Group_Exposure_Data)

final_df = pd.merge(tran_df, Group_Exposure_Data, how='inner')
# 删除可能重复的元素
# final_df.drop_duplicates(subset="ad_id", keep='first', inplace=True)


print(final_df)
final_df.to_csv('../../data/temp2/final_train.csv', index=False)

final_df = pd.read_csv('../../data/temp2/final_train.csv')

final_df.drop('tfa_month', axis=1, inplace=True)
final_df.drop('tfa_day', axis=1, inplace=True)
final_df.drop('Ad_Request_Time', axis=1, inplace=True)
final_df.drop('ad_id', axis=1, inplace=True)
final_df.drop('Ad_account_id', axis=1, inplace=True)
final_df.drop('Commodity_id', axis=1, inplace=True)
final_df.drop('Commodity_type', axis=1, inplace=True)
final_df.drop('Ad_Industry_Id', axis=1, inplace=True)
final_df.drop('Ad_material_size', axis=1, inplace=True)

final_df.to_csv('../../data/temp2/final_train_drop.csv', index=False)
