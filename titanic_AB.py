


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

train1 = pd.read_csv('train.csv')
train2 = train1.fillna(0)

train3 = train2.drop(['Name','Sex','Ticket', 'Cabin', 'Embarked'],1)
train = pd.DataFrame(train3).astype(float)

test1 = pd.read_csv('test.csv')
test2 = test1.fillna(0)

test3 = test2.drop(['Name','Sex','Ticket', 'Cabin', 'Embarked'], 1)


scaler = MinMaxScaler()


train_scaled = pd.DataFrame(scaler.fit_transform(train))

print(train_scaled.head(10))
