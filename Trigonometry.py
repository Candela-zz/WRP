import math
from tkinter import *
from tkinter import ttk

GUI=Tk()
GUI.title('Trigonometry')
GUI.geometry('500x500')

def Cal_sin():
	degree=int(degree_input.get())
	radian=math.radians(degree)
	print('{:.2f}'.format(math.sin(radian)))
	show_text.set('Result of sin{} is {:.2f}'.format(degree,math.sin(radian)))

def Cal_cos():
	degree=int(degree_input.get())
	radian=math.radians(degree)
	print('{:.2f}'.format(math.cos(radian)))
	show_text.set('Result of cos{} is {:.2f}'.format(degree,math.cos(radian)))

def Cal_tan():
	degree=int(degree_input.get())
	radian=math.radians(degree)
	print('{:.2f}'.format(math.tan(radian)))
	show_text.set('Result of tan{} is {:.2f}'.format(degree,math.tan(radian)))
	
L1=Label(GUI,text='Please input degree :')
L1.pack(pady=10)

degree_input=StringVar()

E1=ttk.Entry(GUI,textvariable=degree_input,font=('AngsanaNew',12))
E1.pack(ipadx=7,ipady=7)

F1=Frame(GUI)
F1.place(x=70,y=100)

B1=Button(F1,text='sin',command=Cal_sin)
B1.grid(column=0,row=0,ipadx=40,ipady=10,pady=10)

B2=Button(F1,text='cos',command=Cal_cos)
B2.grid(column=1,row=0,ipadx=40,ipady=10,pady=10,padx=20)

B3=Button(F1,text='tan',command=Cal_tan)
B3.grid(column=2,row=0,ipadx=40,ipady=10,pady=10)

show_text=StringVar()
L2=Label(GUI,textvariable=show_text,font=('AngsanaNew',12),foreground='red')
L2.place(x=180,y=200)

GUI.mainloop()
