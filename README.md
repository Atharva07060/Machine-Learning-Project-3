## 📉 Telco Customer Churn Prediction – Flask + ML App

This project uses machine learning to predict whether a telecom customer is likely to **churn (i.e., leave the service)** based on their demographic, account, and service usage details. It includes a **Flask web application** that allows users to enter customer details and get instant churn predictions, along with the probability score.

---

### 🚀 Key Features

* ✅ **Machine Learning Model for Churn Prediction**
* 📊 **User-friendly Web Interface with Flask**
* 🧹 **Input Preprocessing and Encoding Logic Built-In**
* 🧠 **Displays Churn Risk Prediction and Probability**
* 💾 **Model Loaded with Joblib**
* 🛡️ **Error Handling for Missing or Corrupt Data**

---

### 🛠️ Tech Stack

| Component    | Tech Used                    |
| ------------ | ---------------------------- |
| Language     | Python                       |
| Backend      | Flask                        |
| ML Libraries | scikit-learn, pandas, joblib |
| Web UI       | HTML, Jinja2 Templates       |

---

### 📂 Project Structure

```
Telco_Churn_Prediction/
│
├── app.py                    # Flask web app (main entry point)
├── churn_model.pkl           # Trained ML model (must be generated first)
├── templates/
│   └── index.html            # UI for input form and result display
├── static/                   # (Optional) For CSS, JS, images
├── train_model.py            # Script to train and export churn_model.pkl
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

---

### 📌 How to Use

#### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/Telco_Churn_Prediction.git
cd Telco_Churn_Prediction
```

#### 📦 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

#### 🧠 Step 3: Train the Model (if `churn_model.pkl` doesn’t exist)

```bash
python train_model.py
```

#### 🚀 Step 4: Run the Flask App

```bash
python app.py
```

Then open your browser and go to:
👉 `http://127.0.0.1:5000`

---

### 🖥️ App Demo Flow

1. Enter customer details (tenure, contract type, payment method, etc.)
2. Hit **Submit**
3. See:

   * ✅ **Prediction:** Will the customer churn? (Yes/No)
   * 📈 **Probability:** How confident is the model?

---

### 🧪 Model Details

* **Type:** Classification
* **Algorithm:** Random Forest (or your selected model)
* **Features Used:**
  `gender`, `SeniorCitizen`, `tenure`, `InternetService`, `Contract`, `MonthlyCharges`, `TotalCharges`, etc.

---

### 📈 Evaluation Metrics (from training script)

* Accuracy, Precision, Recall
* ROC-AUC Score
* Confusion Matrix

---

### 📌 Future Improvements

* Add model explainability using SHAP or LIME
* Save user inputs for analytics
* Improve UI styling (Bootstrap integration)
* Deploy on Render / Heroku / Railway / AWS

---



Let me know if you want a ready-made `requirements.txt`, `index.html` template, or `train_model.py` boilerplate to match this setup!
