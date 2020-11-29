import tkinter as tk
import math

# region Setup
win = tk.Tk()
win.geometry(f"350x200")
win.title("Calculator")
win.resizable(False, False)
#endregion

# region Variables
entryText = tk.StringVar()
isThereADot = False
prevNumber = ""
prevChar = ""
availableSymbols='1234567890.'
#endregion

# region Button Functions
def deleteDigit(event):
    if entryText.get()[-1] == ".":
        global isThereADot
        isThereADot = False
    entryText.set(entryText.get()[:-1])

def deleteEverything(event):
    global isThereADot
    global prevNumber
    global prevChar
    isThereADot = False
    entryText.set("")
    prevNumber = 0
    prevChar = ""

def AddToEntry(event, char):
    if char == ".":
        global isThereADot
        if isThereADot == False and entryText.get() != "":
            entryText.set(entryText.get() + char)
            isThereADot = True
    else:
        entryText.set(entryText.get() + char)


def divideWithOne(event):
    number = entryText.get()
    if number == "":
        return

    number = float(number)
    number = 1 / number
    entryText.set(number)

def square(event):
    number = entryText.get()
    if number == "":
        return

    number = float(number)
    number = math.pow(number, 2)
    entryText.set(number)

def squareRoot(event):
    number = entryText.get()
    if number == "":
        return

    number = float(number)
    number = math.sqrt(number)
    entryText.set(number)


def divide(event):
    global prevNumber
    global prevChar
    number = entryText.get()
    if number == "":
        return

    number = float(number)

    deleteEverything("")
    prevNumber = number
    prevChar = "/"

def multiply(event):
    global prevNumber
    global prevChar
    number = entryText.get()
    if number == "":
        return

    number = float(number)

    deleteEverything("")
    prevNumber = number
    prevChar = "*"

def substraction(event):
    global prevNumber
    global prevChar
    number = entryText.get()
    if number == "":
        return

    number = float(number)

    deleteEverything("")
    prevNumber = number
    prevChar = "-"

def sum(event):
    global prevNumber
    global prevChar
    number = entryText.get()
    if number == "":
        return

    number = float(number)
    deleteEverything("")
    prevNumber = number
    prevChar = "+"


def equals(event):
    global prevNumber
    global prevChar

    number = entryText.get()
    number = float(number)

    if number == "":
        return

    if prevChar == "/":
        number = prevNumber / number
    elif prevChar == "*":
        number = prevNumber * number
    elif prevChar == "-":
        number = prevNumber - number
    elif prevChar == "+":
        number = prevNumber + number

    entryText.set(number)

def negativeOrPositive(event):
    if(entryText.get()[0] != '-'):
        entryText.set("-" + entryText.get())
    else: 
        entryText.set(entryText.get()[1:len(entryText.get())])

# endregion

# region Additional Functions
def addButton(name, function, row, column, stick="nswe"):
    button = tk.Button(win, text=name)
    button.grid(row=row, column=column, stick=stick)
    button.bind("<Button-1>", function)


def addButtonLambda(name, function, row, column, lambdaVar, stick="nswe"):
    button = tk.Button(win, text=name)
    button.grid(row=row, column=column, stick=stick)
    button.bind("<Button-1>", lambda e, temp=lambdaVar: function(e, temp))

def charValidation(char):
    if (char in availableSymbols):
        return True
        
    return False
# endregion

# region Main

validation = win.register(charValidation)
tk.Entry(win, textvariable=entryText, validate='all', validatecommand=(validation, '%S')).grid(row=0, column=0, columnspan=4, stick="nswe")

# 1
addButton(name="<", function=deleteDigit, row=1, column=3)
addButton(name="C", function=deleteEverything, row=1, column=2)

# 2
addButton(name="1/x", function=divideWithOne, row=2, column=0)
addButton(name="x^2", function=square, row=2, column=1)
addButton(name="2/‾x‾", function=squareRoot, row=2, column=2)
addButton(name="/", function=divide, row=2, column=3)

# 3
addButtonLambda(name="7", function=AddToEntry, row=3, column=0, lambdaVar="7")
addButtonLambda(name="8", function=AddToEntry, row=3, column=1, lambdaVar="8")
addButtonLambda(name="9", function=AddToEntry, row=3, column=2, lambdaVar="9")
addButton(name="*", function=multiply, row=3, column=3)

# 4
addButtonLambda(name="4", function=AddToEntry, row=4, column=0, lambdaVar="4")
addButtonLambda(name="5", function=AddToEntry, row=4, column=1, lambdaVar="5")
addButtonLambda(name="6", function=AddToEntry, row=4, column=2, lambdaVar="6")
addButton(name="-", function=substraction, row=4, column=3)

# 5
addButtonLambda(name="1", function=AddToEntry, row=5, column=0, lambdaVar="1")
addButtonLambda(name="2", function=AddToEntry, row=5, column=1, lambdaVar="2")
addButtonLambda(name="3", function=AddToEntry, row=5, column=2, lambdaVar="3")
addButton(name="+", function=sum, row=5, column=3)

# 6
addButton(name="+/-", function=negativeOrPositive, row=6, column=0)
addButtonLambda(name="0", function=AddToEntry, row=6, column=1, lambdaVar="0")
addButtonLambda(name=".", function=AddToEntry, row=6, column=2, lambdaVar=".")
addButton(name="=", function=equals, row=6, column=3)

# endregion

# region Footer
for i in range(4):
    win.grid_columnconfigure(i, minsize=350 / 4)
for i in range(7):
    win.grid_rowconfigure(i, minsize=200 / 7)

win.mainloop()
# endregion