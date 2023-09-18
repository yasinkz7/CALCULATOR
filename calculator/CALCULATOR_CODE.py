from tkinter import *

# made (yasinkz7)

window=Tk()
window.title("CALCULATOR")
window.iconbitmap(r"G:\python\calculator\icon\calculator.ico")

entry=Entry(window,borderwidth=30,font=("arial","24","bold"),width=32,bg="#bfbfbf",fg="black")
entry.grid(row=0,column=0,columnspan=4)

def add(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0,END)

def add_button():
    global first_number
    global math_operation 
    math_operation = "addition"
    first_number = entry.get()
    entry.delete(0,END)


def equal_button():
    global second_number
    second_number = entry.get()
    entry.delete(0,END)
    
    if math_operation == "addition":
        entry.insert(0, float(first_number) + float(second_number))
    elif math_operation == "subtraction":
        entry.insert(0, float(first_number) - float(second_number))
    elif math_operation == "division":
        entry.insert(0, float(first_number) / float(second_number))
    elif math_operation == "multiplication":
        entry.insert(0, float(first_number) * float(second_number))
    elif math_operation == "modulus":
        entry.insert(0, float(first_number) % float(second_number))

def subtract_button():
    global first_number
    global math_operation 
    math_operation = "subtraction"
    first_number = entry.get()
    entry.delete(0,END)

def modulus_button():
    global first_number
    global math_operation 
    math_operation = "modulus"
    first_number = entry.get()
    entry.delete(0,END)

def divide_button():
    global first_number
    global math_operation 
    math_operation = "division"
    first_number = entry.get()
    entry.delete(0,END)


def multiply_button():
    global first_number
    global math_operation 
    math_operation = "multiplication"
    first_number = entry.get()
    entry.delete(0,END)


def divide_button():
    global first_number
    global math_operation 
    math_operation = "division"
    first_number = entry.get()
    entry.delete(0,END)

def prantez_chap():
    entry.insert(END, "(")

def prantez_rast():
    entry.insert(END, ")")

def noghte():
    entry.insert(END, ".")

clear=Button(window, text="C", padx=48 , pady=20 ,
                fg="red",bg="gray",bd=8,font=("arial","24","bold"),command=clear)
clear.grid(row=1,column=0)
button1=Button(window, text="7", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(7))
button1.grid(row=2,column=0)
button1=Button(window, text="4", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(4))
button1.grid(row=3,column=0)
button1=Button(window, text="1", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(1))
button1.grid(row=4,column=0)
noghte=Button(window, text=" .", padx=50 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=noghte)
noghte.grid(row=5,column=0)
prantez_chap=Button(window, text="(", padx=55 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=prantez_chap)
prantez_chap.grid(row=1,column=1)
button2=Button(window, text="8", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(8))
button2.grid(row=2,column=1)
button2=Button(window, text="5", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(5))
button2.grid(row=3,column=1)
button2=Button(window, text="2", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(2))
button2.grid(row=4,column=1)
button2=Button(window, text="0", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(0))
button2.grid(row=5,column=1)
button3=Button(window, text=")", padx=55 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=prantez_rast)
button3.grid(row=1,column=2)
button3=Button(window, text="9", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(9))
button3.grid(row=2,column=2)
button3=Button(window, text="6", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(6))
button3.grid(row=3,column=2)
button3=Button(window, text="3", padx=50 , pady=20 ,
                fg="black",bg="white",bd=8,font=("arial","24","bold"),command=lambda:add(3))
button3.grid(row=4,column=2)
button3=Button(window, text="%", padx=50 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=modulus_button)
button3.grid(row=5,column=2)
button4=Button(window, text=" ÷", padx=50 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=divide_button)
button4.grid(row=1,column=3)
button4=Button(window, text="×", padx=54 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=multiply_button)
button4.grid(row=2,column=3)
button4=Button(window, text="-", padx=58 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=subtract_button)
button4.grid(row=3,column=3)
button4=Button(window, text="+", padx=54 , pady=20 ,
                fg="green",bg="gray",bd=8,font=("arial","24","bold"),command=add_button)
button4.grid(row=4,column=3)
button4=Button(window, text="=", padx=54 , pady=20 ,
                fg="yellow",bg="gray",bd=8,font=("arial","24","bold"),command=equal_button)
button4.grid(row=5,column=3)

window.mainloop()