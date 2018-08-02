# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 02:08:35 2018

@author: nilesh8757
"""

from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("400x400")
top.configure(background="#307678")
top.title("BMI Calculator")
top.resizable(width = False, height = False)

def height():
    ht=float(E2.get())
    return ht
    
def weight():
    wt=float(E1.get())
    return wt

def calcBMI():
    try:
        ht=height()
        wt=weight()
        htt=ht/100.0
        bmi=wt/(htt**2)
    except ZeroDivisionError:
        msg=messagebox.showinfo("Result","Please enter positive height!!")
    except:
        msg=messagebox.showinfo("Result","Some error occurred, try again.")
    else:
        if bmi<=15.0:
            res="Your BMI is "+str(bmi)+"\nRemarks: Very severely underweight!!"
            msg=messagebox.showinfo("Result",res)
        elif bmi>15.0 and bmi<=16.0:
            res="Your BMI is "+str(bmi)+"\nRemarks: Severely underweight!"
            msg=messagebox.showinfo("Result",res)
        elif bmi>16.0 and bmi<18.5:
            res="Your BMI is "+str(bmi)+"\nRemarks: Underweight!"
            msg=messagebox.showinfo("Result",res)
        elif bmi>=18.5 and bmi<=25.0:
            res="Your BMI is "+str(bmi)+"\nRemarks: Normal."
            msg=messagebox.showinfo("Result",res)
        elif bmi>25.0 and bmi<=30:
            res="Your BMI is "+str(bmi)+"\nRemarks: Overweight."
            msg=messagebox.showinfo("Result",res)
        elif bmi>30.0 and bmi<=35.0:
            res="Your BMI is "+str(bmi)+"\nRemarks: Moderately obese!"
            msg=messagebox.showinfo("Result",res)
        elif bmi>35.0 and bmi<=40.0:
            res="Your BMI is "+str(bmi)+"\nRemarks: Severely obese!"
            msg=messagebox.showinfo("Result",res)
        else:
            res="Your BMI is "+str(bmi)+"\nRemarks: Super obese!!"
            msg=messagebox.showinfo("Result",res)
    
lb1=Label(top,bg="#cef0f1",text="Enter Weight (in kg):",bd=6,font = ("Helvetica", 10, "bold"))
lb1.place(x=80,y=30)

E1 = Entry(top, bd =7,width=6)
E1.place(x=230,y=30)

lb2=Label(top,bg="#cef0f1",text="Enter Height (in cm):",bd=6,font = ("Helvetica", 10, "bold"))
lb2.place(x=80,y=80)

E2 = Entry(top, bd =7,width=6)
E2.place(x=230,y=80)

button2 = Button( bg = "#2187e7", bd = 12,text = "BMI",  padx = 33, pady = 15,command = calcBMI, font = ("Helvetica", 20, "bold")) 
button2.grid(row = 3, column = 0, sticky = W)
button2.place(x=120,y=250)   
     
top.mainloop()
