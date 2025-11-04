import streamlit as st
import pickle
import numpy as np

# ----------------- Custom Styling -----------------
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💊", layout="centered")

custom_css = """
<style>
.stApp {
    background: linear-gradient(135deg, #e0f7fa, #fff);
    font-family: "Arial", sans-serif;
}

.card {
    padding: 20px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    margin-bottom: 20px;
}

h1 {
    text-align: center;
    font-weight: 700;
    color: #0077b6;
}

label, .stSelectbox label, .stNumberInput label {
    font-size: 16px !important;
    color: #0d3b66 !important;
}

.stButton>button {
    background: linear-gradient(90deg, #0077b6, #00b4d8);
    color: white;
    padding: 10px 25px;
    border-radius: 10px;
    border: none;
    font-size: 18px;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #0096c7, #48cae4);
    transform: scale(1.05);
}

.result-box {
    padding: 15px;
    background: #d9f8e6;
    border-left: 6px solid #00b894;
    font-size: 20px;
    border-radius: 10px;
    animation: fade 0.6s ease-in-out;
}

@keyframes fade {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ----------------- Load Model -----------------
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------- UI Section -----------------
st.title("💊 Medical Insurance Charges Predictor")

st.markdown("""
<div class='card'>
Predict **Medical Insurance Charges** using  
🧓 Age • ⚖ BMI • 🚬 Smoking Status  
</div>
""", unsafe_allow_html=True)

# Input fields inside card
st.markdown("<div class='card'>", unsafe_allow_html=True)

age = st.number_input("Enter Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=60.0, value=25.0)
smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])

st.markdown("</div>", unsafe_allow_html=True)

# Encode smoker variable
smoker_yes = 1 if smoker == "Yes" else 0

input_data = np.array([[age, bmi, smoker_yes]])

# Predict button
if st.button("Predict Insurance Charges 💰"):
    prediction = model.predict(input_data)
    st.markdown(f"""
    <div class='result-box'>
    💵 Estimated Charges: <b>${prediction[0]:,.2f}</b>
    </div>
    """, unsafe_allow_html=True)
