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

install.packages("rpart")
library(rpart)

regression = rpart(formula = ds$Salary ~., data = ds, control = rpart.control(minsplit = 1))
ypred = predict(regression, data.frame(Level = (6.5)))
ypred