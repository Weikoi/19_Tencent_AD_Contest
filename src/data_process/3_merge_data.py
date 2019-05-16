
import pandas as pd

pd.set_option('display.max_columns', 20)

log_df = pd.read_csv('../../data/temp2/Total_Exposure_Log_Data_drop.csv')
static_df = pd.read_csv('../../data/temp2/Ad_Static_Feature_Data_drop.csv')

tran_df = log_df.merge(static_df)

tran_df.drop("Ad_Request_id", axis=1, inplace=True)
tran_df.drop("user_id", axis=1, inplace=True)
# tran_df.drop_duplicates(subset="ad_id", keep='first', inplace=True)
# print(tran_df)

Group_Exposure_Data = tran_df.groupby(
    ['ad_id']).size().reset_index()
Group_Exposure_Data = Group_Exposure_Data.rename(columns={0: 'num_click'})
# print("按照年月日 广告id和广告竞价进行分组之后的数据是:\n", Group_Exposure_Data)

final_df = pd.merge(tran_df, Group_Exposure_Data, how='inner')

print(final_df)
final_df.to_csv('../../data/temp2/final_train.csv', index=False)


