from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Healthcare Diagnosis and Treatment API")

# --- Data Models ---

class PatientInfo(BaseModel):
    name: str
    age: int
    gender: str
    symptoms: List[str]

class DiagnosisResult(BaseModel):
    diagnosis: str
    recommended_treatment: str

# --- Rule-based Diagnostic Engine ---

def diagnose(symptoms: List[str]) -> DiagnosisResult:
    symptom_set = set(symptoms)

    # Simplified rule-based logic
    if {"fever", "cough", "fatigue"}.issubset(symptom_set):
        return DiagnosisResult(
            diagnosis="Likely Flu or COVID-19",
            recommended_treatment="Rest, fluids, and consult a doctor for testing"
        )
    elif {"headache", "sensitivity to light", "stiff neck"}.issubset(symptom_set):
        return DiagnosisResult(
            diagnosis="Possible Meningitis",
            recommended_treatment="Immediate hospital visit recommended"
        )
    elif {"chest pain", "shortness of breath", "dizziness"}.issubset(symptom_set):
        return DiagnosisResult(
            diagnosis="Possible Heart Issue",
            recommended_treatment="Call emergency services immediately"
        )
    else:
        return DiagnosisResult(
            diagnosis="Symptoms not recognized",
            recommended_treatment="Consult a healthcare provider for further evaluation"
        )

# --- API Routes ---

@app.post("/diagnose", response_model=DiagnosisResult)
def get_diagnosis(patient: PatientInfo):
    if not patient.symptoms:
        raise HTTPException(status_code=400, detail="No symptoms provided")
    return diagnose(patient.symptoms)

@app.get("/")
def root():
    return {"message": "Healthcare Diagnosis API is running"}

