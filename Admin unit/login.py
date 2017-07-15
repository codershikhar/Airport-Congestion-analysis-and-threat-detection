from tkinter import *

import os

creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
logedIn = False

def login():
    global nameEL
    global pwordEL # More globals :D
    rootA = Tk() # This now makes a new window.

    def CheckLogin():
        global logedIn
        with open(creds) as f:
            data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
            uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
            pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it

        if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
            logedIn = True
            rootA.destroy()
        else:
            logedIn = False
            rootA.destroy()

    rootA.title('Login') # This makes the window title 'login'

    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah

    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)

    rootA.mainloop()
    return logedIn