import sys, time, os
import random

message = '''Welcome to the game. Based on your level, you have to guess a 3, 4 or 5 digit number with their correct position.
This intuitive game will help you empower your probablistic and mental maths strenghts \n'''
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
    
print("Type the level of your game ['Easy', 'Medium', 'Hard']")
level = input('> ')
if level.lower().startswith('e'):
    NUM_DIGITS = 3
    MAX_GUESSES = 15
elif level.lower().startswith('m'):
    NUM_DIGITS = 4
    MAX_GUESSES = 10
elif level.lower().startswith('h'):
    NUM_DIGITS = 5
    MAX_GUESSES = 8


def main():
    print('''Guesser, a deductive logic game.
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    What I say:    What it means:
      Alan         One digit is correct but in the wrong position.
      Neon         One digit is correct and in the right position.
      Unix         No digit is correct.

    For a 3 digit number, if the secret number is 786 and you guessed 684, the clues will be Alan Neon'''.format(NUM_DIGITS))
    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretnum = getSecretNum()
        print('I have thought a {} digit number without repetition.'.format(NUM_DIGITS))
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
        current_guess = 1
        while current_guess <= MAX_GUESSES:
            input_num = ''
            # Keep looping until user enter a valid number:
            while len(input_num) != NUM_DIGITS or not input_num.isdecimal():
                print('Guess #{}: '.format(current_guess))
                input_num = input('> ')
            clues = getClues(input_num, secretnum)
            print(clues)
            current_guess += 1
            if input_num == secretnum:
                print('You got it!')
                break
            if current_guess > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretnum))
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretnum = ''
    for i in range(NUM_DIGITS):
        secretnum += str(numbers[i])
    return secretnum

def getClues(input_num, secretnum):
    clues = []
    for i in range(len(input_num)):
        if input_num[i] == secretnum[i]:
            # A correct digit is in the correct place.
            clues.append('Neon')
        elif input_num[i] in secretnum:
            # A correct digit is in the incorrect place.
            clues.append('Alan')
    if len(clues) == 0:
        return 'Unix'  # There are no correct digits at all.
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
