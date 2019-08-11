import pandas as pd
import numpy as nu
import matplotlib as mt

ds = pd.read_csv("Position_Salaries.csv")
x = ds.iloc[:,1:2].values
y = ds.iloc[:,2].values

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(x,y)
regressor.predict(6.5)
ypred = regressor.predict(x)

import sklearn.metrics as metric
acc = metric.r2_score(y,ypred)
acc