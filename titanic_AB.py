

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

train1 = pd.read_csv('train.csv').fillna(0)

def age_trans(i):
        if i < 13:
            return 1
        elif i >= 13 and i < 18:
            return 2
        elif i >= 18 and i < 25:
            return 3
        elif i >= 25 and i < 35:
            return 4
        elif i >= 35 and i < 46:
            return 4
        elif i >= 46 and i < 56:
            return 6
        elif i >= 56 and i < 66:
            return 7
        else:
            return 8

        
train1['Age'] = train1['Age'].apply(lambda x: age_trans(x))

#age_train = age_trans(train1)
#print(age_train.head(50))
#print(train1['Age'].describe())

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