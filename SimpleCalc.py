import tkinter as tk
import CalcFuncs as cf
from math import sqrt

root = tk.Tk()

root.title("Simple Calculator")
root.geometry("500x500")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=4)
root.columnconfigure(0, weight=1)

#Display
displayed = "0"
firstNum = None
operator = None
newNum = True

displayframe = tk.Frame(root)
displayframe.rowconfigure(0, minsize=70)
for i in range(3):
    displayframe.columnconfigure(i, weight=1, minsize=100)

prevDisplay = tk.Label(displayframe, text="", anchor="e", font=('Arial, 12'))
display = tk.Label(displayframe, text=displayed, anchor="e", pady=5, font=('Arial, 24'))
prevDisplay.grid(row=0, column=0, columnspan=4, sticky='ew', padx=3, pady=3)
display.grid(row=1, column=0, columnspan=4, sticky='ew', padx=3, pady=3)

def updateDisplay():
    display.configure(text=displayed)

def moveToUpperLayer():
    global displayed

    prevDisplay.configure(text=displayed)
    display.configure(text="0")

def checkInt(answer):
    global displayed

    if answer.is_integer():
        displayed = str(int(answer))
    else:
        displayed = str(answer)

def ce():
    global displayed
    displayed = "0"
    updateDisplay()

def clear():
    global displayed

    displayed = "0"

    prevDisplay.configure(text="")
    updateDisplay()

def back():
    global displayed, operator, firstNum

    if len(displayed) <= 1:
        displayed = "0"
    else:
        displayed = displayed[:-1]

    updateDisplay()

def addNum(num):
    global displayed, newNum

    if newNum:
        displayed = str(num)
        newNum = False
    else:
        if displayed == "0" or displayed == "Error":
            displayed = str(num)
        else:
            displayed += str(num)

    updateDisplay()

def calculate():
    global displayed, firstNum, operator, newNum

    secondNum = float(displayed)
    try:
        if operator == "+":
            firstNum += secondNum
        elif operator == "-":
            firstNum -= secondNum
        elif operator == "*":
            firstNum *= secondNum
        elif operator == "/":
                firstNum /= secondNum
        elif operator == "x²":
            firstNum = pow(firstNum, 2)
    
        displayed = str(firstNum)

        checkInt(firstNum)

        updateDisplay()
        moveToUpperLayer()

    except:
        displayed = "Error"
        prevDisplay.configure(text="")
        updateDisplay()

def percentage():
    global displayed

    answer = cf.percentage(float(displayed))

    checkInt(answer)

    updateDisplay()

def frac():
    global displayed

    answer = cf.frac(float(displayed))

    checkInt(answer)

    updateDisplay()

def sqroot():
    global displayed

    num = float(displayed)
    if num < 0:
        displayed = "Error"
    else:
        answer = sqrt(num)
        checkInt(answer)
    
    updateDisplay()

def square():
    global displayed

    num = float(displayed)
    answer = num ** 2

    checkInt(answer)

    updateDisplay()

def inverse():
    global displayed

    num = float(displayed)
    answer = -num
    
    checkInt(answer)

    updateDisplay()

def addComma():
    global displayed, newNum

    if newNum:
        displayed = "0."
        newNum = False
    elif "." not in displayed:
        displayed += "."

    updateDisplay()


def operate(op):
    global firstNum, operator, newNum

    if operator is None:
        firstNum = float(displayed)
    else:
        calculate()

    operator = op
    newNum = True

    prevDisplay.configure(text=f"{displayed} {op}")

def result():
    global operator, newNum

    calculate()
    operator = None
    newNum = None

#Display Buttons
buttonframe = tk.Frame(root)
for i in range(6):
    buttonframe.rowconfigure(i, weight=1, minsize=20)
for j in range(4):
    buttonframe.columnconfigure(j, weight=1, minsize=70)

buttonFont = ("Arial, 11")

btnPercent = tk.Button(buttonframe, text="%", font=buttonFont, command=percentage)
btnPercent.grid(row=0, column=0, sticky='nsew')

