'''
Day 4 topics:
-Lists
-Randomisation
'''

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random
#Write your code below this line 👇
choice = random.randint(0,len(names) -1)
print(names[choice]+" is going to buy the meal today!")

