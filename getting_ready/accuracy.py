from sklearn import model_selection as ms
from sklearn import linear_model as lm
import pandas as pd
import numpy as np
import random
filename = 'diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=names)
dataframe.drop(dataframe.index[0], inplace=True)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
kfold = ms.StratifiedKFold(n_splits=10, random_state=7, shuffle=True)
model = lm.LogisticRegression(solver='liblinear')
results = ms.cross_val_score(model, X, Y, cv=kfold)
print(results)
