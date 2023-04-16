'''
Day 13: Debugging
'''

#exercises

############DEBUGGING#####################

# Describe Problem
#def my_function():
#    #for i in range(1, 20): range is exclusive on second parameter, need to increase to hit 20 in the loop and access the if statement
#	for i in range(1, 21):
#		if i == 20:
#			print("You got it")
#my_function()

# Reproduce the
#index error in choosing from dice_imgs, change range on randint function to be from 0-5 to match array indexes
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# #dice_num = randint(1, 6)
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer
#need to change conditionals so that years 1980 and 1994 return instead of just exiting
# year = int(input("What's your year of birth?"))
# #if year > 1980 and year < 1994:
# if year >= 1980 and year <1994:
#   print("You are a millenial.")
# #elif year > 1994:
# elif year >=1994:
#   print("You are a Gen Z.")

# Fix the Errors
#indentation error for the print statement
#type error for age value, needs to be cast to an int
#add f before string to support f-string usage of age variable in print statement
# age = input("How old are you?")
# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")
#     print(f"You can drive at age {age}")

#Print is Your Friend
#change equivalence to assignment operator for word_per_page variable
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"words per page = {word_per_page}")
# print(total_words)

# #Use a Debugger
#change location of append to occur inside of the for loop to properly mutate list
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   #b_list.append(new_item)
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])