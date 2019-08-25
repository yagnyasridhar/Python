ds =read.csv("Position_Salaries.csv")
install.packages("caTools")
library(caTools)
set.seed(123)
ds = ds[2:3]

split.Function = function(ds)
{
  split = sample.split(ds, SplitRatio = 0.70)
  train = subset(split, TRUE)
  test = subset(split, FALSE)
}

install.packages("randomForest")
library(randomForest)

x = data.frame(ds$Level)
y = data.frame(ds$Salary)

regression = randomForest(x = x,y = ds$Salary, ntree=100)
ypred = predict(regression, 6.5)
ypred