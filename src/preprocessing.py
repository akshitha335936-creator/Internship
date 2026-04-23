import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    return data

def preprocess(data):
    X = data[['age', 'income', 'tenure']]
    y = data['churn']
    return X, y