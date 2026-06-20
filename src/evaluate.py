import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error,r2_score

def evaluate_model(model, X_test, y_test, save_plot_path=None):
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"MAE: {mae:.4f}")
    print(f"R2: {r2:.4f}")

    plt.scatter(y_test, predictions)
    plt.xlabel("Actual Marks")
    plt.ylabel("Predicted Marks")
    plt.title("Actual vs Predicted Marks")

    if save_plot_path:
        plt.savefig(save_plot_path, dpi=150, bbox_inches="tight")
    plt.show()

    return mae,r2

