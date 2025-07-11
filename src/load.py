import pandas as pd

def load_data(path="DataSet.csv"):
    df = pd.read_csv(path)
    return df
