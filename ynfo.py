# So far just a black screen
# Soon, something else. Maybe.
from tkinter import *

stage = Tk()

stage.attributes("-fullscreen", True)
stage.configure(background='black')
stage.focus_set()
stage.bind("<Escape>", quit)

stage.mainloop()