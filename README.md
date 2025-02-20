# real-time-validation-using-AI

This project continuously monitors *financial transactions* to detect *fraudulent activities* in real-time using *AI-based anomaly detection (Isolation Forest). The system simulates transactions, validates them using an AI model, and provides a **real-time dashboard* for monitoring.

---

## 🔧 Installation Guide

### 1️⃣ Prerequisites
Ensure you have the following installed:
- *Python (3.8 or later)*: [Download Python](https://www.python.org/downloads/)
- *pip (Python package manager)*
- *Git (optional, for cloning repository)*

### 2️⃣ Clone the Repository (Optional)
sh
$ git clone https://github.com/your-username/real-time-fraud-detection.git
$ cd real-time-fraud-detection


### 3️⃣ Create a Virtual Environment (Recommended)
sh
$ python -m venv fraud_env
$ source fraud_env/bin/activate  # On macOS/Linux
$ fraud_env\Scripts\activate  # On Windows


### 4️⃣ Install Required Dependencies
sh
$ pip install -r requirements.txt

*OR* install dependencies manually:
sh
$ pip install streamlit pandas scikit-learn


---

## 🚀 Running the Application
sh
$ streamlit run app.py


After running the command, the application will open in your browser at:

http://localhost:8501


---

## 🛠️ Features
- *Simulates real-time financial transactions* (Credit/Debit, amount, balance, etc.)
- *AI-based anomaly detection* using the *Isolation Forest model*
- *Real-time transaction monitoring dashboard*
- *Charts for transaction trends*
- *Displays fraudulent transactions for review*

---

## 📂 Project Structure

real-time-fraud-detection/
│── app.py                # Main Streamlit application
│── requirements.txt      # Required dependencies
│── README.md             # Documentation
│── fraud_env/            # Virtual environment (if created)
