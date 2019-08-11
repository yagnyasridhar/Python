import pandas as pd
import numpy as nu
import matplotlib as mt

ds = pd.read_csv("Position_Salaries.csv")
x = ds.iloc[:,1:2].values
y = ds.iloc[:,3].values

from sklearn.tree import DecisionTreeClassifier 
classifier = DecisionTreeClassifier(random_state=0)
classifier.fit(x,y)
classifier.predict(6.5)
