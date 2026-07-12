import customtkinter as ctk
import CalcFuncs as cf
from math import sqrt

root = ctk.CTk()

root.title("Simple Calculator")
root.geometry("500x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=4)
root.columnconfigure(0, weight=1)

#Display
displayed = "0"
firstNum = None
operator = None
newNum = True

#Styling
DISPLAY = "#303134"
TEXT = "#FFFFFF"
fg_color = "#3C4043"
HOVER = "#4A4D52"

BUTTON_STYLE = {
    "font": ("Segoe UI", 14),
    "fg_color": "#3C4043",
    "text_color": "white",
    "border_width": 0,
    "corner_radius": 12,
    "hover_color": "#4A4D52",
}

displayframe = ctk.CTkFrame(root)
displayframe.configure(fg_color=DISPLAY)
displayframe.rowconfigure(0, minsize=70)
for i in range(3):
    displayframe.columnconfigure(i, weight=1, minsize=100)

prevDisplay = ctk.CTkLabel(displayframe, text="", anchor="e", font=("Segoe UI", 12), fg_color=DISPLAY, text_color=TEXT)
display = ctk.CTkLabel(displayframe, text=displayed, anchor="e", pady=5, font=("Segoe UI", 24, "bold"), fg_color=DISPLAY, text_color=TEXT)
prevDisplay.grid(row=0, column=0, columnspan=4, sticky='ew', padx=3, pady=3)
display.grid(row=1, column=0, columnspan=4, sticky='ew', padx=3, pady=3)

#Functions
    
def updateDisplay():
    display.configure(text=displayed)

def setAnswer(answer):
    global displayed

    if isinstance(answer, float) and answer.is_integer():
        displayed = str(int(answer))
    else:
        displayed = str(round(answer, 5))
    
    updateDisplay()

def formatInt(num):
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(num)

def ce():
    global displayed, newNum

    displayed = "0"
    newNum = True

    updateDisplay()

def clear():
    global displayed, firstNum, operator, newNum

    displayed = "0"
    firstNum = None
    operator = None
    newNum = True

    prevDisplay.configure(text="")
    updateDisplay()

def back():
    global displayed, operator, firstNum

    if len(displayed) <= 1 or displayed == "Error":
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

    if operator is None:
        return

    if isinstance(firstNum, float) and firstNum.is_integer():
        dpfirstNum = int(firstNum)
    else:
        dpfirstNum = firstNum

    secondNum = float(displayed)
    if isinstance(secondNum, float) and secondNum.is_integer():
        dpsecondNum = int(secondNum)
    else:
        dpsecondNum = secondNum

    try:
        if operator == "+":
            disptext = f"{dpfirstNum}+{dpsecondNum}"
            firstNum += secondNum
        elif operator == "-":
            disptext = f"{dpfirstNum}-{dpsecondNum}"
            firstNum -= secondNum
        elif operator == "*":
            disptext = f"{dpfirstNum}×{dpsecondNum}"
            firstNum *= secondNum
        elif operator == "/":
            disptext = f"{dpfirstNum}÷{dpsecondNum}"
            firstNum /= secondNum
        elif operator == "x²":
            disptext = f"{dpfirstNum}²"
            firstNum = pow(firstNum, 2)
    
        displayed = str(firstNum)

        setAnswer(firstNum)

        prevDisplay.configure(text=f"{disptext} =")

    except ZeroDivisionError:
        displayed = "Error"
        prevDisplay.configure(text="")

        updateDisplay()

def percentage():
    global displayed

    secondNum = float(displayed)

    if operator in ["+", "-"]:
        secondNum = firstNum * secondNum/100
    
    elif operator in ["*", "/"]:
        secondNum = secondNum/100

    setAnswer(secondNum)

def frac():
    global displayed

    num = float(displayed)
    answer = 1/num

    setAnswer(answer)

    prevDisplay.configure(text=f"1/({formatInt(num)})")

def sqroot():
    global displayed

    num = float(displayed)
    if num < 0:
        displayed = "Error"
        updateDisplay()
    else:
        answer = sqrt(num)
        setAnswer(answer)

    prevDisplay.configure(text=f"√({formatInt(num)})")
    
def square():
    global displayed

    num = float(displayed)
    answer = num ** 2

    setAnswer(answer)

    prevDisplay.configure(text=f"({formatInt(num)})²")

def inverse():
    global displayed

    num = float(displayed)
    answer = -num
    
    setAnswer(answer)

    prevDisplay.configure(text=f"-({formatInt(num)})")

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

    if newNum and operator is not None:
        operator = op
        prevDisplay.configure(text=f"{firstNum} {op}")
        return

    if operator is None:
        firstNum = float(displayed)
    else:
        calculate()

    operator = op
    newNum = True

    prevDisplay.configure(text=f"{displayed} {op}")

def result():
    global operator, firstNum, newNum

    if operator is None:
        return

    calculate()

    operator = None
    firstNum = None
    newNum = True

#Display Buttons
buttonframe = ctk.CTkFrame(root)
buttonframe.configure(fg_color=DISPLAY)
for i in range(6):
    buttonframe.rowconfigure(i, weight=1, minsize=20)
for j in range(4):
    buttonframe.columnconfigure(j, weight=1, minsize=70)

btnPercent = ctk.CTkButton(buttonframe, text="%", command=percentage, **BUTTON_STYLE)
btnPercent.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)

