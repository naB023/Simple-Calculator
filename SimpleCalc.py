import customtkinter as ctk
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

RESULT_BUTTON_STYLE = {
    "font": ("Segoe UI", 14),
    "fg_color": "#27a300",
    "text_color": "#ecffeb",
    "border_width": 0,
    "corner_radius": 12,
    "hover_color": "#8fcb9b",
}

OPERATOR_BUTTON_STYLE = {
    "font": ("Segoe UI", 14),
    "fg_color": "#3C4043",
    "text_color": "#27a300",
    "border_width": 0,
    "corner_radius": 12,
    "hover_color": "#8fcb9b",
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

def makeButton(txt, cmd, rw, clm):
    btn = ctk.CTkButton(buttonframe, text=txt, command=cmd, **BUTTON_STYLE)
    btn.grid(row=rw, column=clm, sticky='nsew', padx=2, pady=2)
    return btn

def makeOperator(txt, cmd, rw, clm):
    btn = ctk.CTkButton(buttonframe, text=txt, command=cmd, **OPERATOR_BUTTON_STYLE)
    btn.grid(row=rw, column=clm, sticky='nsew', padx=2, pady=2)
    return btn

#Display Buttons
buttonframe = ctk.CTkFrame(root)
buttonframe.configure(fg_color=DISPLAY)
for i in range(6):
    buttonframe.rowconfigure(i, weight=1, minsize=20)
for j in range(4):
    buttonframe.columnconfigure(j, weight=1, minsize=70)

operatorConfig = [
    ("%", percentage, 0, 0),
    ("CE", ce, 0, 1),
    ("C", clear, 0, 2),
    ("⌫", back, 0, 3),
    ("¹/x", frac, 1, 0),
    ("x²", square, 1, 1),
    ("√x", sqroot, 1, 2),
    ("÷", lambda: operate("/"), 1, 3),
    ("×", lambda: operate("*"), 2, 3),
    ("-", lambda: operate("-"), 3, 3),
    ("+", lambda: operate("+"), 4, 3),
    ("+/-", inverse, 5, 0),
    (".", addComma, 5, 2)
]

buttonConfig = [
    ("1", lambda: addNum(1), 2, 0),
    ("2", lambda: addNum(2), 2, 1),
    ("3", lambda: addNum(3), 2, 2),
    ("4", lambda: addNum(4), 3, 0),
    ("5", lambda: addNum(5), 3, 1),
    ("6", lambda: addNum(6), 3, 2),
    ("7", lambda: addNum(7), 4, 0),
    ("8", lambda: addNum(8), 4, 1),
    ("9", lambda: addNum(9), 4, 2),
    ("0", lambda: addNum(0), 5, 1)
]

for txt, cmd, rw, clm in operatorConfig:
    makeOperator(txt, cmd, rw, clm)

for txt, cmd, rw, clm in buttonConfig:
    makeButton(txt, cmd, rw, clm)

btnResult = ctk.CTkButton(buttonframe, text="=", command=result, **RESULT_BUTTON_STYLE)
btnResult.grid(row=5, column=3, sticky='nsew', padx=2, pady=2)


displayframe.grid(row=0, column=0, sticky='nsew')
buttonframe.grid(row=1, column=0, sticky='nsew')

root.mainloop()