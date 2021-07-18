'''
Day 2 Topics:
-Primitive data types
-casting
-F strings
-mathematical operations

Project - Tip Calculator
'''

#Time left practice problem
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yearsLeft = 90-int(age)
days = yearsLeft * 365
weeks = yearsLeft * 52
months = yearsLeft * 12

print(f"You have {days}, {weeks} weeks, and {months} months left.")

#Project
bill = input("Enter your bill: ")
tip = input("Enter your tip percentage: ")
splitwise = input("How many ways would you like to split the bill: ")

percentage = float("1."+tip)
#quick and dirty way, won't catch edge cases of trying to tip more than the bill

total = float(bill) * percentage
share = total / int(splitwise)
share = round(share, 2)
print("Each person should pay $" +str(share))