btnCE = ctk.CTkButton(buttonframe, text="CE", command=ce, **BUTTON_STYLE)
btnCE.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)

btnClear = ctk.CTkButton(buttonframe, text="C", command=clear, **BUTTON_STYLE)
btnClear.grid(row=0, column=2, sticky='nsew', padx=2, pady=2)

btnBack = ctk.CTkButton(buttonframe, text="⌫", command=back, **BUTTON_STYLE)
btnBack.grid(row=0, column=3, sticky='nsew', padx=2, pady=2)

btnFraction = ctk.CTkButton(buttonframe, text="¹/x", command=frac, **BUTTON_STYLE)
btnFraction.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

btnSquare = ctk.CTkButton(buttonframe, text="x²", command=square, **BUTTON_STYLE)
btnSquare.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

btnSqRoot = ctk.CTkButton(buttonframe, text="√x", command=sqroot, **BUTTON_STYLE)
btnSqRoot.grid(row=1, column=2, sticky='nsew', padx=2, pady=2)

btnDivide = ctk.CTkButton(buttonframe, text="÷", command=lambda: operate("/"), **BUTTON_STYLE)
btnDivide.grid(row=1, column=3, sticky='nsew', padx=2, pady=2)

btnMult = ctk.CTkButton(buttonframe, text="×", command=lambda: operate("*"), **BUTTON_STYLE)
btnMult.grid(row=2, column=3, sticky='nsew', padx=2, pady=2)

btnMinus = ctk.CTkButton(buttonframe, text="-", command=lambda: operate("-"), **BUTTON_STYLE)
btnMinus.grid(row=3, column=3, sticky='nsew', padx=2, pady=2)

btnPlus = ctk.CTkButton(buttonframe, text="+", command=lambda: operate("+"), **BUTTON_STYLE)
btnPlus.grid(row=4, column=3, sticky='nsew', padx=2, pady=2)

btnInverse = ctk.CTkButton(buttonframe, text="+/-", command=inverse, **BUTTON_STYLE)
btnInverse.grid(row=5, column=0, sticky='nsew', padx=2, pady=2)

btnComma = ctk.CTkButton(buttonframe, text=".", command=addComma, **BUTTON_STYLE)
btnComma.grid(row=5, column=2, sticky='nsew', padx=2, pady=2)

btnResult = ctk.CTkButton(buttonframe, text="=", command=result, **BUTTON_STYLE)
btnResult.grid(row=5, column=3, sticky='nsew', padx=2, pady=2)

btn1 = ctk.CTkButton(buttonframe, text="1", command=lambda: addNum(1), **BUTTON_STYLE)
btn1.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)

btn2 = ctk.CTkButton(buttonframe, text="2", command=lambda: addNum(2), **BUTTON_STYLE)
btn2.grid(row=2, column=1, sticky='nsew', padx=2, pady=2)

btn3 = ctk.CTkButton(buttonframe, text="3", command=lambda: addNum(3), **BUTTON_STYLE)
btn3.grid(row=2, column=2, sticky='nsew', padx=2, pady=2)

btn4 = ctk.CTkButton(buttonframe, text="4", command=lambda: addNum(4), **BUTTON_STYLE)
btn4.grid(row=3, column=0, sticky='nsew', padx=2, pady=2)

btn5 = ctk.CTkButton(buttonframe, text="5", command=lambda: addNum(5), **BUTTON_STYLE)
btn5.grid(row=3, column=1, sticky='nsew', padx=2, pady=2)

btn6 = ctk.CTkButton(buttonframe, text="6", command=lambda: addNum(6), **BUTTON_STYLE)
btn6.grid(row=3, column=2, sticky='nsew', padx=2, pady=2)

btn7 = ctk.CTkButton(buttonframe, text="7", command=lambda: addNum(7), **BUTTON_STYLE)
btn7.grid(row=4, column=0, sticky='nsew', padx=2, pady=2)

btn8 = ctk.CTkButton(buttonframe, text="8", command=lambda: addNum(8), **BUTTON_STYLE)
btn8.grid(row=4, column=1, sticky='nsew', padx=2, pady=2)

btn9 = ctk.CTkButton(buttonframe, text="9", command=lambda: addNum(9), **BUTTON_STYLE)
btn9.grid(row=4, column=2, sticky='nsew', padx=2, pady=2)

btn0 = ctk.CTkButton(buttonframe, text="0", command=lambda: addNum(0), **BUTTON_STYLE)
btn0.grid(row=5, column=1, sticky='nsew', padx=2, pady=2)

displayframe.grid(row=0, column=0, sticky='nsew')
buttonframe.grid(row=1, column=0, sticky='nsew')

root.mainloop()