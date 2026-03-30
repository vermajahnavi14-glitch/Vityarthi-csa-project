# Vityarthi-csa-project
# 🏥 Disease Prediction System

A simple command-line based Disease Prediction System built using **pure Python** — no external libraries required!

---

## 📋 Description

This program predicts possible diseases based on symptoms entered by the user. It asks a series of yes/no questions and uses rule-based logic to suggest a likely condition along with basic health advice.

---

## 🚀 Features

- Simple and beginner-friendly Python code
- No external libraries or dependencies
- Interactive command-line input
- Predicts 4 common conditions: Flu, Common Cold, Migraine, and Viral Fever
- Provides basic health suggestions for each predicted condition

---

## 🛠️ Requirements

- Python 3.x
- No additional packages needed

---

## ▶️ How to Run

1. **Clone or download** the file to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the script:

```bash
python disease_prediction.py
```

---

## 💬 Sample Usage

```
=== Disease Prediction System ===
Do you have fever? (yes/no): yes
Do you have cough? (yes/no): yes
Do you have headache? (yes/no): no
Do you feel fatigue? (yes/no): yes
Do you have cold? (yes/no): no

Predicted Disease: Flu

--- Suggestions ---
Rest, drink warm fluids, take paracetamol
```

---

## 🔍 Prediction Logic

| Symptoms                          | Predicted Disease |
|-----------------------------------|-------------------|
| Fever + Cough + Fatigue           | Flu               |
| Cough + Cold                      | Common Cold       |
| Headache + Fatigue                | Migraine          |
| Fever + Headache                  | Viral Fever       |
| None of the above match           | Healthy / Unclear |

---

## 💡 Suggestions Provided

| Disease       | Suggestion                                  |
|---------------|---------------------------------------------|
| Flu           | Rest, drink warm fluids, take paracetamol   |
| Common Cold   | Stay hydrated, take steam, rest well        |
| Migraine      | Avoid stress, take proper sleep             |
| Viral Fever   | Consult doctor, take proper medication      |
| Healthy       | Maintain healthy lifestyle                  |

---

## ⚠️ Disclaimer

> This tool is for **educational purposes only**. It is **not a substitute for professional medical advice**. Always consult a qualified healthcare provider for any health concerns.

---

## 👨‍💻 Author

Jahnavi Verma

---

## 📄 License

This project is open-source and free to use for learning and educational purposes.
