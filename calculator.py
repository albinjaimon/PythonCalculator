import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_display.delete(1.0, "end")
    text_display.insert(1.0, calculation)


def evaluate_calculation(): #using eval function could allow for code to be injected, as python code can be evaluated
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_display.delete(1.0, "end")
        text_display.insert(1.0, calculation)
    except:
        clear_calculator()
        text_display.insert(1.0, "Error")
        pass

def clear_calculator():
    global calculation
    calculation = ""
    text_display.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_display = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_display.grid(columnspan=5)


btn1 = tk.Button(root, text="1", command=lambda:add_to_calculation(1), width=5, font=("Arial",14))
btn1.grid(row=2, column=1, columnspan=1)

btn2 = tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=5, font=("Arial",14))
btn2.grid(row=2, column=2, columnspan=1)

btn3 = tk.Button(root, text="3", command=lambda:add_to_calculation(3), width=5, font=("Arial",14))
btn3.grid(row=2, column=3, columnspan=1)

btn4 = tk.Button(root, text="4", command=lambda:add_to_calculation(4), width=5, font=("Arial",14))
btn4.grid(row=2, column=4, columnspan=1)

btn5 = tk.Button(root, text="5", command=lambda:add_to_calculation(5), width=5, font=("Arial",14))
btn5.grid(row=3, column=1, columnspan=1)

btn6 = tk.Button(root, text="6", command=lambda:add_to_calculation(6), width=5, font=("Arial",14))
btn6.grid(row=3, column=2, columnspan=1)

btn7 = tk.Button(root, text="7", command=lambda:add_to_calculation(7), width=5, font=("Arial",14))
btn7.grid(row=3, column=3, columnspan=1)

btn8 = tk.Button(root, text="8", command=lambda:add_to_calculation(8), width=5, font=("Arial",14))
btn8.grid(row=3, column=4, columnspan=1)

btn9 = tk.Button(root, text="9", command=lambda:add_to_calculation(9), width=5, font=("Arial",14))
btn9.grid(row=4, column=1, columnspan=1)

btn0 = tk.Button(root, text="0", command=lambda:add_to_calculation(0), width=5, font=("Arial",14))
btn0.grid(row=4, column=2, columnspan=1)

btnEqual = tk.Button(root, text="=", command=lambda:add_to_calculation("="), width=5, font=("Arial",14))
btnEqual.grid(row=4, column=3, columnspan=1)



root.mainloop()
