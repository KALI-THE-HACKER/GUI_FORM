"""
GUI Covaxin form(not real registration form of covaxin,it's just an form project) 
using tkinter [Python3]

This script is a simple implementation of GUI Form using python with a touch of graphics using 
tkinter framework.

This script will save all your input data in a csv file - Covaxin_data.csv,when u submit it,
and another time you fill the form and submit it,it will automatically save your new data in
the same csv file without harming your old data.

Author : Lucky Verma (https://github.com/luckyverma-sudo)
Created on : May 7, 2021

Authors contributed to this script (Add your name below if you have contributed) :
1. Lucky Verma (github:https://github.com/luckyverma-sudo/, email:luckyv0545746@gmail.com)
"""

# Importing the required functions and modules
try:
    from tkinter import *
    from tkinter import messagebox
    import csv
    import time
except Exception as e:
    # If there are any errors encountered during the importing of the modules, then we display the error on the console screen

    input(f'\n[ Error : {e} ]\nPress enter key to continue...')


root = Tk()

# Title of our GUI window and our project
root.title("Registration form for Covaxin")
# Default size of our form window
root.geometry("500x600")
# Minimum size of our form window
root.minsize(500, 600)
# Maximum size of our form window
root.maxsize(500, 600)

# calling the function for the 'SUBMIT' button for saving the data


