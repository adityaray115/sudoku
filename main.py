from tkinter import *
root=Tk()
root.geometry('450x450')
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