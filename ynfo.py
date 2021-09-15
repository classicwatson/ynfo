# So far just a black screen
# Soon, something else. Maybe.
from tkinter import *
from time import localtime, strftime

def liveTimeDate():
    time = strftime("%-I:%M:%S%p", localtime())
    date = strftime("%a, %b %d, %Y", localtime())
    timeModule.config(text=time.lower())
    dateModule.config(text=date)
    root.after(1000, liveTimeDate)


root = Tk()

# Main window settings
root.attributes("-fullscreen", True)
root.configure(background='black')
root.focus_set()
root.bind("<Escape>", lambda e: root.destroy())
root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=1)

#spacer columns & rows between frames
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

#3x3 frames layout
topleft = Frame(root, bg='black')
topmid = Frame(root, bg='black')
topright = Frame(root, bg='black')
midleft = Frame(root, bg='black')
midmid = Frame(root, bg='black')
midright = Frame(root, bg='black')
bottomleft = Frame(root, bg='black')
bottommid = Frame(root, bg='black')
bottomright = Frame(root, bg='black')

#populate frames
dateModule = Label(topleft, fg='white', bg='black', font=("Arial Bold", 16))
timeModule = Label(topleft, fg='white', bg='black', font=("Arial Bold", 30))
weatherModule = Label(topright, text='weather module goes here', fg='white', bg='black', font=("Arial Bold", 24))
newsModule = Label(bottommid, text='news module goes here', fg='white', bg='black', font=("Arial Bold", 24))

dateModule.grid()
timeModule.grid()
weatherModule.grid()
newsModule.grid()

#populate grid
topleft.grid(row=0, column=0, padx=45, pady=45)
topmid.grid(row=0, column=2)
topright.grid(row=0, column=4, padx=45, pady=45)
midleft.grid(row=2, column=0)
midmid.grid(row=2, column=2)
midright.grid(row=2, column=4)
bottomleft.grid(row=4, column=0)
bottommid.grid(row=4, column=2, pady=45)
bottomright.grid(row=4, column=4)

liveTimeDate()

root.mainloop()