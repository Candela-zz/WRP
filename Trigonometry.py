import math
from tkinter import *
from tkinter import ttk

GUI=Tk()
GUI.title('Trigonometry')
GUI.geometry('500x500')

L1=Label(GUI,text='Please input degree :')
L1.pack(pady=10)

degree=DoubleVar

E1=ttk.Entry(GUI,textvariable=degree)
E1.pack(ipadx=12,ipady=8)

F1=Frame(GUI)
F1.place(x=200,y=200)
