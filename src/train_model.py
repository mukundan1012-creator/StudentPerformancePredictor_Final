from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
import joblib
from data_preprocessing import load_data, get_features_and_target
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def train_and_save(data_path, model_path, use_grades=True):
    df = load_data(data_path)
    X, y = get_features_and_target(df, use_grades=use_grades)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, model_path)
    return model, X_test, y_test

import os


if __name__ == "__main__":
    data_path = os.path.join(BASE_DIR, "..", "Dataset", "student-mat.csv")
    model_path = os.path.join(BASE_DIR, "..", "Model", "student_performance_model.pkl")

    train_and_save(data_path=data_path, model_path=model_path)