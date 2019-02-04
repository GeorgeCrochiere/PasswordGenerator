from Tkinter import *
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Level 1 - Letters", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Level 3 - Letters and Numbers", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Level 3 - Letters, Numbers, and Symbols", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)
