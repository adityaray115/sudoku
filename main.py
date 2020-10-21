from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('SUDOKU SOLVER')
rootwidth=1150
rootheight=690
root.minsize(rootwidth,rootheight)
root.maxsize(rootwidth,rootheight)

def newg():
    messagebox.showinfo('Message','NEW GAME pressed.')

def saveg():
    messagebox.showinfo('Message','SAVE pressed.')

def solveg():
    messagebox.showinfo('Message','SOLVE pressed.')

def checkg():
    messagebox.showinfo('Message','CHECK pressed.')

def resetg():
    messagebox.showwarning('Warning','Timer will not stop.')
    ans=messagebox.askyesno('Confirm','Are you sure you want to reset?')

def exitg():
    messagebox.showinfo('Message','EXIT pressed.')

#Main Frame
mainframe=Frame(root,bg='yellow')
mainframe.pack(expand=True,fill='both')

#Title of the Application
titleframe=Frame(mainframe,bg='green')
title=Label(titleframe,text='SUDOKU',font=('arial black',70,'bold','underline'),fg='red',bg='green')
title.pack()
titleframe.pack(anchor=N,fill='x')

#Interaction Area for User
leftframe=Frame(mainframe,bg='light blue',width=300)
namelabel=Label(leftframe,text='Enter Name:',bg='light blue',font=('Arial',15))
namelabel.place(x=5,y=20)
entryname=Entry(leftframe,width=15,font=('Arial',15),fg='red')
entryname.place(x=125,y=20)
difficulty=Label(leftframe,text='Difficulty:',bg='light blue',font=('Arial',15))
difficulty.place(x=5,y=60)
newgame=Button(leftframe,text='NEW GAME',bg='light green',font=('Arial',15),command=newg)
newgame.place(x=90,y=300)
checkgame=Button(leftframe,text='CHECK',bg='light green',font=('Arial',15),command=checkg)
checkgame.place(x=170,y=350)
solvegame=Button(leftframe,text='SOLVE',bg='light green',font=('Arial',15),command=solveg)
solvegame.place(x=50,y=350)
savegame=Button(leftframe,text='SAVE',bg='light green',font=('Arial',15),command=saveg)
savegame.place(x=50,y=400)
resetgame=Button(leftframe,text='RESET',bg='light green',font=('Arial',15),command=resetg)
resetgame.place(x=170,y=400)
exitgame=Button(leftframe,text='EXIT',bg='light green',font=('Arial',15),command=exitg)
exitgame.place(x=90,y=450)
diff=StringVar()
diff.set('SELECT')
diffselect=OptionMenu(leftframe,diff,'EASY','NORMAL','HARD')
diffselect.config(font=('Arial',10,'italic'),fg='red')
diffselect.place(x=100,y=60)
leftframe.pack(side=LEFT,fill='y')

#Details display
rightframe=Frame(mainframe,bg='light blue',width=300)
username=Label(rightframe,text='Username:',bg='light blue',font=('Arial',15))
username.place(x=5,y=20)
time=Label(rightframe,text='Time:',bg='light blue',font=('Arial',15))
time.place(x=5,y=60)
rightframe.pack(side=RIGHT,fill='y')

#Play Area
gridframe=Frame(mainframe,bg='blue')
for i in range(1,10):
    for j in range(1,10):
        count=1
        entry=Entry(gridframe,width=2,font=('arial balck',30),fg='red')
        entry.grid(row=i,column=j,padx=5,pady=5)
        j=j+1
        count=count+1
    i=i+1
gridframe.pack(side=TOP,pady=10)

root.mainloop()

'''root.geometry('450x450')
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
var=StringVar()'''