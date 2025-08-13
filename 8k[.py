from tkinter import *
root = Tk()
root.title("pung")

def showmessage():
    Label(text="ฐตวรรณ พงษ์พยัคฆ์", fg="purple", font="60",bg="white").pack()
    Label(text="5/8", fg="purple", font="60",bg="white").pack()
    Label(text="15", fg="purple", font="60",bg="white").pack()
     
x = Button(root,text="information", command=showmessage).pack()

root.geometry("500x500")
root.mainloop()     
    