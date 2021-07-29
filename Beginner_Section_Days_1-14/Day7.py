'''
Day 7 project:
-Hangman

Program Flow:
-generate random word
-generate blanks
-get letter guess from user
-check if the letter is in the word
-add to drawing or add to word
-check if all letters guessed or if out of lives
-repeat or break out of core game loop
'''

#generate random word from list
import random
art = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def displayGameState():
    print(art[lives])
    print(display)
lives = 6
wordList = ['aardvark', 'baboon', 'canary', 'dog', 'eagle', 'fish', 'gopher']
word = random.choice(wordList)
display = []
guesses = []
for letter in word:
    display += '_'

#core loop
running = True
while running:
    displayGameState()
    guess = input('Enter a letter: ').lower()
    if guess in guesses:
        print("You've already guessed that letter, guess again.")
    else:
        guesses += guess
        for i in range(len(word)):
            if guess == word[i]:
                display[i] = guess
        if guess not in word:
            lives -= 1
            print(That letter isn't in the word, you lost a life.  You have ' + str(lives) + ' remaining.')
        #End of game check
        if lives == 0:
            print('You lose :(')
            print('The word was ' + word)
            running = False
        if '_' not in display:
            running = False
            print('You win!')
