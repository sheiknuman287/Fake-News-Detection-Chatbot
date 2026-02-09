function checkNews() {
    const text = document.getElementById("newsInput").value;
    const resultDiv = document.getElementById("result");

    if (!text.trim()) {
        resultDiv.innerHTML = "⚠️ Please enter some news text.";
        return;
    }

    resultDiv.innerHTML = "⏳ Checking...";

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
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
