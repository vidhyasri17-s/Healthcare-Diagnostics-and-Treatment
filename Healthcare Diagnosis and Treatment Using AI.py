import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Step 1: Sample Dataset
# Simulated data: symptoms → diagnosis → treatment
data = {
    'fever': [1, 0, 1, 0, 1, 1, 0],
    'cough': [1, 0, 1, 1, 0, 1, 0],
    'fatigue': [1, 0, 1, 0, 1, 1, 0],
    'headache': [1, 0, 1, 1, 0, 1, 0],
    'age': [25, 34, 45, 50, 29, 60, 40],
    
    # 0: Cold, 1: Flu, 2: COVID-19
    'diagnosis': [0, 0, 1, 2, 1, 2, 0]
}

df = pd.DataFrame(data)

# Diagnosis Labels
diagnosis_labels = {0: 'Common Cold', 1: 'Flu', 2: 'COVID-19'}

# Step 2: Features and Target
X = df[['fever', 'cough', 'fatigue', 'headache', 'age']]
y = df['diagnosis']

# Step 3: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=diagnosis_labels.values()))

# Step 6: Treatment Mapping
treatment_plan = {
    0: "Rest, hydration, and over-the-counter cold meds",
    1: "Antiviral medication, fluids, rest",
    2: "Isolation, oxygen therapy, antivirals if needed"
}

# Step 7: Predict New Patient
new_patient = pd.DataFrame([{
    'fever': 1,
    'cough': 1,
    'fatigue': 1,
    'headache': 1,
    'age': 35
}])

diagnosis_pred = model.predict(new_patient)[0]
diagnosis_name = diagnosis_labels[diagnosis_pred]
recommended_treatment = treatment_plan[diagnosis_pred]

print(f"Diagnosis: {diagnosis_name}")
print(f"Recommended Treatment: {recommended_treatment}")
