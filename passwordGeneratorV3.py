import random

#Ideas
#   idea generator
#   good password generator

def passwordGenerator():
    print('Welcome to the improved Password Generator.')
    print('Please select your criteria.')
    print(' ')
    length=(int(raw_input('Length of password: ')))
    print('Please select the level of complexity:')
    print(' - 1. Letters')
    print(' - 2. Letters and Numbers')
    print(' - 3. Letters, Numbers, and Symbols')
    complexity=(int(raw_input('Level of Complexity of Password: ')))
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbols=['!','@','#','$']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    password=''
    for i in range(0,length):
        chooseCharacter=random.randint(1,complexity)
        if chooseCharacter==1:
            charToAdd=chooseChar(letters)
        if chooseCharacter==2:
            charToAdd=chooseChar(numbers)
        if chooseCharacter==3:
            charToAdd=chooseChar(symbols)
        password+=charToAdd
    print(password)
    
def chooseChar(arr):
    x=random.randint(0,len(arr)-1)
    charToAdd=arr[x]
    return charToAdd
