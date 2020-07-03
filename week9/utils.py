import pandas as pd

def load_data():
    df = pd.read_csv("iris.csv")
    return df