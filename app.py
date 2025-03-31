from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

# Load the trained model and scaler
model = pickle.load(open("fraud_detection_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        transaction_type = int(request.form["type"])
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])

        # Preprocess input
        features = np.array([[transaction_type, amount, oldbalanceOrg, newbalanceOrig]])
        features[:, 1:] = scaler.transform(features[:, 1:])  # Scale numeric features

        # Predict fraud
        prediction = model.predict(features)
        result = "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"

        return render_template("index.html", prediction_text=result)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)