btnCE = tk.Button(buttonframe, text="CE", font=buttonFont, command=ce)
btnCE.grid(row=0, column=1, sticky='nsew')

btnClear = tk.Button(buttonframe, text="C", font=buttonFont, command=clear)
btnClear.grid(row=0, column=2, sticky='nsew')

btnBack = tk.Button(buttonframe, text="<<", font=buttonFont, command=back)
btnBack.grid(row=0, column=3, sticky='nsew')

btnFraction = tk.Button(buttonframe, text="x⁻¹", font=buttonFont, command=frac)
btnFraction.grid(row=1, column=0, sticky='nsew')

btnSquare = tk.Button(buttonframe, text="x²", font=buttonFont, command=square)
btnSquare.grid(row=1, column=1, sticky='nsew')

btnSqRoot = tk.Button(buttonframe, text="√x", font=buttonFont, command=sqroot)
btnSqRoot.grid(row=1, column=2, sticky='nsew')

btnDivide = tk.Button(buttonframe, text="÷", font=buttonFont, command=lambda: operate("/"))
btnDivide.grid(row=1, column=3, sticky='nsew')

btnMult = tk.Button(buttonframe, text="×", font=buttonFont, command=lambda: operate("*"))
btnMult.grid(row=2, column=3, sticky='nsew')

btnMinus = tk.Button(buttonframe, text="-", font=buttonFont, command=lambda: operate("-"))
btnMinus.grid(row=3, column=3, sticky='nsew')

btnPlus = tk.Button(buttonframe, text="+", font=buttonFont, command=lambda: operate("+"))
btnPlus.grid(row=4, column=3, sticky='nsew')

btnInverse = tk.Button(buttonframe, text="+/-", font=buttonFont, command=inverse)
btnInverse.grid(row=5, column=0, sticky='nsew')

btnComma = tk.Button(buttonframe, text=".", font=buttonFont, command=addComma)
btnComma.grid(row=5, column=2, sticky='nsew')

btnResult = tk.Button(buttonframe, text="=", font=buttonFont, command=result)
btnResult.grid(row=5, column=3, sticky='nsew')

btn1 = tk.Button(buttonframe, text="1", font=buttonFont, command=lambda: addNum(1))
btn1.grid(row=2, column=0, sticky='nsew')

btn2 = tk.Button(buttonframe, text="2", font=buttonFont, command=lambda: addNum(2))
btn2.grid(row=2, column=1, sticky='nsew')

btn3 = tk.Button(buttonframe, text="3", font=buttonFont, command=lambda: addNum(3))
btn3.grid(row=2, column=2, sticky='nsew')

btn4 = tk.Button(buttonframe, text="4", font=buttonFont, command=lambda: addNum(4))
btn4.grid(row=3, column=0, sticky='nsew')

btn5 = tk.Button(buttonframe, text="5", font=buttonFont, command=lambda: addNum(5))
btn5.grid(row=3, column=1, sticky='nsew')

btn6 = tk.Button(buttonframe, text="6", font=buttonFont, command=lambda: addNum(6))
btn6.grid(row=3, column=2, sticky='nsew')

btn7 = tk.Button(buttonframe, text="7", font=buttonFont, command=lambda: addNum(7))
btn7.grid(row=4, column=0, sticky='nsew')

btn8 = tk.Button(buttonframe, text="8", font=buttonFont, command=lambda: addNum(8))
btn8.grid(row=4, column=1, sticky='nsew')

btn9 = tk.Button(buttonframe, text="9", font=buttonFont, command=lambda: addNum(9))
btn9.grid(row=4, column=2, sticky='nsew')

btn0 = tk.Button(buttonframe, text="0", font=buttonFont, command=lambda: addNum(0))
btn0.grid(row=5, column=1, sticky='nsew')

displayframe.grid(row=0, column=0, sticky='nsew')
buttonframe.grid(row=1, column=0, sticky='nsew')

root.mainloop()