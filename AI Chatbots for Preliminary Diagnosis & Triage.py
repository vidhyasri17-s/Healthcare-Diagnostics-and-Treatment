import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Symptom-to-condition mapping (simplified)
symptom_conditions = {
    'fever': ['flu', 'common cold', 'COVID-19'],
    'cough': ['bronchitis', 'common cold', 'COVID-19'],
    'headache': ['migraine', 'tension headache', 'dehydration'],
    'chest pain': ['heart attack', 'angina', 'anxiety'],
    'shortness of breath': ['asthma', 'COVID-19', 'pneumonia'],
    'rash': ['allergy', 'eczema', 'measles'],
    'diarrhea': ['food poisoning', 'gastroenteritis'],
    'sore throat': ['strep throat', 'flu', 'common cold'],
    'nausea': ['pregnancy', 'food poisoning', 'migraine'],
}

# Triage rules
triage_rules = {
    'chest pain': 'Seek emergency medical attention immediately.',
    'shortness of breath': 'Seek medical advice urgently.',
    'fever': 'Monitor and consult a doctor if it persists.',
    'headache': 'Rest and take fluids. Consult if severe.',
    'diarrhea': 'Stay hydrated. See a doctor if it lasts more than 2 days.',
}

# Clean and tokenize input
def extract_keywords(user_input):
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    keywords = [word for word in tokens if word.isalpha() and word not in stop_words]
    return keywords

# Diagnosis engine
def diagnose(symptoms):
    possible_conditions = set()
    advices = set()

    for symptom in symptoms:
        if symptom in symptom_conditions:
            possible_conditions.update(symptom_conditions[symptom])
            if symptom in triage_rules:
                advices.add(triage_rules[symptom])

    if not possible_conditions:
        return ("Sorry, I couldn't identify the condition. Please consult a doctor.", None)
    
    return (f"Based on the symptoms, possible conditions include: {', '.join(possible_conditions)}.", 
            f"Triage Advice: {' '.join(advices) if advices else 'Consider seeing a healthcare professional.'}")

# Main chatbot loop
def chatbot():
    print("🤖 Hi! I'm your health assistant. Tell me about your symptoms.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Take care! If symptoms worsen, seek medical help. 👋")
            break
        keywords = extract_keywords(user_input)
        diagnosis, advice = diagnose(keywords)
        print("Bot:", diagnosis)
        if advice:
            print("Bot:", advice)

# Run chatbot
if __name__ == "__main__":
    chatbot()
