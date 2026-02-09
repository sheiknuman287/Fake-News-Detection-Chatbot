from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "model")

model = joblib.load(os.path.join(MODEL_DIR, "fake_news_model.pkl"))
vectorizer = joblib.load(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))

@app.route("/")
def home():
    return "Fake News Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    text_tfidf = vectorizer.transform([text])
    prediction = model.predict(text_tfidf)[0]
    confidence = model.predict_proba(text_tfidf).max()

    result = "REAL" if prediction == 1 else "FAKE"

    return jsonify({
        "prediction": result,
        "confidence": round(float(confidence), 3)
    })

if __name__ == "__main__":
    app.run(debug=True)
