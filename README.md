# Fraud Detection in Financial Transactions

## 🚀 Overview
This project focuses on detecting fraudulent transactions using machine learning. It includes data analysis, model training, evaluation, and a Flask web app for real-time predictions.

## 📹 Demo Video
Below is a screen recording of the web app in action:

![Demo Video](demo_video.mp4)

Ensure the `demo_video.mp4` file is placed inside the `static/` folder so it can be accessed properly in the README.

---

## 📂 Project Structure
```
📁 fraud-detection-app
│── 📂 templates
│   ├── index.html  # Web app frontend
│── 📂 static
│   ├── style.css   # Web app styling (if applicable)
│   ├── demo_video.mp4  # Web app demo video
│── app.py          # Flask application
│── model.pkl       # Trained ML model
│── requirements.txt # Dependencies
│── README.md       # Documentation
│── fraud_detection.ipynb # Jupyter Notebook for data analysis
```

## 📊 Data Analysis & Preprocessing
- Identified transaction patterns and anomalies.
- Handled class imbalance using undersampling.
- Standardized numerical features for better model performance.

## 🤖 Machine Learning Models
- **Algorithms used:** Logistic Regression, Decision Tree, KNN, SVM, Naïve Bayes, Random Forest.
- **Best Model:** Random Forest (Optimized via GridSearchCV)
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score.

## 🌍 Web App Deployment
A Flask-based web app where users can input transaction details to check if they are fraudulent.

### 🚀 How to Run
#### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
#### 2️⃣ Run Flask App
```sh
python app.py
```
#### 3️⃣ Access in Browser
Open `http://127.0.0.1:5000/` in your browser.

---
Made with ❤️ by Team - InnovateX
Team Members
Ujjwal Raj - ME22B1072
Suraj Kumar - ME22B1073
