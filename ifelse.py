age = input('whats your age?\n') #take age input

if int(age) < 5 or int(age) == 5:
    print('you are a baby')

elif int(age) < 12 or int(age) == 12:
    print('you are a kid')

elif int(age) < 16 or int(age) == 16:
    print('you are a teen')

else:
    print('you are an adult')

