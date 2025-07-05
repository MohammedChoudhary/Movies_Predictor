import streamlit as st
import pandas as pd
import joblib

# Load model and column names
model = joblib.load('movie_success_predictor.pkl')
columns = joblib.load('movies_columns.pkl')

# Streamlit page config
st.set_page_config(page_title="Movie Success Predictor", layout="centered")
st.title("🎬 Movie Success Predictor")
st.write("Enter movie details to predict whether it's a **Hit** or **Flop**!")

# Collect user inputs
budget = st.number_input("Budget (in USD)", min_value=0)
popularity = st.number_input("Popularity Score", min_value=0.0)
runtime = st.number_input("Runtime (in minutes)", min_value=0)
vote_count = st.number_input("Vote Count", min_value=0)
vote_average = st.slider("Vote Average (1-10)", 1.0, 10.0, step=0.1)

# Predict button and input validation
if st.button("Predict"):
    # Input validations
    if not (1_000_000 <= budget <= 300_000_000):
        st.warning("⚠️ Please enter a budget between $1M and $300M.")
    elif not (0 <= popularity <= 100):
        st.warning("⚠️ Please enter a popularity score between 0 and 100.")
    elif not (60 <= runtime <= 210):
        st.warning("⚠️ Please enter a runtime between 60 and 210 minutes.")
    elif not (1.0 <= vote_average <= 10.0):
        st.warning("⚠️ Vote average must be between 1.0 and 10.0.")
    else:
        # Prepare input DataFrame
        input_df = pd.DataFrame(
            [[budget, popularity, runtime, vote_average]],
            columns=columns
        )

        # Predict result
        prediction = model.predict(input_df)[0]

        # Display result
        if prediction == 1:
            st.success("✔The movie is predicted to be a **Hit**! 🍿💰")
        else:
            st.error("🧩The movie is predicted to be a **Flop**. 👎🏼")
