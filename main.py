from tkinter import *
from tkinter import messagebox
import numpy as np
import random
from numpy.random.mtrand import shuffle

root=Tk()
root.title('SUDOKU SOLVER')
rootwidth=1150
rootheight=690
root.minsize(rootwidth,rootheight)
root.maxsize(rootwidth,rootheight)


##-----------TIMER-------------------------
hour = minute = second = 0
def counter_label(timer):
    # global timer
    minute = 0
    second = 0
    def count():
        global second
        global minute
        global hour
        second = second + 1
        if second > 59:
            minute = minute + 1
            second = 0
            if minute > 59:
                hour = hour +1
                second=0
        timer.config(text = str(hour)+':'+str(minute)+':'+str(second))
        timer.after(1000,count)
    count()
#-----------

grid_choices_remaining=[]
for x in range(1,10):
    l=[]
    for y in range(1,10):
        l.append(y)
    grid_choices_remaining.append(l)
                #  entry=np.array([[Entry()]*9]*9)


def valid(x,y,n):
    for i in range(0,9):
        if entry[x][i].get()==str(n):
            return False
    for i in range(0,9):
        if entry[i][y].get()==str(n):
            return False
    for i in range(x-x%3,x-x%3+3):
        for j in range(y-y%3,y-y%3+3):
            if entry[i][j].get()==str(n):
                return False
    return True

def check_fill():
    for i in range(9):
        for j in range(9):
            if(entry[i][j].get()==''):
                return False
    return True

numberlist=list(range(1,10))


def fillGrid():
    #   global counter
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if entry[row][col].get()=='':
      shuffle(numberlist)      
      for value in numberlist:
        value=str(value)
        #Check that this value has not already be used on this row
        if not value in (entry[row][0].get(),entry[row][1].get(),entry[row][2].get(),entry[row][3].get(),entry[row][4].get(),entry[row][5].get(),entry[row][6].get(),entry[row][7].get(),entry[row][8].get()):
            if not value in (entry[0][col].get(),entry[1][col].get(),entry[2][col].get(),entry[3][col].get(),entry[4][col].get(),entry[5][col].get(),entry[6][col].get(),entry[7][col].get(),entry[8][col].get()):
                #Identify which of the 9 squares we are working on
                square=[]
                l=[]
                for i in range(row-row%3,row-row%3+3):
                    for j in range(col-col%3,col-col%3+3):
                        l.append(entry[i][j].get())
                #Check that this value has not already be used on this 3x3 square
                if not value in l:
                    entry[row][col].delete(0,END)
                    entry[row][col].insert(0,str(value))
                    if check_fill():
                        return True
                    else:
                        if fillGrid():
                            return True
            
      break
  entry[row][col].delete(0,END)        
  entry[row][col].insert(0,str(''))


def newg():
    global timer
    if entryname.get()=='' and diff.get()=='SELECT':
        messagebox.showerror('Error','Enter name and select difficulty level.')
    elif entryname.get()=='':
        messagebox.showerror('Error','Name field should not be empty.')
    elif diff.get()=='SELECT':
        messagebox.showerror('Error','Difficulty level not selected.')
    else:
        resetgrid(entry)
        newbuttonpressed()
        counter_label(timer)
        fillGrid()
        count=0
        if diff.get()=='EASY':count=40
        elif diff.get()=='NORMAL':count=50
        elif diff.get()=='HARD':count=60
        print(diff.get())
        while count>0:
            row=random.randint(0,8)
            col=random.randint(0,8)
            if not entry[row][col].get()=='':
                entry[row][col].delete(0,END)
                entry[row][col].insert(0,str(''))
                count-=1

def saveg():
    messagebox.showinfo('Message','SAVE pressed.')    

def solveg():
    messagebox.showinfo('Message','SOLVE pressed.')

def checkg():
    messagebox.showinfo('Message','CHECK pressed.')

def resetg():
    messagebox.showwarning('Warning','Timer will not stop.')
    ans=messagebox.askyesno('Confirm','Are you sure you want to reset?')
    if ans==1:
        resetgrid(entry)
    else:
        pass

