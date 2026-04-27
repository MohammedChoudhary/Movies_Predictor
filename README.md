# 🎬 Movie Success Predictor

This project predicts whether a movie will be a **Hit** or **Flop** based on various numerical features like budget, popularity, runtime, and vote average.

It includes:
- Data preprocessing and EDA using **Pandas, Matplotlib, Seaborn**
- Machine Learning model using **Logistic Regression**
- A web app using **Streamlit**
- Deployment on **Streamlit Cloud**
- A **production-style REST API** built with **FastAPI**

---

## 🌐 Live App

👉 [Try the Streamlit Web App](https://moviespredictor-zgvh3sy2f84f2vptkumydf.streamlit.app/)

---

## 🚀 REST API (FastAPI)

This project also includes a **production-style REST API** built with FastAPI, allowing any application to programmatically access the prediction model.

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check — confirms API is running |
| POST | `/predict` | Send movie data, get Hit/Flop prediction |

### Sample Request

```json
POST /predict
{
  "budget": 50000000,
  "popularity": 45.0,
  "runtime": 120,
  "vote_average": 7.5
}
```

### Sample Response

```json
{
  "prediction": "Hit",
  "confidence": "88.0%",
  "input_received": {
    "budget": 50000000,
    "popularity": 45.0,
    "runtime": 120,
    "vote_average": 7.5
  }
}
```

### Run the API Locally

1. Install dependencies
   ```
   pip install fastapi uvicorn joblib pandas
   ```
2. Run the API
   ```
   uvicorn movie_api:app --reload --port 8001
   ```
3. Open interactive docs
   ```
   http://127.0.0.1:8001/docs
   ```

---

## 📊 Dataset

This project uses **The Movies Dataset** from Kaggle:
🔗 [https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

---

## 📋 Features Used for Prediction

| Feature | Typical Range |
|----------------|-------------------------|
| Budget | 1,000,000 – 250,000,000 |
| Popularity | 1 – 150 |
| Runtime | 60 – 240 minutes |
| Vote Average | 1.0 – 10.0 |

> The API uses Pydantic validation to ensure only realistic values are accepted.

---

## 🧠 Machine Learning

- **Model**: Logistic Regression
- **Target Variable**: Success_Label (`Hit` or `Flop`)
- **Accuracy Achieved**: ~95%
- **Metrics**: Precision, Recall, F1-score, Accuracy

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy, Seaborn, Matplotlib**
- **Scikit-learn**
- **Streamlit** — Web app
- **FastAPI** — REST API framework
- **Pydantic** — Input validation
- **Joblib** — Model loading
- **Uvicorn** — ASGI server
- **Git & GitHub**

---

## 🖥️ How to Run Locally

### Streamlit Web App
1. Clone the repo
   ```
   git clone https://github.com/MohammedChoudhary/Movies_Predictor.git
   ```
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
3. Run the app
   ```
   streamlit run app.py
   ```

### FastAPI REST API
1. Install dependencies
   ```
   pip install fastapi uvicorn joblib pandas
   ```
2. Run the API
   ```
   uvicorn movie_api:app --reload --port 8001
   ```
3. Open docs at `http://127.0.0.1:8001/docs`

---

## 🙋‍♂️ Author

**Mohammed Choudhary**
🔗 [LinkedIn](https://www.linkedin.com/in/mohammedchoudhary)
📧 mohammedcm7007@gmail.com

---

## 📌 License

This project is licensed under the MIT License.
