#this project is a self-motivated project,only for learning the concepts of graphical programming.
#it is basically a gui interface cum operable calculator.
#GUI has been developed over tkinter library of python programming language.
#date:11/01/2020.
#name:Simple Calculator.


from tkinter import *

#GUI window with geometry=256x363.
#the calculator has been made non-resizable(intentionally).
root= Tk()
root.title("my_calculator")
root.geometry("256x363")
root.resizable(0,0)


#take entry in the input Box.
#grid puts up the Entry widget on the root interface(window).
e=Entry(root,width=42,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

#t=Text(root,height=1,width=23,font=("arial",15,"bold"))
#t.grid(row=0,column=0,columnspan=3)

#function to define what a button click does.
def click(num):
	curr=e.get()
	e.delete(0,END)
	e.insert(0,curr+num)
	global x
	x=e.get()

#function to define what the clear button does.
def clear():
	e.delete(0,END)

#function to define what the "+" button does.
def add():
	global f_num
	f_num=e.get()
	e.delete(0,END)
	global label
	label="+"

#function to define what the "-" button does.
def substract():
	global s
	s=e.get()
	e.delete(0,END)
	global label
	label="-"

#function to define what the "x" button does.
def multiplication():
	global m
	m=e.get()
	e.delete(0,END)
	global label
	label="x"


#function to define what the "/" button does.
def divide():
	global d
	d=e.get()
	e.delete(0,END)
	global label
	label="/"


#function to define what the "=" button does.
def equal():
	e.delete(0,END)
	if(label=="+"):
		e.insert(0,str(float(f_num)+float(x)))
	elif(label=="-"):
		e.insert(0,str(float(s)-float(x)))
	elif(label=="x"):
		e.insert(0,str(float(m)*float(x)))
	else:
		if(x=="0"):
			e.insert(0,"NP")
		e.insert(0,str(float(d)/float(x)))



#button(s) created.
button_0=Button(root,text="0",padx=35,pady=15,bg="white",command=lambda:click("0"),bd=3)

button_1=Button(root,text="1",padx=35,pady=15,bg="white",command=lambda:click("1"),bd=3)
button_2=Button(root,text="2",padx=35,pady=15,bg="white",command=lambda:click("2"),bd=3)
button_3=Button(root,text="3",padx=35,pady=15,bg="white",command=lambda:click("3"),bd=3)

button_4=Button(root,text="4",padx=35,pady=15,bg="white",command=lambda:click("4"),bd=3)
button_5=Button(root,text="5",padx=35,pady=15,bg="white",command=lambda:click("5"),bd=3)
button_6=Button(root,text="6",padx=35,pady=15,bg="white",command=lambda:click("6"),bd=3)

button_7=Button(root,text="7",padx=35,pady=15,bg="white",command=lambda:click("7"),bd=3)
button_8=Button(root,text="8",padx=35,pady=15,bg="white",command=lambda:click("8"),bd=3)
button_9=Button(root,text="9",padx=35,pady=15,bg="white",command=lambda:click("9"),bd=3)

button_add=Button(root,text="+",padx=34,pady=15,command=add,bd=3)
button_multiply=Button(root,text="x",padx=35,pady=15,command=multiplication,bd=3)
button_divide=Button(root,text="/",padx=35,pady=15,command=divide,bd=3)
button_substract=Button(root,text="-",padx=35,pady=15,command=substract,bd=3)

button_clear=Button(root,text="clear",padx=70,pady=15,command=clear,bd=3)
button_equal=Button(root,text="=",padx=78,pady=15,command=equal,bd=3)

#buttons_packed onto the screen.
button_0.grid(row=4,column=0)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_add.grid(row=6,column=0)
button_divide.grid(row=5,column=2)
button_multiply.grid(row=5,column=1)
button_substract.grid(row=5,column=0)

button_clear.grid(row=6,column=1,columnspan=2)
button_equal.grid(row=4,column=1,columnspan=2)

#mainloop() will encircle the whole content of the program indispensablly,so that the user don't find any fluctuations in the interface unless the calculator is set close.
root.mainloop()