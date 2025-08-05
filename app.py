from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "churn_model.pkl")
if not os.path.exists(model_path):
    raise FileNotFoundError("❌ churn_model.pkl not found. Run train_model.py first.")
model = joblib.load(model_path)

# Define input features
features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
            'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
            'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
            'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
            'MonthlyCharges', 'TotalCharges']

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None

    if request.method == "POST":
        input_data = {f: request.form.get(f) for f in features}
        df = pd.DataFrame([input_data])

        # Convert numeric fields
        for field in ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']:
            df[field] = pd.to_numeric(df[field], errors='coerce').fillna(0)

        # Encode categorical variables
        for col in df.select_dtypes(include='object').columns:
            df[col] = pd.factorize(df[col])[0]

        # Align with model features
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0
        df = df[model.feature_names_in_]

        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

    return render_template("index.html", prediction=prediction, probability=probability)

# ✅ Entry point to start Flask server
if __name__ == "__main__":
    print("✅ Starting Flask server...")
    app.run(debug=True)
