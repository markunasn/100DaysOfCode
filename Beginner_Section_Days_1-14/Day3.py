'''
Day 3 Topics:
-conditionals
-logical operators
'''

#BMI calculator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI =round(weight / height ** 2)

if BMI < 18.5:
	print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
	print(f"Your BMI is {BMI}, you are a normal weight")
elif BMI < 30:
	print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI < 35:
	print(f"Your BMI is {BMI}, you are obese")
else:
	print(f"Your BMI is {BMI}, you are clinically obese")


#Leap year calculator
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("Leap year.")
		else:
			Print("Not a leap year")
	else:
		print('Leap year')
else:
	print("Not leap year.")
