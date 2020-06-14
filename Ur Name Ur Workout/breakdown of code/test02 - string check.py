print()
print('Provide input')
charRaw = input()
print()

print('you typed this:')
print(charRaw)
print()

#for i in range(len(charRaw)):
#    print('Character #:')
#    print(i)
#    print('is:')
#    print(charRaw[i])
#    print('and its Unicode number is:')
#    print(ord(charRaw[i]))
#    print()

#    print('Character #' + str(j) + ', which is, ' + charRaw[j] + ', is:')


# removal of non text characters
newCharRaw = ""
for j in range(len(charRaw)):
    for k in range(65,123):
        if ord(charRaw[j]) == k:
            newCharRaw = newCharRaw + charRaw[j]

print('These are the only letters:')            
print(newCharRaw)
