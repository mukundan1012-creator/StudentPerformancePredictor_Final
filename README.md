# 🎓 Student Performance Predictor AI

An interactive end-to-end machine learning web application that uses a tuned Random Forest Regressor to predict a student's final academic grade ($G3$) based on demographic, lifestyle, and historical academic features.

## 📊 Model & Performance Metrics
* **Algorithm:** Random Forest Regressor (`n_estimators=100`, `max_depth=5`)
* **Validation Strategy:** 5-Fold Cross-Validation
* **Primary Metric:** Achieved a strong $R^2$ score of **0.872**, indicating that the selected features explain over 87% of the variance in final student outcomes.

## 🛠️ Features Explored
* **Prior Grades:** First period ($G1$) and Second period ($G2$) scores (0-20 scale)
* **Academic Factors:** Past class failures and weekly study hours
* **Lifestyle Factors:** Total school absences

## 🚀 How to Run Locally

1. Clone this repository to your machine:
```bash
git clone [https://github.com/mukundan1012-creator/StudentPerformancePredictor_Final.git](https://github.com/mukundan1012-creator/StudentPerformancePredictor_Final.git)

cd StudentPerformancePredictor_Final

pip install -r requirements.txt

streamlit run app.py
