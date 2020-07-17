import pandas as pd
import matplotlib as mp
def dataset_minmax(dataset):
    #print(data.loc['Outcome'])
    min_max_list = []
    for column in dataset.columns[:]:
        max_value = max(dataset[column])
        min_value = min(dataset[column])
        min_max_tuple = (max_value, min_value)
        min_max_list.append(min_max_tuple)
    return min_max_list
def normalize_dataset(dataset, minmax):
    normalized_data = []
    normalized_row = [0,0,0,0,0,0,0,0,0]
    for row in range(len(dataset)):
        for i in range(len(dataset.columns)):
            normalized_row[i] = float(dataset.iloc[row,i]-minmax[i][1])/(minmax[i][0]-minmax[i][1])
        normalized_data.append(normalized_row)
    return normalized_data
def load_normalized_csv(filename):
    dataset = pd.read_csv(filename)
    minmax_list = dataset_minmax(dataset)
    normalized_data = normalize_dataset(dataset,minmax_list)
    return normalized_data
def standardize(df, label):
    """
    standardizes a series with name ``label'' within the pd.DataFrame
    ``df''.
    """
    df = df.copy(deep=True)
    series = df.loc[:, label]
    avg = series.mean()
    stdv = series.std()
    series_standardized = (series - avg)/ stdv
    return series_standardized
normalized_data = load_normalized_csv('diabetes.csv')
names = ['Pregnancies', 'Glucose', 'BloodPres', 'Skin Thickness', 'Insulin', 'BMI', 'DiabPedigreeFunc', 'Age', 'Class']
normalized_dataframe = pd.DataFrame(normalized_data, columns=names)
print(normalized_dataframe)
def load_standardized_csv(filename):
    data = pd.read_csv('diabetes.csv')
    standardized_dataframe = pd.DataFrame(columns=data.columns)
    for name in data.columns:
        standardized_series = standardize(data,name)
        standardized_dataframe[name] = standardized_series
    return standardized_dataframe
'''standardized_data = load_standardized_csv('diabetes.csv')
standardized_data.hist()
mp.pyplot.show()'''