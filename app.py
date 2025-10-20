from flask import Flask, render_template, request
import os
import pickle
import re

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "phishing.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


def extract_features(url):
    features = []
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(int('https' in url))
    features.append(int('@' in url))
    features.append(int('//' in url[7:]))
    features.append(len(re.findall(r'\d', url)))
    features.append(int('login' in url.lower()))
    features.append(int('secure' in url.lower()))
    
    
    while len(features) < 31:
        features.append(0)
    return features



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url', '').strip()

    
    features = extract_features(url)

    try:
        prediction = model.predict([features])[0]

        if str(prediction) == "1" or str(prediction).lower() in ['phish', 'malicious', 'suspicious']:
            output = f"({url}) is SUSPICIOUS."
        else:
            output = f"({url}) is LEGITIMATE."

    except Exception as e:
        output = f"Prediction failed: {e}"

    return render_template('index.html', result=output)


if __name__ == '__main__':
    app.run(debug=True)
