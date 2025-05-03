from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load("model.pkl.gz")

@app.route("/")
def home():
    return "Hello from Flask on Azure with model!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        education = data.get("education")
        experience = data.get("experience")

        # Map education levels to numeric values
        education_map = {"Bachelors": 0, "Masters": 1, "PhD": 2}
        education_val = education_map.get(education, -1)

        # Format input and run prediction
        model_input = np.array([[education_val, int(experience)]])
        prediction = model.predict(model_input)[0]

        return jsonify({"prediction": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400