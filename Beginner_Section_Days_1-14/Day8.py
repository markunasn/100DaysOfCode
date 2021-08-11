'''
Day 8 topics:
-functions with inputs
-arguments and parameters
Project:
-Caesar cipher encoder
'''
import math
'''
def greet(name):
    print(f'hello {name}')
    print(f'hola{name}')
    print(f'bonjour {name}')


def greetLocation(name, location):
    print(f'hello {name}')
    print(f'What is it like in {location}')
    print(f'bonjour {name}')


def paintCalculator(width, height, coverage):
    area = width * height
    numCans = math.ceil(area/coverage)
    print(f'You will need {numCans} cans to cover the wall.')

wallHeight = int(input("Height of the wall is:"))
wallWidth = int(input("Width of the wall is:"))
canSize = int(input("A can covers how many square feet:"))

paintCalculator(width=wallWidth,height=wallHeight,coverage=canSize)
'''
#Caesar cipher project
def encrypt(message, shiftAmount):
    cipheredText = ""
    for letter in message:
        position = alphabet.index(letter)
        shiftedPostion = position + shiftAmount
        newLetter = alphabet[shiftedPostion]
        cipheredText += newLetter
    print(f'Encoded message is {cipheredText}.')

def decrypt(message, shiftAmount):
    decipheredText = ''
    for letter in message:
        position = alphabet.index(letter)
        shiftedPosition = position - shiftAmount
        newLetter = alphabet[shiftedPosition]
        decipheredText += newLetter
    print(f'Decoded message is {decipheredText}.')

def caesar(message, shiftAmount, shiftDirection):
    if shiftDirection == 'encode':
        encrypt(message,shiftAmount)
    elif shiftDirection == 'decode':
        decrypt(message,shiftAmount)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(message=text,shiftAmount=shift,shiftDirection=direction)