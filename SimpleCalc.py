import tkinter as tk
import CalcFuncs as cf

root = tk.Tk()

root.title("Simple Calculator")
root.geometry("500x500")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=4)
root.columnconfigure(0, weight=1)

#Display Layer
displayframe = tk.Frame(root)
displayframe.rowconfigure(0, minsize=70)
for i in range(3):
    displayframe.columnconfigure(i, weight=1, minsize=100)

display = tk.Label(displayframe, text="0", anchor="e", pady=5, font=('Arial, 24'))
display.grid(row=0, column=0, columnspan=4, sticky='ew', padx=3, pady=3)

#Functions
def alwaysZero():
    display.configure(text="0")

def percentage():
    currentText = display.cget("text")
    currentText = list(currentText)
    num = currentText[-1]
    newNum = cf.percentage(num)
    currentText[-1] = newNum
    currentText = ''.join(currentText)
    display.configure(text=currentText)

def clear():
    display.configure(text="0")

def back():
    currentText = display.cget("text")
    currentText = list(currentText)
    currentText.pop()
    if len(currentText) <= 1:
        display.configure(text="0")
    else:
        display.configure(text=currentText[:-1])

def addNum(num):
    currentText = display.cget("text")
    currentText = list(currentText)
    if currentText[0] == "0":
        currentText.pop(0)
    currentText.append(str(num))
    currentText = ''.join(currentText)
    display.configure(text=currentText)

#Display Buttons
buttonframe = tk.Frame(root)
for i in range(6):
    buttonframe.rowconfigure(i, weight=1, minsize=20)
for j in range(4):
    buttonframe.columnconfigure(j, weight=1, minsize=70)

buttonFont = ("Arial, 11")

btnPercent = tk.Button(buttonframe, text="%", font=buttonFont, command=percentage)
btnPercent.grid(row=0, column=0, sticky='nsew')

btnCE = tk.Button(buttonframe, text="CE", font=buttonFont, command=cf.ce)
btnCE.grid(row=0, column=1, sticky='nsew')

btnClear = tk.Button(buttonframe, text="C", font=buttonFont, command=clear)
btnClear.grid(row=0, column=2, sticky='nsew')

btnBack = tk.Button(buttonframe, text="<<", font=buttonFont, command=back)
btnBack.grid(row=0, column=3, sticky='nsew')

btnFraction = tk.Button(buttonframe, text="x⁻¹", font=buttonFont, command=cf.frac)
btnFraction.grid(row=1, column=0, sticky='nsew')

btnSquare = tk.Button(buttonframe, text="x²", font=buttonFont, command=cf.square)
btnSquare.grid(row=1, column=1, sticky='nsew')

btnSqRoot = tk.Button(buttonframe, text="√x", font=buttonFont, command=cf.sqroot)
btnSqRoot.grid(row=1, column=2, sticky='nsew')

btnDivide = tk.Button(buttonframe, text="÷", font=buttonFont, command=cf.divide)
btnDivide.grid(row=1, column=3, sticky='nsew')

btnMult = tk.Button(buttonframe, text="×", font=buttonFont, command=cf.mult)
btnMult.grid(row=2, column=3, sticky='nsew')

btnMinus = tk.Button(buttonframe, text="-", font=buttonFont, command=cf.minus)
btnMinus.grid(row=3, column=3, sticky='nsew')

btnPlus = tk.Button(buttonframe, text="+", font=buttonFont, command=cf.plus)
btnPlus.grid(row=4, column=3, sticky='nsew')

btnInverse = tk.Button(buttonframe, text="+/-", font=buttonFont, command=cf.inverse)
btnInverse.grid(row=5, column=0, sticky='nsew')

btnComma = tk.Button(buttonframe, text=".", font=buttonFont, command=cf.comma)
btnComma.grid(row=5, column=2, sticky='nsew')

btnResult = tk.Button(buttonframe, text="=", font=buttonFont, command=cf.result)
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