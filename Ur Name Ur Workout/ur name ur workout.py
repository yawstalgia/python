'''
Script: Your Name Your Workout (v0.2)
Author: @zeroyaw (Yaw Asare)
Date: 4-17-2020
Purpose/background: I came across an IG post where you use the letters of your name to create a workout. I thought this would be great to make into a script
'''


####### Defining the functions

# Function to show the user what this app is about
def appHeader():
    print()
    asteriskLine(2)
    print()
    print('Your Name Your Workout (v0.2)')
    print('Instructions: Type your name and get a workout!')
    print()
    asteriskLine(1)

# Function to print a line of asterisks
def asteriskLine(numberOfLines):
    for i in range(numberOfLines):
        print('************************************************************')

# Function to get the user's name
def getName():
    print()
    print('Please enter your name')
    userName = input()
    print()
    return userName

# Function to remove any invalid characters or errors in the user's name
def cleanseName(userName):
    userNameFiltered = ""

    for j in range(len(userName)):
        for k in range(65,123):
            if k > 90 and k < 97:
                continue
            if ord(userName[j]) == k:
                userNameFiltered = userNameFiltered + userName[j].lower()

    return userNameFiltered

# Function to check to see if the user's name is blank
def checkNameBlank(userName):
    itsBlank = True

    if userName == '':
        itsBlank = True
    else:
        itsBlank = False

    return itsBlank

# Function to get the user's full workout by going through each letter
def getFullWorkout(userName):
    print('Here is your workout:')
    print()
    for i in range(len(userName)):
        print(userName[i].upper() + ': ' + getOneExercise(userName[i]))

# GetExercise... function to get the exercise for each letter
def getOneExercise(z):
    exerciseOutput = ""

    if z == "a":
        exerciseOutput = "10 mountain climbers"
    elif z == "b":
        exerciseOutput = "25 crunches"
    elif z == "c":
        exerciseOutput = "10 burpees"
    elif z == "d":
        exerciseOutput = "1 minute plank"
    elif z == "e":
        exerciseOutput = "20 pushups"
    elif z == "f":
        exerciseOutput = "15 jumping jacks"
    elif z == "g":
        exerciseOutput = "20 alternate lunges"
    elif z == "h":
        exerciseOutput = "10 full situps"
    elif z == "i":
        exerciseOutput = "1 minute wall sit"
    elif z == "j":
        exerciseOutput = "15 plank jacks"
    elif z == "k":
        exerciseOutput = "12 star jumps"
    elif z == "l":
        exerciseOutput = "15 sumo squats"
    elif z == "m":
        exerciseOutput = "15 tricep dips"
    elif z == "n":
        exerciseOutput = "30 crunches"
    elif z == "o":
        exerciseOutput = "15 plank jacks"
    elif z == "p":
        exerciseOutput = "15 glute bridges"
    elif z == "q":
        exerciseOutput = "10 squat jumps"
    elif z == "r":
        exerciseOutput = "15 calf raisers"
    elif z == "s":
        exerciseOutput = "20 high knees"
    elif z == "t":
        exerciseOutput = "20 Russian twists"
    elif z == "u":
        exerciseOutput = "10 tricep dips"
    elif z == "v":
        exerciseOutput = "12 toe touches"
    elif z == "w":
        exerciseOutput = "30 second wall sit"
    elif z == "x":
        exerciseOutput = "10 tuck jumps"
    elif z == "y":
        exerciseOutput = "20 supermans"
    elif z == "z":
        exerciseOutput = "10 side lunges"

    return exerciseOutput

# Function to get user's request to rerun the program
def rinseRepeat(firstRunTest):
    if firstRunTest == 0:
        return True
    elif firstRunTest > 0:
        print('Would you like to get another workout (y/n)')
        shouldWeRestart = input()

        if shouldWeRestart.lower() == "y" or shouldWeRestart.lower() == "yes":
            return True
        else:
            return False

# Function to send the user off
def appEnd():
    print()
    print('Good luck!')
    print()
    asteriskLine(2)





####### Body of the script

appHeader()
runs = 0

while rinseRepeat(runs) == True:
    userName = ""

    while checkNameBlank(userName) == True:
        userName = getName()
        userName = cleanseName(userName)
    else:
        getFullWorkout(cleanseName(userName))
        runs += 1
        print()

appEnd()













