import numpy as np
import pandas as pd


url = "https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/csv/bdfc59ed-c3c7-48ac-a3d3-9e54663f6c1d" \
      ".csv "
train = pd.read_csv(url)
for name in train.columns:
    x = train[name].isna().sum()
    if x > 0:
        val_list = np.random.choice(train.groupby(name).count().index, x,
                                    p=train.groupby(name).count()['Id'].values / sum(
                                        train.groupby(name).count()['Id'].values))
        train.loc[train[name].isna(), name] = val_list
train_2 = train[['SalePrice', 'OverallQual', 'YearRemodAdd', 'MasVnrArea']]
train_2['MasVnrArea']=train_2['MasVnrArea'].replace(0.0,train_2['MasVnrArea'].mean())




