import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
import matplotlib.pyplot as plt

# Sample synthetic data (you can replace with real data)
np.random.seed(42)
n_samples = 1000

data = pd.DataFrame({
    'age': np.random.randint(30, 80, n_samples),
    'bmi': np.random.uniform(18, 40, n_samples),
    'systolic_bp': np.random.randint(100, 180, n_samples),
    'diastolic_bp': np.random.randint(60, 120, n_samples),
    'cholesterol': np.random.uniform(150, 300, n_samples),
    'glucose': np.random.uniform(70, 200, n_samples),
    'smoker': np.random.randint(0, 2, n_samples),
    'diabetic': np.random.randint(0, 2, n_samples),
    'risk': np.random.randint(0, 2, n_samples)  # 1 = high risk, 0 = low risk
})

# Features and labels
X = data.drop('risk', axis=1)
y = data['risk']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train_scaled, y_train)

# Predict
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print(f"ROC AUC Score: {roc_auc_score(y_test, y_proba):.2f}")

# Plot ROC Curve
RocCurveDisplay.from_predictions(y_test, y_proba)
plt.title("ROC Curve - Patient Risk Stratification")
plt.show()
