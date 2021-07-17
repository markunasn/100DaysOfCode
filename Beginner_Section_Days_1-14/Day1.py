'''
Day 1 Topics:
-Printing to console
-Taking input
-Basic string manipulation
-basic variables
Project - Band Name Generator
'''


#creates a band name by taking user input of home town and a pet and concatenates them
print("Welcome to the Band Name Generator")
city = input("Please enter the city you grew up in: ")

pet = input("Please enter the name of a pet: ")

bandName = city + " " + pet

print("A band name could be: " + bandName)