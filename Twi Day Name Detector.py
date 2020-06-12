# TWI DAY NAME DETECTOR PROGRAM
# Yaw Asare, June 12 2020
# This is primarily a test of boolean and comparison operators

print()
print('*** TWI DAY NAME DETECTOR ***')
print()
print('Tell me the day of the week you were born and your gender, I will tell you your dayname in Twi')
print()


# getting the user's gender
genderpassed = False

while genderpassed == False:
    print('What is your gender (m/f)?')
    gender = input().lower()

    # check to see if they used the shorthard
    if gender == 'm' or gender == 'ma':
        gender = 'male'
    elif gender == 'f' or gender == 'fem':
        gender = 'female'

    # check to see if there is a male or female selected
    if gender == 'male' or gender == 'female':
        genderpassed = True
    else:
        print('Sorry, but Twi daynames are designated for males and females.')
        print('Would you like to try again (y/n)?')
        tryagain = input().lower()
        
        if tryagain == 'y' or tryagain == 'yes':
            genderpassed = False
        elif tryagain == 'n' or tryagain == 'no':
            genderpassed = True
        else:
            genderpassed = False

    print()


# getting the user's bornday
daypassed = False

while daypassed == False:
    print('What day of the week were you born on?')
    day = input()
    day = day.lower()

    # check to see if they used the shorthand
    if day == 'mon' or day == 'm':
        day = day + 'day'
    elif day == 'tues' or day == 'tu':
        day = day + 'day'
    elif day == 'weds' or day == 'wed':
        day = 'wednesday'
    elif day == 'thurs' or day == 'th' or day == 'thu':
        day = 'thursday'
    elif day == 'fri' or day == 'f':
        day = 'friday'
    elif day == 'sat' or day == 'sa':
        day = 'saturday'
    elif day == 'sun' or day == 'su':
        day = 'sunday'
        
    if day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday':
        print('Sorry, but that is not a day of the week.')
        print('Would you like to try again (y/n)?')
        tryagain = input().lower()

        if tryagain == 'y' or tryagain == 'yes':
            daypassed = False
        elif tryagain == 'n' or tryagain == 'no':
            daypassed = True
        else:
            daypassed = False  
    else:
        daypassed = True

    print()


#giving the user their day name
print()
print('Your day name is: ')

if gender == 'male' and day == 'monday':
    print('Kojo')
elif gender == 'male' and day == 'tuesday':
    print('Kwabena')
elif gender == 'male' and day == 'wednesday':
    print('Kwaku')
elif gender == 'male' and day == 'thursday':
    print('Yaw')
elif gender == 'male' and day == 'friday':
    print('Kofi')
elif gender == 'male' and day == 'saturday':
    print('Kwame')
elif gender == 'male' and day == 'sunday':
    print('Kwasi')
elif gender == 'female' and day == 'monday':
    print('Adjoa')
elif gender == 'female' and day == 'tuesday':
    print('Abena')
elif gender == 'female' and day == 'wednesday':
    print('Akua')
elif gender == 'female' and day == 'thursday':
    print('Yaa')
elif gender == 'female' and day == 'friday':
    print('Afia')
elif gender == 'female' and day == 'saturday':
    print('Amma')
elif gender == 'female' and day == 'sunday':
    print('Akosua')
else:
    print('...Sorry, there is no Twi day name for you.')




