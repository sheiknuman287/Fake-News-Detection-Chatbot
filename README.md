# 📰 Fake News Detection Chatbot

A full-stack AI chatbot that detects whether a news article is **REAL or FAKE** using Natural Language Processing and Machine Learning.

## 🚀 Features
- TF-IDF based text vectorization
- Logistic Regression classifier (98%+ accuracy)
- Flask REST API backend
- Simple chatbot-style frontend (HTML/CSS/JS)

## 🧠 How It Works
1. User enters a news article
2. Text is vectorized using TF-IDF
3. ML model predicts REAL or FAKE
4. Confidence score is returned

> ⚠️ Note: This model detects **news writing style**, not factual truth.

## 🛠 Tech Stack
- Python
- Scikit-learn
- NLTK
- Flask
- HTML / CSS / JavaScript

## ▶️ Run Locally
```bash
pip install -r requirements.txt
cd backend
python app.py
Open frontend/index.html in browser.

📈 Model Performance
Accuracy: 98.8%

Precision / Recall / F1-score: 0.99

📌 Author
Sheik Numan