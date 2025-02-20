import streamlit as st
import random
import pandas as pd
from sklearn.ensemble import IsolationForest
import time

# Title and Abstract Display
st.title("Real-Time Fraud Detection in Financial Transactions")
st.markdown("""
#### **Use Case: Real-Time Financial Transactions Monitoring**

This system continuously monitors financial transactions to detect fraudulent activities. 
Anomalies in transaction patterns can indicate potential fraud, helping financial institutions 
prevent losses and unauthorized access. Our model uses **AI-based anomaly detection** (Isolation Forest) 
to validate each transaction and flag suspicious ones in real-time.

**How it Works:**
- Simulates real-time financial transactions (amount, transaction type, balance, etc.)
- Uses **AI-based anomaly detection** to detect fraud.
- Provides a **real-time dashboard** for transaction monitoring.
- Displays anomalies for further investigation.
""")

# Initialize Session State for Data Storage
if "historical_data" not in st.session_state:
    st.session_state.historical_data = pd.DataFrame(columns=["amount", "transaction_type", "balance", "status"])

# Simulated Transaction Stream Function
def generate_transaction():
    return {
        "amount": random.uniform(1, 10000),  # Random transaction amount
        "transaction_type": random.choice(["Credit", "Debit"]),  # Type of transaction
        "balance": random.uniform(100, 50000)  # Account balance after transaction
    }

# Data Preprocessing
def preprocess_data(data):
    df = pd.DataFrame([data])
    df["amount"] = df["amount"].clip(1, 10000)  # Limit transaction amount range
    df["balance"] = df["balance"].clip(100, 50000)  # Keep balance within range
    return df

# Initialize AI Model
@st.cache_resource
def initialize_model():
    training_data = pd.DataFrame({
        "amount": [random.uniform(1, 10000) for _ in range(1000)],
        "balance": [random.uniform(100, 50000) for _ in range(1000)],
    })
    model = IsolationForest(contamination=0.02, random_state=42)  # 2% fraud rate assumption
    model.fit(training_data)
    return model

# AI-Based Validation
def validate_transaction(model, data):
    if isinstance(data, pd.DataFrame):
        df = data
    else:
        df = pd.DataFrame([data])
    prediction = model.predict(df.drop(columns=["transaction_type"]))[0]
    return "Legit" if prediction == 1 else "Fraudulent"

# Initialize Model
st.write("Initializing fraud detection model...")
model = initialize_model()
st.success("Model initialized successfully!")

# Streaming Transactions with Real-Time Validation
st.write("### Real-Time Transaction Monitoring")
placeholder = st.empty()

while True:
    # Generate & preprocess incoming transaction
    raw_data = generate_transaction()
    processed_data = preprocess_data(raw_data)

    # Validate transaction using AI model
    status = validate_transaction(model, processed_data)
    processed_data["status"] = status
    processed_data["transaction_type"] = raw_data["transaction_type"]  # Add transaction type back

    # Update historical data
    st.session_state.historical_data = pd.concat([st.session_state.historical_data, processed_data], ignore_index=True)

    # Display Data in Streamlit UI
    with placeholder.container():
        st.write("#### Latest Transactions with Validation Status")
        st.dataframe(st.session_state.historical_data.tail(10))

        st.write("#### Transaction Trends Over Time")
        st.line_chart(st.session_state.historical_data[["amount", "balance"]])

        st.write("#### Recent Fraudulent Transactions")
        frauds = st.session_state.historical_data[st.session_state.historical_data["status"] == "Fraudulent"].tail(5)
        if not frauds.empty:
            st.dataframe(frauds)
        else:
            st.write("No fraudulent transactions detected recently.")

    # Pause to simulate real-time streaming
    time.sleep(2)