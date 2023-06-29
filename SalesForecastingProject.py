# pip install upgini catboost
from os.path import exists
import pandas as pd
df_path = "train.csv.zip" if exists('train.csv.zip') else "https://github.com/upgini/upgini/raw/main/notebooks/train.csv.zip"
df = pd.read_csv(df_path)
print(df.head())
df = df.sample(n=19_000,random_state=0)
df['store'] = df['store'].astype(str)
df['item'] = df['item'].astype(str)
df['date'] = pd.to_datetime(df['date'])
df.sort_values("date",inplace=True)
df.reset_index(inplace=True,drop=True)
print(df.head(10))
print('Spliting data set to train and testing based on yearwise')
train = df[df['date'] < "2017-01-01"]
test  = df[df['date'] >= "2017-01-01"]
train_features = train.drop(columns=["sales"])
train_target = train['sales']

test_features = test.drop(columns=["sales"])
test_target = test['sales']

from upgini import FeaturesEnricher,SearchKey
from upgini.metadata import CVType
#pip install numpy==1.21 Got some error to avoid that error numpy version is used.

enricher = FeaturesEnricher(
    search_keys={'date': SearchKey.DATE},
       cv = CVType.time_series
)

enricher.fit(train_features,train_target,eval_set=[(test_features,test_target)])



