'''
Day 10 topics:
-functions with outputs

Project:
-Calculator
'''

'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapYear = is_leap(year)
    if (month == 2) and (leapYear == True):
        return 29
    else:
        return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
'''

#Project

#operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = float(input("What is the first number?: "))
    for operator in operations:
        print(operator)
    loop = True
    while loop:
        operation_chosen = input("Pick an operation from the list above: ")
        num2 = float(input("What is the next number?: "))
        calculation = operations[operation_chosen]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_chosen} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ") == 'y':
            num1 = answer
        else:
            loop = False
            calculator()


calculator()
