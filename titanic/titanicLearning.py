import numpy as np # linear algebra
import pandas as pd # data processing

train_data = pd.read_csv("/kaggle/input/titanic/train.csv")
train_data.head()
test_data = pd.read_csv(("/kaggle/input/titanic/test.csv"))

men = train_data.loc[train_data.Sex=='male']["Survived"]
rate_men = sum(men)/ len(men)
print(rate_men)

women = train_data.loc[train_data.Sex=='female']["Survived"]
rate_women = sum(women)/len(women)
print(rate_women)
