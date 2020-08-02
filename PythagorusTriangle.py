#GUIcal.py
from tkinter import *
from tkinter import ttk
import math

GUI=Tk()
GUI.title('My Cal Program')
GUI.geometry('500x500')

def calc():
	height=v_height.get()
	base=v_base.get()#ดึงค่ามาจากv_base
	print(f'height is {height}')
	print(f'Basal length is {base}')
	length= math.isqrt((height*height)+(base*base))
	print('Lenght is {:.2f}'.format(length))

###For attach picture
'''
IMG=PhotoImage(file='Pytagorus.jpg')
IM1=Label(GUI,image=IMG)
IM1.pack()
'''
v_height=IntVar()
v_base=IntVar()

L1=Label(text='Please input height')
L1.pack()
E1=ttk.Entry(GUI,textvariable=v_height)
E1.pack(pady=8,ipady=7,ipadx=17)


L2=Label(text='Please input basal length')
L2.pack()
E2=ttk.Entry(GUI,textvariable=v_base)
E2.pack(pady=8,ipady=7,ipadx=17)


B1=ttk.Button(text='Calculate',command=calc)
B1.pack()


GUI.mainloop()
