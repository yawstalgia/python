import random

print('Put in a number between 1 and 10 and I will see if I can guess it!')
userNumber = input()
print()

numberOfGuesses = 0

while True:
    compGuess = random.randint(1, 10)
    numberOfGuesses = numberOfGuesses + 1
    if compGuess == int(userNumber):
        print('I got it right!! Your number is: ' + str(userNumber))
        break
    else:
        print('Hmm... I guess ' + str(compGuess) + '. Missed didnt I? I will try again!')

print()
print('It took me ' + str(numberOfGuesses) + ' tries to get it right.')

