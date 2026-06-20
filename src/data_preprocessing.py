import pandas as pd

def load_data(path):
    df = pd.read_csv(path, sep=";")
    return df

def get_features_and_target(df, use_grades=True):
    if use_grades:
        features = ["studytime", "failures", "absences", "G1", "G2"]
    else:
        features = ["studytime", "failures", "absences"]
    
    X = df[features]
    y = df["G3"]
    return X,y

