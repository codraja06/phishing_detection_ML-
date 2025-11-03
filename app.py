from flask import Flask, render_template, request, jsonify
import os
import re
from urllib.parse import urlparse

# -----------------------------------------
# Flask app setup
# -----------------------------------------
app = Flask(__name__)

# -----------------------------------------
# Helper functions
# -----------------------------------------
def is_valid_url(url):
    """Validate URL format."""
    pattern = re.compile(
        r'^(https?://)?'  # http:// or https://
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})'  # domain
        r'(:[0-9]{1,5})?'  # optional port
        r'(/.*)?$',  # path
        re.IGNORECASE
    )
    return re.match(pattern, url) is not None


def simple_phishing_check(url):
    """
    Simple heuristic check (no ML model).
    Flags suspicious URLs with common phishing indicators.
    """
    url = url.lower()

    suspicious_keywords = [
        "login", "secure", "update", "verify", "bank", "account",
        "password", "signin", "confirm", "reset", "free", "bonus"
    ]

    # If too long or contains '@' or '-' or IP address pattern
    if len(url) > 80 or '@' in url or re.search(r'\d+\.\d+\.\d+\.\d+', url):
        return True

    # Keyword match
    for word in suspicious_keywords:
        if word in url:
            return True

    return False


# -----------------------------------------
# Routes
# -----------------------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url', '').strip()
    if not url:
        return render_template('index.html', result="⚠️ Please enter a URL.")

    if not is_valid_url(url):
        return render_template('index.html', result="⚠️ Invalid URL format.")

    # Simple rule-based detection (no ML)
    is_phish = simple_phishing_check(url)

    if is_phish:
        output = f"🚨 The URL ({url}) looks SUSPICIOUS!"
    else:
        output = f"✅ The URL ({url}) seems LEGITIMATE."

    return render_template('index.html', result=output)


@app.route('/analyze', methods=['POST'])
def analyze():
    """JSON API for testing without ML."""
    data = request.get_json()
    url = (data.get('url') if data else "").strip()

    if not url:
        return jsonify({"success": False, "error": "URL is required"}), 400

    if not is_valid_url(url):
        return jsonify({"success": False, "error": "Invalid URL format"}), 400

    is_phish = simple_phishing_check(url)

    return jsonify({
        "success": True,
        "url": url,
        "result": "Illegal" if is_phish else "Legal",
        "is_phishing": is_phish
    })


# -----------------------------------------
# Run the app
# -----------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