def exitg():
    ex1=messagebox.askyesno('Warning','Any unsaved changes may be lost. Do you want to continue?')
    if ex1==1:
        ex2=messagebox.askyesno('Close Game','Do you want to exit the application?')
        if ex2==1:
            root.destroy()
        else:
            exitbuttonpressed()
            resetgrid(entry)
            disname.configure(text=entryname.get())
            diffright2.configure(text='')
            username['state']=DISABLED
            time['state']=DISABLED
            diffright1['state']=DISABLED
    else:
        pass

def newbuttonpressed():
    messagebox.showinfo('Game','Lets Play.....'+entryname.get())
    disname.configure(text=entryname.get())
    diffright2.configure(text=diff.get())
    entryname.delete(0,END)
    # diff.set('SELECT')
    entryname['state']=DISABLED
    diffselect['state']=DISABLED
    namelabel['state']=DISABLED
    difficulty['state']=DISABLED
    newgame['state']=DISABLED
    checkgame['state']=NORMAL
    solvegame['state']=NORMAL
    savegame['state']=NORMAL
    resetgame['state']=NORMAL
    exitgame['state']=NORMAL
    username['state']=NORMAL
    time['state']=NORMAL
    diffright1['state']=NORMAL

def exitbuttonpressed():
    entryname['state']=NORMAL
    entryname.configure(text='')
    diffselect['state']=NORMAL
    diff.set('SELECT')
    namelabel['state']=NORMAL
    difficulty['state']=NORMAL
    newgame['state']=NORMAL
    checkgame['state']=DISABLED
    solvegame['state']=DISABLED
    savegame['state']=DISABLED
    resetgame['state']=DISABLED
    exitgame['state']=DISABLED

def resetgrid(entry):
    for i in range(9):
        for j in range(9):
            entry[i][j].delete(0,END)

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
exitgame=Button(leftframe,text='EXIT GAME',bg='light green',font=('Arial',15),command=exitg)
exitgame.place(x=90,y=450)
diff=StringVar()
diff.set('SELECT')
diffselect=OptionMenu(leftframe,diff,'EASY','NORMAL','HARD')
diffselect.config(font=('Arial',10,'italic'),fg='red')
diffselect.place(x=100,y=60)
exitbuttonpressed()
leftframe.pack(side=LEFT,fill='y')

#Details display
rightframe=Frame(mainframe,bg='light blue',width=300)
username=Label(rightframe,text='Username:',bg='light blue',font=('Arial',15))
username.place(x=5,y=20)
disname=Label(rightframe,bg='light blue',font=('Arial',15),fg='red')
disname.place(x=105,y=20)
diffright1=Label(rightframe,text='Difficulty:',bg='light blue',font=('Arial',15))
diffright1.place(x=5,y=60)
diffright2=Label(rightframe,bg='light blue',font=('Arial',15),fg='red')
diffright2.place(x=90,y=60)
time=Label(rightframe,text='Time:',bg='light blue',font=('Arial',15))
time.place(x=5,y=100)
timer=Label(rightframe,bg='light blue',font=('Arial',15),fg='red')
timer.place(x=70,y=100)
username['state']=DISABLED
time['state']=DISABLED
diffright1['state']=DISABLED
rightframe.pack(side=RIGHT,fill='y')

#Play Area
canvas1 = Canvas(mainframe, width = 455, height = 455)
canvas1.pack(pady=44)
canvas1.create_line(155, 0,155,500)
canvas1.create_line(305, 0,305,500)
canvas1.create_line(5, 155,500,155)
canvas1.create_line(5, 305,500,305)

entry=np.array([[Entry()]*9]*9)
x=30
y=30
for i in range(9):
    for j in range(9):
        entry[i][j] = Entry(canvas1,width=2,font=('arial balck',30),fg='red',justify='center')
        canvas1.create_window(x+i*50,y+j*50,window=entry[i][j])

root.mainloop()


#Aniket's Play Area using 
# gridframe=Frame(mainframe,bg='blue')
# for i in range(1,10):
#     for j in range(1,10):
#         count=1
#         entry=Entry(gridframe,width=2,font=('arial balck',30),fg='red')
#         entry.grid(row=i,column=j,padx=5,pady=5)
#         j=j+1
#         count=count+1
#     i=i+1
# gridframe.pack(side=TOP,pady=10)


###Menu Code For Just in Case
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