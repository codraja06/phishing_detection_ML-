# Phishing Detection Using Machine Learning

<img width="1913" height="1003" alt="image" src="https://github.com/user-attachments/assets/fa3e9a47-bade-43a5-aa8a-af370db68903" />
 <!-- Replace '#' with a direct link to your application screenshot or GIF -->

This project implements a web-based tool for real-time phishing detection using a machine learning model integrated via the Flask framework. Users can input a URL and instantly receive a prediction on whether the link is legitimate or a potential phishing attempt, making machine learning accessible for practical cybersecurity awareness.

## 🚀 Key Features

* **Phishing URL Detection:** Uses a pre-trained scikit-learn model to classify URLs as Legitimate or Phishing.
* **User-Friendly Web Interface:** Clean, responsive HTML/CSS interface for both desktop and mobile devices.
* **Dynamic Result Display:** Result message (Legitimate/Suspicious) appears **only after input submission**, hidden by default.
* **Enhanced Styling:** Result box styled with color-coded feedback (green for legitimate, red for suspicious) and smooth fade-in animation.
* **Seamless Model Integration:** Production-ready approach to serve a machine learning model (.pkl file) via Python backend.
* **Real-Time Prediction:** Provides instantaneous feedback on URL submissions.
* **Responsive Design:** Optimized for all devices, from mobile to desktop.

## ⚙️ Technologies Used

| Category         | Technology   | Purpose                                             |
| ---------------- | ------------ | --------------------------------------------------- |
| Backend & ML     | Python 3.x   | Core logic, data processing, ML model handling      |
| Web Framework    | Flask        | Application routing and backend functionality       |
| Machine Learning | scikit-learn | Training, serialization, and serving the classifier |
| Frontend         | HTML & CSS   | Structure and styling of the interface              |
| Assets           | Font Awesome | Icons and visual enhancements                       |

## 📂 Project Structure

```
phishing_detection_ml/
│
├── app.py                 # Flask backend logic and routing
├── model/
│   └── model.pkl          # Pre-trained ML classification model (or mode.pkl)
├── templates/
│   └── index.html         # Frontend template (updated result display logic)
├── static/
│   ├── css/
│   │   └── style.css      # Updated CSS with result animation and color-coded feedback
│   └── asset/
│       └── img1.png       # App icon or favicon
└── requirements.txt       # Python dependencies
```

## 🏁 Getting Started

### Prerequisites

* Python 3.6+ installed on your system.

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/phishing-detection-ml.git
cd phishing-detection-ml
```

Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
# On Linux/macOS
source venv/bin/activate
# On Windows
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure the model is present:

* Verify that `model.pkl` is inside the `model/` directory. A fallback to `mode.pkl` is supported.

### Running the Application

Start the Flask server (local development):

```bash
python app.py
Alternatively, if deploying with Procfile (e.g., Render/Heroku), the command is:

```
gunicorn app:app
```

### API

JSON endpoint for programmatic checks:

```
POST /analyze
{
  "url": "http://example.com"
}
```

Response:

```
{
  "success": true,
  "url": "http://example.com",
  "result": "Legal",
  "is_phishing": false
}
```
```

Access the application in your browser:

```
http://127.0.0.1:5000/
```

### 👩‍💻 Usage

1. Open the application in your browser.
2. Enter any website URL in the input field.
3. Click **Submit**.
4. View the prediction result (Legitimate or Suspicious) displayed dynamically.

## 🧠 Model Details

The application uses a trained machine learning model (`phishing.pkl`) built on a dataset of labeled phishing and legitimate URLs.

Typical features extracted for prediction include:

* URL length
* Number of subdomains
* Presence of `@`, `-`, or multiple `//`
* Presence of words like `login`, `secure`, or numeric patterns
* Whether `https` is used

> Note: `phishing.pkl` contains both feature extraction and the trained classifier (e.g., Random Forest).

## 🔧 Recent Updates

* ✅ Fixed issue where result text displayed even before input.
* ✅ Added conditional rendering logic in `index.html`.
* ✅ Enhanced CSS with animations, color-coded feedback, and better visibility control.
* ✅ Updated Flask route logic for cleaner predictions.

## 🤝 Contact and Reference

* **Portfolio:** [Your Portfolio](https://codwolf-7c928.web.app/)
* **GitHub:** [codraja06](https://github.com/codraja06)

