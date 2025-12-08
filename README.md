# 🎣 Phishing Detection

   This project is a web-based tool that checks whether a given URL is safe or suspicious. Users can enter any website link, and the system quickly analyzes it and shows if it might be a phishing site. This helps people stay safer online by avoiding fake or harmful websites.


![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-None-red)
![Stars](https://img.shields.io/github/stars/codraja06/phishing_detection_ML-?style=social)
![Forks](https://img.shields.io/github/forks/codraja06/phishing_detection_ML-?style=social)

---
## Preview
<img width="1916" height="1006" alt="image" src="https://github.com/user-attachments/assets/7169ed70-fc8e-4d03-9ad4-e23f52d89923" />
 <!-- Replace '#' with a direct link to your application screenshot or GIF -->


## ✨ Features

*   🧠 **Intelligent Detection:** Leverages advanced machine learning models to accurately classify URLs and content as legitimate or phishing.
*   ⚡ **Real-time Analysis:** Provides rapid feedback on submitted links, minimizing exposure time to malicious sites.
*   🌐 **Web-based Interface:** User-friendly web application built with Python (Flask) for easy interaction and URL submission.
*   🛠️ **Extensible Architecture:** Designed with modularity in mind, allowing for easy integration of new models or data sources.
*   📈 **Performance Monitoring:** Includes `.snapshots` directory for potential model versioning or performance tracking.

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


## 🚀 Installation Guide

Follow these steps to get the Phishing Detection ML- project up and running on your local machine.

### Prerequisites

Ensure you have Python 3.8+ and `pip` installed.

### Step-by-Step Installation

1.  **Clone the Repository:**
    Start by cloning the project repository to your local machine:

    ```bash
    git clone https://github.com/codraja06/phishing_detection_ML-.git
    cd phishing_detection_ML-
    ```

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage project dependencies:

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    *   **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

    *   **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    Install all required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application:**
    Once all dependencies are installed, you can start the Flask web application:

    ```bash
    python app.py
    ```
    The application will typically run on `http://127.0.0.1:5000/`.
---
## 👩‍💻 Usage

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
