import csv
import copy
def load_csv(filename):
    # from csv import reader
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset
dataset = load_csv('diabetes.csv')
print('Loaded data file {0} with {1} rows and {2} columns'.format('diabetes.csv', len(dataset),len(dataset[0])))
def str_column_to_float(dataset, index):
    for i in range(1,len(dataset)):
        dataset[i][index]=float(dataset[i][index].strip())
    return dataset
dataset_new=copy.deepcopy(dataset)
for i in range(len(dataset_new[0])):
    dataset_new=str_column_to_float(dataset_new,i)
print(dataset_new[1])
