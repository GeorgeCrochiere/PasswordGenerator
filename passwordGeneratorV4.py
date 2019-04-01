import random
from Tkinter import *

def getRandomChar(arr):
    x = random.randint(0, len(arr) - 1)
    charToAdd = arr[x]
    return charToAdd

def generatePassword(length, complexity):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbols = ['!','@','#','$']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    password = ''
    for i in range(0, length):
        chooseCharacter=random.randint(1,complexity)
        if chooseCharacter == 1:
            charToAdd = getRandomChar(letters)
        if chooseCharacter == 2:
            charToAdd = getRandomChar(numbers)
        if chooseCharacter == 3:
            charToAdd = getRandomChar(symbols)
        password += charToAdd
    return password

def onClick():
    passwordTextBox.delete(1.0,END)
    passwordTextBox.insert(END, (generatePassword(int(lengthText.get(1.0, END)), complexity.get())))

root = Tk()
global complexity
complexity = IntVar()
global lengthText
global passwordTextBox

label = Label(root, text = 'Length:')
lengthText = Text(width = 5, height = 1)
lengthText.insert(END, 8)
lengthText.see(END)
label.grid(row = 0, column = 0)
lengthText.grid(row = 0, column = 1)

complexLabel = Label(root, text = 'Complexity:')
complexLabel.grid(row = 1, column = 0)
L1 = Radiobutton(root, text = 'Level 1: Letters', variable = complexity, value = 1)
L2 = Radiobutton(root, text = 'Level 2: Letters and Numbers', variable = complexity, value = 2)
L3 = Radiobutton(root, text = 'Level 3: Letters, Numbers, and Symbols', variable = complexity, value = 3)
L1.grid(row = 1, column = 1)
L2.grid(row = 2, column = 1)
L3.grid(row = 3, column = 1)

passwordTextBox = Text(width = 30, height = 2)
passwordTextBox.grid(row = 4, column = 0, columnspan = 2)

generate = Button(root, text = 'Generate!', command=onClick)
generate.grid(row = 5, column = 0, columnspan = 2)

root.mainloop()
