from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

# --------------------
# App setup
# --------------------
app = Flask(__name__)
CORS(app)

# --------------------
# Resolve base paths safely (works locally + Render)
# --------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_PATH = os.path.join(MODEL_DIR, "fake_news_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")

# --------------------
# Load model & vectorizer
# --------------------
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model files: {e}")

# --------------------
# Routes
# --------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "message": "Fake News Detection API is live 🚀"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not data or "text" not in data:
        return jsonify({"error": "Text field is required"}), 400

    text = data["text"].strip()

    if len(text) == 0:
        return jsonify({"error": "Text cannot be empty"}), 400

    try:
        text_tfidf = vectorizer.transform([text])
        prediction = model.predict(text_tfidf)[0]
        confidence = model.predict_proba(text_tfidf).max()

        result = "REAL" if prediction == 1 else "FAKE"

        return jsonify({
            "prediction": result,
            "confidence": round(float(confidence), 3)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------------------
# Entry point
# --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
