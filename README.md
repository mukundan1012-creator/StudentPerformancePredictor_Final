# 🎓 Student Performance Predictor AI

An end-to-end Machine Learning web application that predicts a student's final academic grade (G3) using demographic, academic, and lifestyle factors.

## 📊 Model Performance
| Metric | Value |
|----------|----------|
| Algorithm | Random Forest Regressor |
| Validation Strategy | 5-Fold Cross Validation |
| R² Score | 0.872 |

## 🔍 Features Used

## Features Engineering

The following features were selected for prediction:

- First Period Grade (G1)
- Second Period Grade (G2)
- Weekly Study Time
- Number of Past Failures
- School Absences

These features showed strong correlation with final academic performance and were used as inputs to the Random Forest model.

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib

## 📁 Project Structure

```
StudentPerformancePredictor_Final/
│
├── Dataset/
├── Model/
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/mukundan1012-creator/StudentPerformancePredictor_Final.git
```

### 2. Move into the Project Directory

```bash
cd StudentPerformancePredictor_Final
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Application

```bash
streamlit run app.py
```

## 🎯 Project Goal

The objective of this project is to predict student academic performance using Machine Learning techniques and provide an interactive interface for users to test predictions.

---
Developed using Python, Scikit-Learn, and Streamlit.
