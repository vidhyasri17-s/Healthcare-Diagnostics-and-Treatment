import datetime

# Data class for maternal health
class Mother:
    def __init__(self, name, age, weeks_pregnant, blood_pressure, weight, fetal_movement_per_day):
        self.name = name
        self.age = age
        self.weeks_pregnant = weeks_pregnant
        self.blood_pressure = blood_pressure  # (systolic, diastolic)
        self.weight = weight  # in kg
        self.fetal_movement_per_day = fetal_movement_per_day

    def assess_risks(self):
        risks = []
        if self.blood_pressure[0] > 140 or self.blood_pressure[1] > 90:
            risks.append("⚠️ High blood pressure (risk of preeclampsia)")
        if self.age > 35:
            risks.append("⚠️ High maternal age")
        if self.fetal_movement_per_day < 10:
            risks.append("⚠️ Low fetal movement")
        if self.weeks_pregnant > 40:
            risks.append("⚠️ Post-term pregnancy")

        return risks if risks else ["✅ No significant maternal health risks detected."]


# Data class for child health
class Child:
    def __init__(self, name, age_months, weight, height, vaccinations_received):
        self.name = name
        self.age_months = age_months
        self.weight = weight  # in kg
        self.height = height  # in cm
        self.vaccinations_received = vaccinations_received

    def check_growth(self):
        if self.age_months < 6 and self.weight < 5:
            return "⚠️ Underweight for age (infant)"
        elif self.age_months >= 12 and self.height < 70:
            return "⚠️ Below-average height for age"
        return "✅ Growth within normal range."

    def check_vaccinations(self):
        required = ["BCG", "DTP", "Polio", "HepB", "MMR"]
        missing = [v for v in required if v not in self.vaccinations_received]
        if missing:
            return f"⚠️ Missing vaccinations: {', '.join(missing)}"
        return "✅ All essential vaccinations received."


# Interface
def monitor_health():
    print("📋 Maternal and Child Health Monitoring System\n")

    mother = Mother(
        name=input("Enter mother's name: "),
        age=int(input("Mother's age: ")),
        weeks_pregnant=int(input("Weeks of pregnancy: ")),
        blood_pressure=(
            int(input("Systolic BP: ")),
            int(input("Diastolic BP: "))
        ),
        weight=float(input("Mother's weight (kg): ")),
        fetal_movement_per_day=int(input("Fetal movements per day: "))
    )

    print("\n--- Maternal Health Assessment ---")
    for risk in mother.assess_risks():
        print(risk)

    print("\nNow entering child data...\n")

    child = Child(
        name=input("Child's name: "),
        age_months=int(input("Child's age (in months): ")),
