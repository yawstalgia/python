# My shot at the "Guess the number" program
import random

# Get the user's name
print('Hi, what is your name?')
userName = input()
print('Nice to meet you, ' + str(userName))

# Produce the secret number
upperLimit = 20
guessesLimit = 6
secretNumber = random.randint(1, upperLimit)

print('Hey I am thinking of a number between 1 and ' + str(upperLimit) + '. I will give you ' + str(guessesLimit) + ' guesses.')


# Get the user guess
for userGuessTimes in range (1, guessesLimit+1):
    print('Take a guess.')
    userGuess = input()

    try:
        # guess higher and lower
        userGuess = int(userGuess)

        print('Guess #' + str(userGuessTimes))

        if userGuess > secretNumber:
            print('Your guess is too high.')
        elif userGuess < secretNumber:
            print('Your guess is too low.')
        else:
            print('You got it! My number is ' + str(secretNumber) + '.')
            break

        # heating up range
        if userGuess > (secretNumber - 2) and userGuess < (secretNumber + 2):
            print('You are getting hot.')

    except ValueError:
        print('You have to give a number in Arabic numerical format.')        


# Output ultimate results
if userGuess == secretNumber:
    print('Good job, ' + userName + '. ')
    print('That was fun. It took you ' + str(userGuessTimes) + ' guesses.')
elif userGuess != secretNumber:
    print('Oh no, ' + userName + '! You missed it. It was ' + str(secretNumber) + '.')
    
