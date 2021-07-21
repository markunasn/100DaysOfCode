'''
Day 5 tops:
-loops

Project - Password Generator
'''
'''
#Average height calculator, not able to use len() or sum() funtions

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

counter = 0
total = 0
for height in student_heights:
	total += height
	counter += 1

avgHeight = total / counter
print(int(avgHeight))
'''
'''
#FizzBuzz problem
for num in range(1,101):
	output = ''
	if num % 3 == 0:
		output += 'Fizz'
	if num % 5 == 0:
		output += 'Buzz'
	elif len(output) == 0:
		output = num
	print(output)
'''
#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#generates in order each time, not randomised
password = ''
pwdList = []
for i in range(0,nr_letters):
    password += random.choice(letters)
    pwdList.append(random.choice(letters))
for i in range(0,nr_numbers):
    password += random.choice(numbers)
    pwdList.append(random.choice(numbers))
for i in range(0,nr_symbols):
    password += random.choice(symbols)
    pwdList.append(random.choice(symbols))
print(password)

#generates password with order of characters randomised
random.shuffle(pwdList)
shuffled = ''
for character in pwdList:
    shuffled += character
print(shuffled)