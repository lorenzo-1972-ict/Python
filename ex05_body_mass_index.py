# python script to compute the BMI

weight = input("\nWhat is your weight (Kg)? ")
height = input("\nWhat is your height (m)? ")
bmi = float (int(weight) / (float(height) * float(height)))

print(float(height) ** 2)

if bmi < 18.5:
    result = "Underweight"

if 18.5 < bmi < 25:
    result = "Normal build"

if 25 < bmi < 30:
    result = "Overweight"

else:
    result = "Obesity"

print ("\nYour BMI status is:", result,"\n")