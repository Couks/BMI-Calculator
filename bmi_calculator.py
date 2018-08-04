# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 03:19:44 2018

@author: nilesh8757
"""
from tkinter import *
from tkinter import messagebox

TOP = Tk()

TOP.geometry("400x400")
TOP.configure(background="#307678")
TOP.title("BMI Calculator")
TOP.resizable(width=False, height=False)

def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height
def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight
def calculate_bmi():
    '''
       This function calculates the result
    '''
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height**2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif bmi > 15.0 and bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif bmi > 16.0 and bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif bmi >= 18.5 and bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif bmi > 25.0 and bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif bmi > 30.0 and bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif bmi > 35.0 and bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)
LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
               font=("Helvetica", 10, "bold"))
LABLE1.place(x=80, y=30)
ENTRY1 = Entry(TOP, bd=7, width=6)
ENTRY1.place(x=230, y=30)
LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Height (in cm):", bd=6,
               font=("Helvetica", 10, "bold"))
LABLE2.place(x=80, y=80)
ENTRY2 = Entry(TOP, bd=7, width=6)
ENTRY2.place(x=230, y=80)
BUTTON = Button(bg="#2187e7", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
                font=("Helvetica", 20, "bold"))
BUTTON.grid(row=3, column=0, sticky=W)
BUTTON.place(x=120, y=250)
TOP.mainloop()
