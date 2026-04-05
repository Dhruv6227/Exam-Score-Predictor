import streamlit as st
import numpy as np
import pickle

# load model
model = pickle.load(open("model/model.pkl", "rb"))
encoders = pickle.load(open("model/encoders.pkl", "rb"))

st.title("🎓 Student Exam Score Predictor")

st.write("Enter student details to predict exam score")

# input fields
age = st.number_input("Age", 15, 40, 20)

gender = st.selectbox("Gender", encoders["gender"].classes_)

course = st.selectbox("Course", encoders["course"].classes_)

study_hours = st.slider("Study Hours", 0, 12, 5)

attendance = st.slider("Class Attendance %", 0, 100, 75)

internet = st.selectbox("Internet Access", encoders["internet_access"].classes_)

sleep_hours = st.slider("Sleep Hours", 0, 12, 7)

sleep_quality = st.selectbox("Sleep Quality", encoders["sleep_quality"].classes_)

study_method = st.selectbox("Study Method", encoders["study_method"].classes_)

facility = st.selectbox("Facility Rating", encoders["facility_rating"].classes_)

difficulty = st.selectbox("Exam Difficulty", encoders["exam_difficulty"].classes_)


if st.button("Predict Score"):
    
    input_data = {
        "age": age,
        "gender": encoders["gender"].transform([gender])[0],
        "course": encoders["course"].transform([course])[0],
        "study_hours": study_hours,
        "class_attendance": attendance,
        "internet_access": encoders["internet_access"].transform([internet])[0],
        "sleep_hours": sleep_hours,
        "sleep_quality": encoders["sleep_quality"].transform([sleep_quality])[0],
        "study_method": encoders["study_method"].transform([study_method])[0],
        "facility_rating": encoders["facility_rating"].transform([facility])[0],
        "exam_difficulty": encoders["exam_difficulty"].transform([difficulty])[0],
    }

    features = np.array(list(input_data.values())).reshape(1,-1)

    prediction = model.predict(features)

    st.success(f"Predicted Exam Score: {round(prediction[0],2)}")