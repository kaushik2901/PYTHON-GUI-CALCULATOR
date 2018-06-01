from tkinter import *
from math import *


root = Tk()
root.title("Calculator")
root.resizable(0, 0)
view1 = Frame(root).grid()

InputBoxFrame = Frame(view1).grid()
InputButtonFrame = Frame(view1).grid(row=1)

textBoxText = StringVar()
textBox = Entry(InputBoxFrame,font=('Verdana', 30), textvariable=textBoxText, justify='right', state=DISABLED)
textBox.grid(row=0, column=0, columnspan=6, sticky="nsew")

inputBox = Entry(InputBoxFrame,font=('Verdana', 20), justify='right')
inputBox.grid(row=1, column=0, columnspan=6, sticky="nsew")
inputBox.config(highlightbackground='WHITE')
ButtonTexts = [
	[ 7, 8, 9, "/", "AC", "DEL" ],
	[ 4, 5, 6, "x", "(", ")" ],
	[ 1, 2, 3, "-", "sqrt", "^" ],
	[ ".", 0, "%", "+", "=" ] ]

Flag = 0

def insert(char):
	global Flag
	if Flag == 1:
		inputBox.delete(0, END)
		Flag = 0
	inputBox.insert(END, char)
	return

def clear():
	inputBox.delete(0, END)
	return

def delete():
	temp = inputBox.get()[:-1]
	inputBox.delete(0, END)
	inputBox.insert(END, temp)
	return

def result():
	temp = inputBox.get()
	global Flag
	try:
		res = eval(temp)
		textBoxText.set(res)
		Flag = 1
	except Exception as e:
		textBoxText.set("ERROR")
		print("Error : " + str(e))
	return



#BUTTONS
Button(InputButtonFrame, text=str(ButtonTexts[0][0]), command=lambda:insert('7')).grid(row=2, column=0, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[0][1]), command=lambda:insert('8')).grid(row=2, column=1, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[0][2]), command=lambda:insert('9')).grid(row=2, column=2, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[0][3]), command=lambda:insert('/')).grid(row=2, column=3, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[0][4]), command=lambda:clear()).grid(row=2, column=4, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[0][5]), command=lambda:delete()).grid(row=2, column=5, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[1][0]), command=lambda:insert('4')).grid(row=3, column=0, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[1][1]), command=lambda:insert('5')).grid(row=3, column=1, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[1][2]), command=lambda:insert('6')).grid(row=3, column=2, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[1][3]), command=lambda:insert('*')).grid(row=3, column=3, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[1][4]), command=lambda:insert('(')).grid(row=3, column=4, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[1][5]), command=lambda:insert(')')).grid(row=3, column=5, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[2][0]), command=lambda:insert('1')).grid(row=4, column=0, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[2][1]), command=lambda:insert('2')).grid(row=4, column=1, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[2][2]), command=lambda:insert('3')).grid(row=4, column=2, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[2][3]), command=lambda:insert('-')).grid(row=4, column=3, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[2][4]), state=DISABLED).grid(row=4, column=4, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[2][5]), state=DISABLED).grid(row=4, column=5, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[3][0]), command=lambda:insert('.')).grid(row=5, column=0, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[3][1]), command=lambda:insert('0')).grid(row=5, column=1, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[3][2]), command=lambda:insert('%'), state=DISABLED).grid(row=5, column=2, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[3][3]), command=lambda:insert('+')).grid(row=5, column=3, sticky="nsew", pady=1, padx=1)
Button(InputButtonFrame, text=str(ButtonTexts[3][4]), command=lambda:result()).grid(row=5, column=4, columnspan=2, sticky="nsew", pady=1, padx=1)

inputBox.focus()
root.mainloop()
