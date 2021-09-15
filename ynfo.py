# So far just a black screen
# Soon, something else. Maybe.
from tkinter import *

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
topleft = Frame(root)
topmid = Frame(root)
topright = Frame(root)
midleft = Frame(root)
midmid = Frame(root)
midright = Frame(root)
bottomleft = Frame(root)
bottommid = Frame(root)
bottomright = Frame(root)

#populate frames
time = Label(topleft, text='time', fg='white', bg='black', font=("Arial Bold", 70)).grid()
weather = Label(topright, text='weather', fg='white', bg='black', font=("Arial Bold", 70)).grid()
news = Label(bottommid, text='news goes here', fg='white', bg='black', font=("Arial Bold", 70)).grid()

#populate grid
topleft.grid(row=0, column=0)
topmid.grid(row=0, column=2)
topright.grid(row=0, column=4)
midleft.grid(row=2, column=0)
midmid.grid(row=2, column=2)
midright.grid(row=2, column=4)
bottomleft.grid(row=4, column=0)
bottommid.grid(row=4, column=2)
bottomright.grid(row=4, column=4)

root.mainloop()