# 🎓 Student Exam Score Predictor

## Overview
This project is a machine learning application that predicts a student's exam score based on various academic, lifestyle, and demographic factors. It consists of a model training pipeline built with Jupyter Notebook and an interactive web interface powered by Streamlit.

## Project Structure
- **`app.py`**: The Streamlit web application that provides the UI for making predictions.
- **`model.ipynb`**: A Jupyter Notebook containing data exploration, preprocessing, and the training pipeline for the Linear Regression model.
- **`model/model.pkl`**: The trained Linear Regression model.
- **`model/encoders.pkl`**: Saved label encoders used to transform categorical variables for the model.
- **`Exam_Score_Prediction.csv`**: The dataset used to train the machine learning model.
- **`requirement.txt`**: The list of Python dependencies required for the project.

## Requirements
Ensure you have Python installed, then install the required libraries:
- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`

## Installation and Usage

1. **Clone or navigate to the project directory** where your files are located.
2. **Install the dependencies** via pip:
   ```bash
   pip install -r requirement.txt
   ```
3. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```
4. **Access the App**: A new tab should automatically open in your web browser. If not, you can view the app at `http://localhost:8501`.

## Features Used
The web app prompts users for the following inputs to generate a prediction:
- Age
- Gender
- Course
- Study Hours
- Class Attendance (%)
- Internet Access
- Sleep Hours
- Sleep Quality
- Study Method
- Facility Rating
- Exam Difficulty
