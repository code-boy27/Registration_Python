"""
Created on Fri May 14 22:22:14 2020

@email_id : shubham.more26@gmail.com
@author: SHUBHAM MORE
"""
from tkinter import *
import datetime
import sqlite3
from tkinter import messagebox
import tkinter as tk

'''
# Database creation or connection
con = sqlite3.connect("registration.db")
query = con.cursor()

query.execute("""create table registration_data(
                First_name text,                
                Mobile integer,
                Gender text,
                DOB text ,
                Address text        
              
              
               )""")
con.commit()

con.close()
'''

# Root object and declaring Frame size
root = Tk()
root.geometry('800x700+350+200')
root.resizable(FALSE, FALSE)
root.title("Registration Form")
root.iconphoto(FALSE, tk.PhotoImage(file='icons8-registration-50.png'))
# Top Down Frame Creation

top = Frame(root, height=60, bg='gray')
top.pack(fill=X)

add_lbl = Label(top, text=' Registration  ', bg='skyblue', font=('Segoe Print bold', 30), background='gray')
add_lbl.place(x=250, y=-13)

down = Frame(root, height=550, bg='skyblue')
down.pack(fill=X)

botm = Frame(root, height=100, bg='skyblue')
botm.pack(fill=X)

# name ENTRY and LABLE
name_lbl = Label(down, text="NAME", font='arial', bg='skyblue')
name_lbl.place(x=140, y=60)
name_entry = Entry(down, width=20, font=('arial 15 bold', 15, 'bold'))
name_entry.place(x=270, y=60)
name_entry.focus_set()

# MObile ENTRY and LABLE

mob_lbl = Label(down, text="NUMBER", font='arial ', bg='skyblue')
mob_lbl.place(x=140, y=120)
mob_entry = Entry(down, width=20, font=('arial 15 bold', 15, 'bold'))
mob_entry.place(x=270, y=120)

# Gender
rb_lbl = Label(down, text="GENDER", font='arial ', bg='skyblue')
rb_lbl.place(x=140, y=190)

selected = StringVar(down)
selected.set('Female')


def get_selected():
    return selected.get()


rb_male = Radiobutton(down, text="Male", value="Male", variable=selected, font=('console', 13), bg='skyblue',
                      command=get_selected)
rb_male.place(x=270, y=190)
rb_female = Radiobutton(down, text="Female", value="Female", variable=selected, font=('console', 13), bg='skyblue',
                        command=get_selected)
rb_female.place(x=350, y=190)

# ------------------------------------- Calender START---------------------------------------------

# Calender label

cal_lbl = Label(down, text='DOB', bg='skyblue', font='arial')
cal_lbl.place(x=140, y=240)

# Day
day_veriable = StringVar(down)
day_veriable.set('Day')
opt_day = OptionMenu(down, day_veriable, *range(1, 32))
opt_day.config(width=4, font=('helvetica', 12))
opt_day.place(x=270, y=240)

# Months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']
months_veriable = StringVar(down)
months_veriable.set('Month')
opt_month = OptionMenu(down, months_veriable, *months)
opt_month.config(width=5, font=('Helvetica', 12))
opt_month.place(x=355, y=240)

# Year
current_year = datetime.datetime.now().year  # Get current year into current_year
year_veriable = StringVar(down)
year_veriable.set('Year')
opt_year = OptionMenu(down, year_veriable, *range(1990, current_year))
opt_year.config(width=4, font=('helvetica', 12))
opt_year.place(x=450, y=240)

# -------------------------------------------------CALENDER END-------------------------------------------------
# ADDRESS
add_lbl = Label(down, text='ADDRESS ', bg='skyblue', font='arial')
add_lbl.place(x=140, y=300)
get_add = StringVar()
get_add.set('address')
add_entry = Text(down, width=25, height=5, font='arial 15 ')
add_entry.place(x=270, y=300)

# ===========================================================================================
var = IntVar()
var.set(0)
cbn = Checkbutton(down, variable=var, text='I accept term and condition ', bg='skyblue', font='console')
cbn.place(x=140, y=450)

addres = StringVar()


def validation():
    if var.get() == 0:
        messagebox.showinfo('Error', "Plese select terms and condition to proceed..", icon='error')
    elif name_entry.get() == '':
        messagebox.showinfo('error', 'name can not be empty')

    elif mob_entry.get() == '' or not (len(mob_entry.get()) == 10):
        messagebox.showinfo('error', 'Enter correct mobile No')

    elif day_veriable.get() == 'Day' or months_veriable.get() == 'Month' or year_veriable.get() == 'Year':
        messagebox.showinfo('error', 'select a proper date')

    elif add_entry.get(1.0, END) == '\n':
        messagebox.showinfo('error', 'Adress can not be empty ')


    else:
        return TRUE


# validating user input if all data is valid save otherwise display error
def clear():
    mob_entry.delete(0, END)
    day_veriable.set('Day')
    months_veriable.set("Month")
    year_veriable.set('Year')
    add_entry.delete(1.0, END)
    name_entry.delete(0, END)
    name_entry.focus_set()


def save():
    if validation():

        con = sqlite3.connect("registration.db")
        query = con.cursor()
        # Open database connection to save data into database
        query.execute("INSERT INTO registration_data VALUES (:name, :num, :gender, :dob, :add)",
                      {'name': name_entry.get(),
                       'num': mob_entry.get(),
                       'gender': get_selected(),
                       'dob': day_veriable.get() + '/' + months_veriable.get() + '/' + year_veriable.get(),
                       'add': add_entry.get(1.0, END)
                       }
                      )
        # save data in to database and close the connection
        con.commit()
        data = con.execute('select * from registration_data')
        for item in data:
            print(item)
        con.close()
        clear()
        messagebox.showinfo("saved", "registration completed", icon='info')

add = PhotoImage(file=r"add.png")
photoimage = add.subsample(4, 4)
save = Button(down, text="Register  ",image=photoimage, compound=LEFT, font='console', command=save)
save.place(x=350, y=500)

mainloop()
