Def diagnose(symptoms):
Diagnosis = *
Treatment="
# Simple rules (for illustration only, not medical advice)
If fever' in symptoms and 'cough' in symptoms and fatigue' in symptoms:
Diagnosis = "Flu"
Treatment = "Rest, fluids, and antiviral medications if needed"
Elif 'chest pain' in symptoms and 'shortness of breath' in symptoms:
Diagnosis = "Possible heart issue"
Treatment = Immediate medical attention, ECG, and further
cardiology evaluation* Elif 'headache' in symptoms and 'nausea' in symptoms:
Diagnosis = "Migraine"
Treatment = "Pain relief, dark room, possible prescription
medication" Else:
Diagnosis = "Unknown"
Treatment = "Recommend clinical consultation for further diagnosis"
Retur diagnosis, treatment
# Example usage
Symptoms = [fever', 'cough', 'atigue"]
Diagnosis, treatment = diagnose(symptoms)
Print(" Diagnosis: (diagnosis)")
Print("Recommended Treatment: (treatment)")