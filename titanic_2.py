
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

train1 = pd.read_csv('train.csv')

#Variable exploration
print(train1['Pclass'].describe())
print(train1['SibSp'].describe())
print(train1['Parch'].describe())
print(train1['Fare'].describe())
print(train1['Age'].describe())

# check distribution per variable (0.1 percentiles increments)
train1.quantile([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])

# Data conversion

#convert age into bands

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

#gender conversion

def gen_trans(i):
    if i == 'male':
        return 1
    elif i == 'female':
        return 0
    else:
        return 2

train1['Sex'] = train1['Sex'].apply(lambda x: gen_trans(x))

# SibSp and Parch conversion fn:
def band_sp(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i >= 2:
        return 2

train1['SibSp'] = train1['SibSp'].apply(lambda x: band_sp(x))
train1['Parch'] = train1['Parch'].apply(lambda x: band_sp(x))

# Fare conversion fn:
def band_fare(i):
    if i<8:
        return 1
    elif i >=8 and i < 15:
        return 2
    elif i >= 8 and i < 32:
        return 3
    elif i >= 32 and i < 75:
        return 4
    elif i <= 75:
        return 5

train1['Fare'] = train1['Fare'].apply(lambda x: band_fare(x))

print(train1.head(20))

#train2['Sex'] = train2['Sex'].astype('category').cat.codes

#train2['Embarked'] = train2['Embarked'].astype('category').cat.codes

#cat_dict = {}
#cat_dict['Sex'] = {}
#cat_dict['Embarked'] = {}
#for i in range(len(ip_data)):
#cat_dict['Sex'][df1.loc[i,'Sex']] = train2.loc[i, 'Sex']
#cat_dict['Embarked'][df1.loc[i,'Embarked']] = train2.loc[i, 'Embarked']

#train3 = train2.drop(['PassengerId', 'Name','Ticket', 'Cabin'],1)
#train = pd.DataFrame(train3).astype(float)
#scaler = MinMaxScaler()

#train_scaled = pd.DataFrame(scaler.fit_transform(train))

#print(train_scaled)
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