def submit(event=NONE):
    # Converting our all input data into variables
    f_name = e1.get()
    l_name = e2.get()
    age = e3.get()
    gender = var.get()
    contact = e5.get()
    city = e6.get()
    pincode = e7.get()
    address = e8.get()

    # fullname of the user,by combinig first name and last name
    fullname = f_name+" "+l_name

    '''Checking that if the user input/fill all the entries,if all the entries are filled the
    script will continue but if not then it throws an error to fill the empty Entry'''
    if f_name:
        pass

    else:
        messagebox.showerror('error', "Please enter your First name!")
        return 0

    if l_name:
        pass

    else:
        messagebox.showerror('error', "Please enter your Last name!")
        return 0

    if age:
        pass

    else:
        messagebox.showerror('error', "Please enter your Age!")
        return 0

    if gender:
        pass

    else:
        messagebox.showerror('error', "Please select your Gender")
        return 0

    if contact:
        pass

    else:
        messagebox.showerror('error', "Please enter your Contact no.!")
        return 0

    if city:
        pass

    else:
        messagebox.showerror('error', "Please enter your City name!")
        return 0

    if pincode:
        pass

    else:
        messagebox.showerror('error', "Please enter your Area's Pincode!")
        return 0

    if address:
        pass

    else:
        messagebox.showerror('error', "Please enter your Address!")
        return 0

    '''If all the entries are filled by user,and then user click on submot button.it will show
    an message to the user'''

    messagebox.showinfo(
        'welcome', 'Your data is saving'+fullname+"...")
    # Sleep code for 2 seconds to make programme Good-Looking
    time.sleep(2)
    # Removing all the data filled by user in textfields after submitting the data
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    var.set(None)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)

    # Defining variable for RadioButton
    G = str(gender)

    # Converting values of RadioButton into varibale(text)
    if (G == '1'):
        gender = "male"

    elif (G == '2'):
        gender = "female"

    else:
        gender = "other"

    # Saving user input data in Covaxin_data.csv file
    with open('Covaxin_data.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow([">>> DATA OF "+fullname+"<<<"])
        w.writerow([])
        w.writerow(["Name = "+fullname])
        w.writerow(["Age = "+age])
        w.writerow(["Gender = "+gender])
        w.writerow(["Contact no. = "+contact])
        w.writerow(["City = "+city])
        w.writerow(["Pincode = "+pincode])
        w.writerow(["Address = "+address])
        w.writerow([])
        w.writerow(["##################################################"])
        w.writerow([])
    # Data saved successfully and showing an message to the user

    messagebox.showinfo('Congratulations!', 'Congrats '+fullname +
                        '!You are successfully registered for covaxin')

    # Sleep the script for 2 seconds and then terminate it
    time.sleep(2)
    root.destroy()


# Heading of our form
label = Label(root, text="Registration form for Covaxin",
              font=("consolas", 14, "bold", "underline"))
label.grid()
# Position of our Heading(with .place())
label.place(x=85, y=15)

# Defining var for RadioButton
var = IntVar()

# Main form frame,consist of all the Labels and Textfields
frame = Frame(root, bg=None, borderwidth=4, relief=GROOVE, pady=40, padx=40)
frame.grid(row=3, column=0, sticky="e")
# Position of main form frame
frame.place(x=45, y=80)

# Labels for the Form
# blank_l is a label with no text to make space between two labels to make our form Neat and Clean

l1 = Label(frame, text="First name  : ", font=("serif", 12))
l1.grid(row=3, column=0)

blank_l = Label(frame, text="").grid(row=4, column=0)

l2 = Label(frame, text="Last name  : ", font=("serif", 12))
l2.grid(row=5, column=0)

blank_l = Label(frame, text="").grid(row=6, column=0)

l3 = Label(frame, text="Age             : ", font=("serif", 12))
l3.grid(row=7, column=0)

blank_l = Label(frame, text="").grid(row=8, column=0)

l4 = Label(frame, text="Gender        : ", font=("serif", 12))
l4.grid(row=9, column=0)

blank_l = Label(frame, text="").grid(row=10, column=0)

l5 = Label(frame, text="Contact no.: ", font=("serif", 12))
l5.grid(row=11, column=0)

blank_l = Label(frame, text="").grid(row=12, column=0)

l6 = Label(frame, text="City            : ", font=("serif", 12))
l6.grid(row=13, column=0)

blank_l = Label(frame, text="").grid(row=14, column=0)

l7 = Label(frame, text="Pincode      : ", font=("serif", 12))
l7.grid(row=15, column=0)

blank_l = Label(frame, text="").grid(row=16, column=0)

l8 = Label(frame, text="Address      : ", font=("serif", 12))
l8.grid(row=17, column=0)


# Now,it's time for entries/imput user Info

e1 = Entry(frame, font=("serif", 12),)
e1.grid(row=3, column=1)

blank_l = Label(frame, text="").grid(row=4, column=1)

e2 = Entry(frame, font=("serif", 12))
e2.grid(row=5, column=1)

blank_l = Label(frame, text="").grid(row=6, column=1)

e3 = Entry(frame, font=("serif", 12))
e3.grid(row=7, column=1)

blank_l = Label(frame, text="").grid(row=8, column=1)

# RadioButtons for selecting Gender in our Form - 'e4'

e4 = Radiobutton(frame, text="M", variable=var, value=1, font=("serif", 12))
e4.grid(row=9, column=1, sticky='w')

e4 = Radiobutton(frame, text="F", variable=var, value=2, font=("serif", 12))
e4.grid(row=9, column=1, sticky='s')

e4 = Radiobutton(frame, text="other", variable=var,
                 value=3, font=("serif", 12))
e4.grid(row=9, column=1, sticky='e')


blank_l = Label(frame, text="").grid(row=10, column=1)

e5 = Entry(frame, font=("serif", 12))
e5.grid(row=11, column=1)

blank_l = Label(frame, text="").grid(row=12, column=1)

e6 = Entry(frame, font=("serif", 12))
e6.grid(row=13, column=1)

blank_l = Label(frame, text="").grid(row=14, column=1)

e7 = Entry(frame, font=("serif", 12))
e7.grid(row=15, column=1)

blank_l = Label(frame, text="").grid(row=16, column=1)

e8 = Entry(frame, font=("serif", 12))
e8.grid(row=17, column=1)

blank_l = Label(frame, text="").grid(row=18, column=0)
blank_l = Label(frame, text="").grid(row=19, column=0)

# It's submission time of the user data!

btn = Button(frame, text="SUBMIT", font=(
    "consolas", 14, "bold"), command=submit)
btn.grid(row=20, column=1)
btn.place(x=110, y=370)

# Code for auto-clicking on 'submit' button when pressed '<Return' or 'Enter' in common language
root.bind('<Return>', submit)

root.mainloop()

'''>>>END OF THE SCRIPT CODED BY LUCKY VERMA<<<
   >>>JOIN OUR ORGANIZATION ON GITHUB - github.com/wsb-org<<<'''
