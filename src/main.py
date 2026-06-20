from train_model import train_and_save
from evaluate import evaluate_model

model, X_test, y_test = train_and_save(
    data_path="../Dataset/student-mat.csv",
    model_path="../Model/student_performance_model.pkl",
    use_grades=True
)
print("=== Original Model (with G1, G2) ===")
evaluate_model(model, X_test, y_test, save_plot_path="predicted_vs_actual.png")

model_ng, X_test_ng, y_test_ng = train_and_save(
    data_path="../Dataset/student-mat.csv",
    model_path="../Model/student_performance_model_no_grades.pkl",
    use_grades=False    
)
print("\n=== Honesty-Test Model (without G1, G2) ===")
evaluate_model(model_ng, X_test_ng, y_test_ng)

