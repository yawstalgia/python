print('Provide a letter')
charRaw = input()
charNum = ord(charRaw)

print()
print('you typed this:')
print(charRaw)

print()
print('the unicode number of ' + str(charRaw) + ' is:')
print(charNum)

print()
print('the string rep of ' + str(charNum) + ' is:')
print(chr(charNum))
print('which should also be:')
print(charRaw)

