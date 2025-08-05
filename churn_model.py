# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("Telco-Customer-Churn.csv")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
df.drop('customerID', axis=1, inplace=True)

for col in df.select_dtypes(include='object').columns:
    if col != 'Churn':
        df[col] = pd.factorize(df[col])[0]
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

X = df.drop('Churn', axis=1)
y = df['Churn']

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "churn_model.pkl")
print("✅ Model saved as churn_model.pkl")
