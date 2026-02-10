const API_URL = "https://fake-news-detection-chatbot.onrender.com/predict";

function checkNews() {
    const text = document.getElementById("newsInput").value;
    const resultDiv = document.getElementById("result");

    if (!text.trim()) {
        resultDiv.innerHTML = "⚠️ Please enter some news text.";
        return;
    }

    resultDiv.innerHTML = "⏳ Checking...";

    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = "❌ Error: " + data.error;
        } else {
            resultDiv.innerHTML = `
                <strong>Prediction:</strong> ${data.prediction}<br>
                <strong>Confidence:</strong> ${data.confidence}
            `;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = "❌ Could not connect to server.";
        console.error(error);
    });
}
