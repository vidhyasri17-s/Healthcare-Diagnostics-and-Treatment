import tkinter as tk
from tkinter import messagebox

# Basic rules-based diagnosis system
def diagnose(symptoms):
    symptoms = symptoms.lower()
    if 'fever' in symptoms and 'cough' in symptoms:
        return "Possible Condition: Flu\nTreatment: Rest, hydration, antiviral meds if needed."
    elif 'chest pain' in symptoms and 'shortness of breath' in symptoms:
        return "Possible Condition: Heart Issue\nTreatment: Seek immediate medical attention."
    elif 'headache' in symptoms and 'nausea' in symptoms:
        return "Possible Condition: Migraine\nTreatment: Pain relievers, dark room, rest."
    elif 'fatigue' in symptoms and 'weight loss' in symptoms:
        return "Possible Condition: Diabetes or Thyroid Issue\nTreatment: Blood tests and consultation."
    else:
        return "Diagnosis unclear. Please consult a healthcare provider."

# Function triggered on button click
def get_diagnosis():
    symptoms = symptom_entry.get()
    if not symptoms.strip():
        messagebox.showwarning("Input Error", "Please enter symptoms.")
        return
    result = diagnose(symptoms)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# UI Setup
root = tk.Tk()
root.title("Healthcare Diagnosis App")
root.geometry("500x400")
root.config(padx=20, pady=20)

# Header
header = tk.Label(root, text="Healthcare Diagnosis & Treatment", font=("Helvetica", 16, "bold"))
header.pack(pady=10)

# Symptom entry
symptom_label = tk.Label(root, text="Enter your symptoms (comma-separated):", font=("Helvetica", 12))
symptom_label.pack(anchor="w")
symptom_entry = tk.Entry(root, width=50)
symptom_entry.pack(pady=5)

# Diagnose button
diagnose_btn = tk.Button(root, text="Get Diagnosis", command=get_diagnosis, bg="#4CAF50", fg="white", font=("Helvetica", 12))
diagnose_btn.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Diagnosis & Treatment:", font=("Helvetica", 12))
result_label.pack(anchor="w")
result_text = tk.Text(root, height=10, width=60)
result_text.pack(pady=5)

# Run the app
root.mainloop()
