from tkinter import *
root=Tk()
root.geometry('450x450')

def empty():
    pass

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Easy", command=empty)
filemenu.add_command(label="New Medium", command=empty)
filemenu.add_command(label="New Hard", command=empty)
filemenu.add_separator()
filemenu.add_command(label="Validate", command=empty)
filemenu.add_command(label="Solve", command=empty)
filemenu.add_separator()
filemenu.add_command(label="Reset This Game", command=empty)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Options", menu=filemenu)
root.config(menu=menubar)
var=StringVar()
for i in range(1,10):
    for j in range(1,10):
        count=1
        entry=Entry(root,width=2,font=('arial balck',30))
        entry.grid(row=i,column=j)
        j=j+1
        count=count+1
    i=i+1
root.mainloop()
