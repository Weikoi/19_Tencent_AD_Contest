import pandas as pd

test_sampledf = pd.DataFrame(
    pd.read_csv('../../data/raw/Btest_sample_new.dat ', sep='\t',
                header=None,
                names=['样本id', '广告id', '创建时间', '素材尺寸', '广告行业id', '商品类型', '商品id', '广告账户id', '投放时间', '人群定向', '出价'],
                usecols=['样本id', '广告id', '出价']))
test_sampledf['曝光'] = (
            (test_sampledf['出价'].groupby(test_sampledf['广告id']).rank(ascending=1, method='dense')) / 7.33).round(decimals=4)
test_sampledf.to_csv("submission.csv", sep=",",
                     index=False, encoding="utf-8", header=None, columns=["样本id", "曝光"])
