from random import seed
from random import randrange
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
class Data:
    '''divides dataset into two batches. One for training. One for testing.'''
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.train_batch = []
        self.test_batch = []
    def divide_dataset(self, train_perc=0.8):
        train_size = train_perc * len(self.dataframe)
        self.test_batch = list(self.dataframe)
        while len(self.train_batch) < train_size:
            index = randrange(len(self.test_batch))
            self.train_batch.append(self.test_batch.pop(index))
'''dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
my_data = Data(dataset)
my_data.divide_dataset(0.8)
print(f' Training batch: {my_data.train_batch} \n Testing Batch: {my_data.test_batch}')'''
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataset1=pd.read_csv('diabetes.csv',names=names)
dataset = dataset1.iloc[1:]
dataset = dataset.astype(float)
class_count=dataset['class'].value_counts()
negative_count = class_count[0]
positive_count = class_count[1]
total_ratio = positive_count/negative_count
print(f'Diabetic count : {positive_count} \nNon-diabetic count : {negative_count} \nDiabetic / non-diabetic ratio : {total_ratio}')
train, test = train_test_split(dataset, test_size=0.25, random_state=41, stratify=dataset['class'])
print(f'Number of elements in train set: {len(train)} \nNumber of elements in test set: {len(test)}')
thickest_arm = dataset['skin'].idxmax()
print(f'The patient number with thickest arm: {thickest_arm}')
outcome_train = train['class'].value_counts()
negative_train = outcome_train[0]
positive_train = outcome_train[1]
outcome_test = test['class'].value_counts()
negative_test = outcome_test[0]
positive_test = outcome_test[1]
print(f'Train set positive/negative ratio: {positive_train/len(train)}\nTest set positive/negative ratio: {positive_test/len(test)}')
#print(dataset)


