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

---

## 🚀 How to Run Locally

Follow these separate step-by-step instructions to clone and deploy the application on your local workstation:

### 1. Clone the Repository
```bash
# Step 1: Pull the latest production codebase from GitHub to your machine
git clone [https://github.com/mukundan1012-creator/StudentPerformancePredictor_Final.git](https://github.com/mukundan1012-creator/StudentPerformancePredictor_Final.git)

### 2. Initialize the Path
# Step 2: Move into the root folder where all project scripts reside
cd StudentPerformancePredictor_Final

### 3. Install Core Dependencies
# Step 3: Install the exact versions of Scikit-Learn, Streamlit, and Joblib required by the pipeline
pip install -r requirements.txt

### 4. Launch the Streamlit Web Application
# Step 4: Boot up the local web application server
streamlit run app.py



