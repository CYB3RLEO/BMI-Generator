weight = input("Enter weight (kg): ")
height = input("Enter height (m): ")

bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is {bmi:.1f}, categorized as {category}.")