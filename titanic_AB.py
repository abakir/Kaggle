

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

train1 = pd.read_csv('train.csv').fillna(0)


def age_trans(data):
    Age = [float(age) for age in data['Age']]
    for i in Age:
        if i < 13:
            data.replace(i,1, inplace=True)
        elif i >= 13 and i < 18:
            data.replace(i,2, inplace=True)
        elif i >= 18 and i < 25:
            data.replace(i,3, inplace=True)
        elif i >= 25 and i < 35:
            data.replace(i,4, inplace=True)
        elif i >= 35 and i < 46:
            data.replace(i,5, inplace=True)
        elif i >= 46 and i < 56:
            data.replace(i,6, inplace=True)
        elif i >= 56 and i < 66:
            data.replace(i,7, inplace=True)
        else:
            data.replace(i,8, inplace=True)
    return data

age_train = age_trans(train1)
print(age_train.head(50))
print(train1['Age'].describe())

#
# train3 = train2.drop(['PassengerId','Name','Sex','Ticket', 'Cabin', 'Embarked'],1)
# train = pd.DataFrame(train3).astype(float)
#
# test1 = pd.read_csv('test.csv')
# test2 = test1.fillna(0)
#
# test3 = test2.drop(['PassengerId','Name','Sex','Ticket', 'Cabin', 'Embarked'], 1)
#
#
#
# scaler = MinMaxScaler()
#
#
# train_scaled = pd.DataFrame(scaler.fit_transform(train), columns=['Survived','Pclass','i','SibSp','Parch','Fare'])
#
# print(train_scaled.head(10))
#
# #Feature Selection
#
# # Check for correlation among variables and with target
#
# print(train_scaled.corr())