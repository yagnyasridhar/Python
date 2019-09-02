import pandas as pd
import numpy as nu
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split

def importDS(path):
    ds = pd.read_csv(path)
    return ds

ds = importDS("Social_Network_Ads.csv")
x = ds.iloc[:,1:4].values
y = ds.iloc[:,4].values

def split(x,y):
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state = 0)
    return xtrain, xtest, ytrain, ytest

def Encoder(x):
    lbl = LabelEncoder()
    x[:,0] = lbl.fit_transform(x[:,0])
    onehten = OneHotEncoder()
    x[:,0] = onehten.transform(x[:,0])
    return x[:,0]

def scaleDataX(x):
    std = StandardScaler()
    x = std.fit_transform(x)
    return x

def scaleDataY(y):
    std = StandardScaler()
    y = std.transform(y)
    return y

xtrain, xtest, ytrain, ytest = split(x,y)

xtrain[:,0] = Encoder(xtrain)
xtest[:,0] = Encoder(xtest)

xtrain = scaleDataX(xtrain)
xtest = scaleDataX(xtest)

from sklearn.svm import SVC

regression = SVC(random_state = 0, kernel='rbf')
regression.fit(xtrain,ytrain)

ypred = regression.predict(xtest)

cf = confusion_matrix(ytest, ypred)
cf