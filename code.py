# Disease Prediction System (Basic Python - No Libraries)

print("=== Disease Prediction System ===")

# Taking user input
fever = input("Do you have fever? (yes/no): ")
cough = input("Do you have cough? (yes/no): ")
headache = input("Do you have headache? (yes/no): ")
fatigue = input("Do you feel fatigue? (yes/no): ")
cold = input("Do you have cold? (yes/no): ")

# Convert to lowercase (for safety)
fever = fever.lower()
cough = cough.lower()
headache = headache.lower()
fatigue = fatigue.lower()
cold = cold.lower()

# Prediction logic
if fever == "yes" and cough == "yes" and fatigue == "yes":
    disease = "Flu"
elif cough == "yes" and cold == "yes":
    disease = "Common Cold"
elif headache == "yes" and fatigue == "yes":
    disease = "Migraine"
elif fever == "yes" and headache == "yes":
    disease = "Viral Fever"
else:
    disease = "You seem Healthy or symptoms are unclear"

# Output result
print("\nPredicted Disease:", disease)

# Suggestions
print("\n--- Suggestions ---")
if disease == "Flu":
    print("Rest, drink warm fluids, take paracetamol")
elif disease == "Common Cold":
    print("Stay hydrated, take steam, rest well")
elif disease == "Migraine":
    print("Avoid stress, take proper sleep")
elif disease == "Viral Fever":
    print("Consult doctor, take proper medication")
else:
    print("Maintain healthy lifestyle")
