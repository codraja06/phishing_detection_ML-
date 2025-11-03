# Phishing Detection

<img width="1916" height="1006" alt="image" src="https://github.com/user-attachments/assets/7169ed70-fc8e-4d03-9ad4-e23f52d89923" />
 <!-- Replace '#' with a direct link to your application screenshot or GIF -->

This project implements a web-based tool for real-time phishing detection using a machine learning model integrated via the Flask framework. Users can input a URL and instantly receive a prediction on whether the link is legitimate or a potential phishing attempt, making machine learning accessible for practical cybersecurity awareness.

## 🚀 Key Features

Phishing URL Detection: Detects and classifies URLs as Legitimate or Suspicious based on URL patterns.

User-Friendly Web Interface: Clean, responsive HTML/CSS design for both desktop and mobile devices.

Dynamic Result Display: Result appears only after submission, hidden by default.

Color-Coded Feedback: Green for legitimate sites, red for suspicious links.

Real-Time Analysis: Instant result after entering the URL.

Responsive Design: Optimized layout for all screen sizes.
## ⚙️ Technologies Used

| Category         | Technology   | Purpose                                             |
| ---------------- | ------------ | --------------------------------------------------- |
| Backend & ML     | Python 3.x   | Core logic, data processing, ML model handling      |
| Web Framework    | Flask        | Application routing and backend functionality       |
| Frontend         | HTML & CSS   | Structure and styling of the interface              |
| Assets           | Font Awesome | Icons and visual enhancements                       |

## 📂 Project Structure

```
phishing_detection_ml/
│
├── app.py                 # Flask backend logic and routing    
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
git clone https://github.com/codraja06/phishing-detection-ml.git
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

## 🔧 Recent Updates

* ✅ Fixed issue where result text displayed even before input.
* ✅ Added conditional rendering logic in `index.html`.
* ✅ Enhanced CSS with animations, color-coded feedback, and better visibility control.
* ✅ Updated Flask route logic for cleaner predictions.

## 🤝 Contact and Reference

* **Portfolio:** [Your Portfolio](https://codwolf-7c928.web.app/)
* **GitHub:** [codraja06](https://github.com/codraja06)

