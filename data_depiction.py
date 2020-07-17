import pandas as pd
import matplotlib as mp

filename = 'diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filename)#, names=names)
#data.drop(data.index[0], inplace=True)
description = data.describe()
correlations = data.corr(method='pearson')
class_counts = data.groupby('Outcome').size()
data.hist(figsize=(12,12))
mp.pyplot.tight_layout()
mp.pyplot.show()
#print(class_counts)
#print(correlations)
#print(data.shape)
#print(data)
#print(description)
