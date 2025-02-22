import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import messagebox
from tkinter import *

driver = webdriver.Chrome()


def login(username, password):
    # selenium code to open the window and
    win.destroy()
    driver.maximize_window()
    driver.get("http://moodle.mitsgwalior.in/")
    link = driver.find_element(By.LINK_TEXT, "Log in")
    link.click()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginbtn").click()


def teachers(teachnames):
    print(teachnames)
    if teachnames.lower() == "dkj":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=344")

    elif teachnames.lower() == "aso":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=355")

    elif teachnames.lower() == "psharma":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=366")

    elif teachnames.lower() == "sk":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=530")

    elif teachnames.lower() == "ashish":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=771")

    elif teachnames.lower() == "vs":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=724")


def prompt(userchoice):
    x = userchoice.split()

    if "attendance" in x:

        win2.destroy()
        root = Tk()
        root.geometry("500x500")
        root.title("ATTENDANCE")

        enter_info = Label(root, text="Moodle Automation", bg="lightgrey", font=("Arial", 14))
        enter_info.grid(row=0, column=1, rowspan=1, columnspan=4, padx=5, pady=5)

        enter_info = Label(root, text="version = 0.1.1", bg="lightgrey")
        enter_info.grid(row=1, column=1, rowspan=1, columnspan=4, padx=5, pady=5)

        # For entering a text
        Label(root, text="Teacher Name ").grid(row=2)
        Label(root, text="Teacher Subject ").grid(row=3)

        teacher_entry = Entry(root, width=35)
        teacher_subject = Entry(root, width=35)
        teacher_entry.grid(row=2, column=2, padx=20, pady=20)
        teacher_subject.grid(row=3, column=2, padx=20, pady=20)

        # Button which says Click Here
        button1 = Button(root, text="Click Here",
                         command=lambda: teacher_attendance(teacher_entry.get(), teacher_subject.get())).grid(row=4,
                                                                                                              column=2,
                                                                                                              sticky=tk.W,
                                                                                                              pady=25,
                                                                                                              padx=25)

        root.mainloop()

    elif "page" in x:
        win2.destroy()
        var = Tk()
        var.geometry("500x500")
        var.title("Course Page")

        canvas = Canvas(var)
        canvas.create_text(200, 180, text="Moodle Automation", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(200, 220, text="Version: 0.0.1α", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(200, 250, text="Who's page do you want to access?", fill="black", font=('Helvetica 15 bold'))
        canvas.pack()

        # For entering a text
        userentry = Entry(var)
        userentry.pack()

        # Button which says Click Here
        button1 = Button(var, text="Click Here", command=lambda: teachers(userentry.get()))
        button1.pack()
        var.mainloop()


def teacher_attendance(teachername, subject):
    teachersplit = teachername.split()
    subjsplit = subject.split()

    if "dkj" in teachersplit and "transform" in subjsplit:
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=344&section=2")
        elems = driver.find_element(By.CLASS_NAME, "aalink")

        if len(str(elems)) > 0:
            driver.get("http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78375")

        else:
            messagebox.showinfo("Access Denied", "You are not enrolled in this Course")

    elif "dkj" in teachersplit and "nec" in subjsplit:
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=344&section=1")
        elems = driver.find_element(By.CLASS_NAME, "aalink")

        if len(str(elems)) > 0:
            driver.get("")

        else:
            messagebox.showinfo("Access Denied", "You are not enrolled in this Course")

    elif "skb" in teachersplit and "python" in subjsplit:
        #add this to the file which you have made
        # driver.get("http://moodle.mitsgwalior.in/course/view.php?id=590&section=4")
        driver.get("http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78742")
        driver.get("http://moodle.mitsgwalior.in/mod/attendance/attendance.php?sessid=171308&sesskey=SrYwK9fHuP")
        driver.find_element(By.CLASS_NAME, "form-check-input").click()
        driver.find_element(By.CLASS_NAME, "btn-btn-primary").click()


win = Tk()

# customization of the tkinter window
win.title("Moodle Automation")
win.geometry("400x350")
win.maxsize(500, 500)
win.config(bg="lightgrey")

enter_info = Label(win, text="Moodle Automation", bg="lightgrey", font=("Arial", 14))
enter_info.grid(row=0, column=1, rowspan=1, columnspan=4, padx=5, pady=5)

enter_info = Label(win, text="version = 0.1.1", bg="lightgrey")
enter_info.grid(row=1, column=1, rowspan=1, columnspan=4, padx=5, pady=5)

Label(win, text="Username").grid(row=2)
Label(win, text="Password").grid(row=3)

# userinput and password
userinput = Entry(win, width=35)
password = Entry(win, width=35, show="*")

userinput.grid(row=2, column=2, padx=20, pady=20)
password.grid(row=3, column=2, padx=20, pady=20)

# Button which says Click Here
tk.Button(win, text="Click Here to Start", command=lambda: login(userinput.get(), password.get())).grid(row=4, column=2,
                                                                                                        sticky=tk.W,
                                                                                                        pady=25,
                                                                                                        padx=25)

win.mainloop()

# window for user entry

win2 = Tk()

# customization of the tkinter window
win2.title("Moodle Automation")
win2.geometry("350x300")
win2.maxsize(500, 500)
win2.config(bg="lightgrey")

enter_info1 = Label(win2, text="Moodle Automation", bg="lightgrey", font=("Arial", 14))
enter_info1.grid(row=0, column=4, rowspan=1, columnspan=4, padx=10, pady=10)

enter_info3 = Label(win2, text="version = 0.1.1", bg="lightgrey")
enter_info3.grid(row=1, column=3, rowspan=1, columnspan=4, padx=10, pady=5, ipadx=5, ipady=5)

enter_info2 = Label(win2, text="What would you like to access?", bg="lightgrey", font=("Arial", 13))
enter_info2.grid(row=2, column=3, rowspan=1, columnspan=4, padx=10, ipady=5, ipadx=10)

# userinput and password
userinput = Entry(win2, width=35)

userinput.grid(row=3, column=5, padx=15, pady=15)

# Button which says Click Here
tk.Button(win2, text="Click Here", command=lambda: prompt(userinput.get())).grid(row=4, column=5, sticky=tk.W, pady=10,
                                                                                 padx=80, ipadx=5, ipady=5)

win2.mainloop()

time.sleep(5000)
