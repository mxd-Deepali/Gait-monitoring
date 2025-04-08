# ✅ First line: streamlit config (MUST be before everything Streamlit-related)
import streamlit as st
st.set_page_config(page_title="Multiuser Gait Monitoring")

# ✅ Then rest of the imports
import pandas as pd
from datetime import datetime
import os

st.title("👣 Gait Monitoring Dashboard - Multiuser")

# 📁 Directory to store user data files
data_dir = "user_data"
os.makedirs(data_dir, exist_ok=True)

# 👤 1. User Login / Identification
username = st.text_input("Enter your name to begin:")

if username:
    user_file = os.path.join(data_dir, f"{username}_gait.csv")

    st.success(f"Welcome, {username}! Let's start monitoring your gait.")
    st.markdown("---")

    # 🧠 2. Collect Gait Features
    st.subheader("Step 1: Enter Gait Parameters")

    step_time = st.slider("Step Time (s)", 0.3, 1.5, 0.8)
    stride_length = st.slider("Stride Length (m)", 0.2, 1.2, 0.45)
    toe_pressure = st.slider("Toe Pressure (%)", 0, 100, 30)
    heel_pressure = st.slider("Heel Pressure (%)", 0, 100, 70)
    cadence = st.slider("Cadence (steps/min)", 40, 150, 90)

    # 💾 3. Save Button
    if st.button("💾 Save Gait Entry"):
        data = {
            "Timestamp": datetime.now(),
            "Step Time": step_time,
            "Stride Length": stride_length,
            "Toe Pressure": toe_pressure,
            "Heel Pressure": heel_pressure,
            "Cadence": cadence
        }
        df = pd.DataFrame([data])

        if os.path.exists(user_file):
            df.to_csv(user_file, mode='a', header=False, index=False)
        else:
            df.to_csv(user_file, index=False)

        st.success("✅ Entry saved to your personal gait log!")

    # 📂 4. View Gait History
    if st.checkbox("📁 Show My Gait History"):
        if os.path.exists(user_file):
            data = pd.read_csv(user_file)
            st.dataframe(data)
        else:
            st.warning("⚠️ No data found for you yet.")
