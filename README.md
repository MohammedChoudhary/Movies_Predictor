**🎬 Movie Success Predictor**

This project predicts whether a movie will be a **Hit** or **Flop** based on various numerical features like budget, popularity, runtime, vote count, and vote average.

It includes:
- Data preprocessing and EDA using **Pandas, Matplotlib, Seaborn**
- Machine Learning models like **Logistic Regression**
- A web app using **Streamlit**
- Deployment on **Streamlit Cloud**
- A clean and minimal UI for interaction

---

##  Live App

👉 [Try the Web App](https://moviespredictor-zgvh3sy2f84f2vptkumydf.streamlit.app/)

---

**📊 Dataset**

This project uses **The Movies Dataset** from Kaggle:  
🔗 [https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

---

##  Features Used for Prediction

| Feature        | Typical Range           |
|----------------|-------------------------|
| Budget         | 1,000,000 – 250,000,000 |
| Popularity     | 1 – 150                 |
| Runtime        | 60 – 240 minutes        |
| Vote Count     | 0 – 50,000+             |
| Vote Average   | 1.0 – 10.0              |

> The app uses input validation to ensure users enter realistic values.

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
- **Streamlit**
- **Joblib**
- **Git & GitHub**

---

## 🖥️ How to Run Locally

1. Clone the repo  
   `git clone https://github.com/MohammedChoudhary/Movies_Predictor.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the app  
   `streamlit run app.py`

---

## 🙋‍♂️ Author

**Mohammed Choudhary**  
🔗 [LinkedIn](https://www.linkedin.com/in/mohammedchoudhary)  
📧 choudhary@example.com *(replace with your email)*

---

## 📌 License

This project is licensed under the MIT License.
