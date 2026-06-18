import streamlit as st
import joblib

# Load trained model
model = joblib.load("Model/student_performance_model.pkl")
st.sidebar.title("Project Information")

st.sidebar.info("""
Model: Random Forest Regressor

Dataset: UCI Student Performance Dataset

R² Score: 0.86

Features Used:
- Study Time
- Failures
- Absences
- G1
- G2
""")

# Title
st.title("🎓 AI-Powered Student Performance Predictor")

st.markdown("""
This application predicts a student's final academic performance (G3)
using a Machine Learning Random Forest model trained on the
UCI Student Performance Dataset.

Fill in the details below and click Predict Final Grade.
""")

# Inputs
studytime = st.number_input("Study Time (1-4)", min_value=1, max_value=4, value=2)

failures = st.number_input("Past Failures", min_value=0, max_value=4, value=0)

absences = st.number_input("Absences", min_value=0, value=0)

g1 = st.number_input("First Period Grade (G1)", min_value=0, max_value=20, value=10)

g2 = st.number_input("Second Period Grade (G2)", min_value=0, max_value=20, value=10)

# Predict button
if st.button("Predict Final Grade"):

    prediction = model.predict([
        [
            studytime,
            failures,
            absences,
            g1,
            g2
        ]
    ])

    pred = prediction[0]

    st.success(
        f"🎯 Predicted Final Grade (G3): {pred:.2f}/20"
    )

    if pred >= 16:
        st.info("🌟 Excellent Performance")

    elif pred >= 12:
        st.info("👍 Good Performance")

    elif pred >= 8:
        st.warning("📚 Average Performance")

    else:
        st.error("⚠️ Needs Improvement")
st.markdown("---")

st.caption(
    "Built using Python, Scikit-Learn, Streamlit and Random Forest Regression."
)