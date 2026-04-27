from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd


# LOAD MODEL — runs once when server starts
try:
    model = joblib.load("movie_success_predictor.pkl")
    columns = joblib.load("movies_columns.pkl")
    print("Yes!! , Model loaded successfully!")
except Exception as e:
    print(f"Oops man, Error loading model: {e}")
    model = None
    columns = None


# CREATE APP

app = FastAPI(
    title="Movie Success Predictor API",
    description="Predict whether a movie will be a Hit or Flop using ML",
    version="1.0.0"
)


# INPUT MODEL — with validation ranges

class MovieInput(BaseModel):
    budget: float = Field(..., ge=1000000, le=250000000, description="Movie budget in USD")
    popularity: float = Field(..., ge=1.0, le=150.0, description="Popularity score")
    runtime: float = Field(..., ge=60, le=240, description="Runtime in minutes")
    vote_average: float = Field(..., ge=1.0, le=10.0, description="Average vote rating (1-10)")


# ENDPOINTS


# Health check
@app.get("/")
def root():
    return {
        "status": "Movie Predictor API is running!",
        "model_loaded": model is not None
    }

# Prediction endpoint
@app.post("/predict")
def predict(movie: MovieInput):

    # Check model is loaded
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Step 1: Create dataframe exactly like Streamlit app does
    input_df = pd.DataFrame(
        [[movie.budget, movie.popularity, movie.runtime, movie.vote_average]],
        columns=columns
    )

    # Step 2: Make prediction
    prediction = model.predict(input_df)[0]

    # Step 3: Get probability/confidence
    probability = model.predict_proba(input_df)[0]
    confidence = round(max(probability) * 100, 2)

    # Step 4: Return result
    return {
        "prediction": "Hit" if prediction == 1 else "Flop",
        "confidence": f"{confidence}%",
        "input_received": {
            "budget": movie.budget,
            "popularity": movie.popularity,
            "runtime": movie.runtime,
            "vote_average": movie.vote_average
        }
    }