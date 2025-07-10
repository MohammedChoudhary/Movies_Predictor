import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load model and columns
model = joblib.load("movie_success_predictor.pkl")
columns = joblib.load("movies_columns.pkl")

# Load profile image
profile_img = Image.open("assets/profile.jpeg")

# App configuration
st.set_page_config(page_title="Movie Success Predictor", layout="centered")

# ---- Custom CSS ----
st.markdown("""
    <style>
        .title-text {
            font-size: 40px;
            font-weight: bold;
            color: #0F4C75;
        }
        .subtitle-text {
            font-size: 24px;
            color: #3282B8;
        }
        .desc-text {
            font-size: 16px;
            color: #333333;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #0f4c75;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Header Section ----
st.image(profile_img, width=150)
st.markdown("<div class='title-text'>Mohammed Choudhary</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>Data Science</div>", unsafe_allow_html=True)
st.markdown("<div class='desc-text'>Predict whether your movie will be a blockbuster or a flop in seconds! 🎬</div>", unsafe_allow_html=True)
st.markdown("---")

# ---- Prediction Section ----
st.header("🎯 Movie Success Prediction")
st.markdown("Enter the details below:")

budget = st.number_input("💰 Budget (USD)", min_value=1000000, max_value=250000000, step=1000000)
popularity = st.number_input("🔥 Popularity Score", min_value=1.0, max_value=150.0, step=1.0)
runtime = st.number_input("🎬 Runtime (minutes)", min_value=60, max_value=240, step=5)
vote_count = st.number_input("🗳️ Vote Count", min_value=0, max_value=50000, step=100)
vote_average = st.slider("⭐ Vote Average (1-10)", 1.0, 10.0, step=0.1)

if st.button("Predict"):
    try:
        input_df = pd.DataFrame([[budget, popularity, runtime, vote_average]], columns=columns)
        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.success("✅ The movie is predicted to be a **Hit**! 🍿💰")
        else:
            st.error("❌ The movie is predicted to be a **Flop**. 🎬💸")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("---")

# ---- Contact Section ----
st.subheader("📬 Connect with Me")
st.write("🔗 [LinkedIn](https://www.linkedin.com/in/mohammedchoudhary)")
st.write("💻 [GitHub](https://github.com/MohammedChoudhary)")
st.write("📧 Email: choudhary@example.com")

# ---- Footer ----
st.markdown("<div class='footer'>Made with ❤️ by Mohammed Choudhary</div>", unsafe_allow_html=True)
