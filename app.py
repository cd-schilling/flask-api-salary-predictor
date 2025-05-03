from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Azure!"

@app.route("/predict", methods=["POST"])
def predict():
    return {"message": "API is working!"}