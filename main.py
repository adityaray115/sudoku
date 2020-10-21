from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('SUDOKU SOLVER')
rootwidth=1150
rootheight=690
root.minsize(rootwidth,rootheight)
root.maxsize(rootwidth,rootheight)

def newg():
    if entryname.get()=='' and diff.get()=='SELECT':
        messagebox.showerror('Error','Enter name and select difficulty level.')
    elif entryname.get()=='':
        messagebox.showerror('Error','Name field should not be empty.')
    elif diff.get()=='SELECT':
        messagebox.showerror('Error','Difficulty level not selected.')
    else:
        messagebox.showinfo('Game','Lets Play.....'+entryname.get())
        Label(rightframe,text=entryname.get(),bg='light blue',font=('Arial',15),fg='red').place(x=105,y=20)
        entryname.delete(0,END)
        entryname['state']=DISABLED
        diffselect['state']=DISABLED
        namelabel['state']=DISABLED
        difficulty['state']=DISABLED
        checkgame['state']=NORMAL
        solvegame['state']=NORMAL
        savegame['state']=NORMAL
        resetgame['state']=NORMAL
        exitgame['state']=NORMAL
        username['state']=NORMAL
        time['state']=NORMAL

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
    ex1=messagebox.askyesno('Warning','Any unsaved changes may be lost. Do you want to continue?')
    if ex1==1:
        ex2=messagebox.askyesno('Close Game','Do you want to exit the application?')
        if ex2==1:
            root.destroy()
        else:
            pass
    else:
        pass

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
checkgame['state']=DISABLED
solvegame['state']=DISABLED
savegame['state']=DISABLED
resetgame['state']=DISABLED
exitgame['state']=DISABLED
leftframe.pack(side=LEFT,fill='y')

#Details display
rightframe=Frame(mainframe,bg='light blue',width=300)
username=Label(rightframe,text='Username:',bg='light blue',font=('Arial',15))
username.place(x=5,y=20)
time=Label(rightframe,text='Time:',bg='light blue',font=('Arial',15))
time.place(x=5,y=60)
rightframe.pack(side=RIGHT,fill='y')

#Play Area
canvas1 = Canvas(mainframe, width = 455, height = 455)
canvas1.pack(pady=50)

canvas1.create_line(155, 0,155,500)
canvas1.create_line(305, 0,305,500)
canvas1.create_line(5, 155,500,155)
canvas1.create_line(5, 305,500,305)

#1st block
entry00 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 30, window=entry00)
entry01 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 30, window=entry01)
entry02 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 30, window=entry02)

entry10 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 80, window=entry10)
entry11 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 80, window=entry11)
entry12 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 80, window=entry12)

entry20 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 130, window=entry20)
entry21 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 130, window=entry21)
entry22 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 130, window=entry22)


#2nd block
entry03 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 30, window=entry03)
entry04 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 30, window=entry04)
entry05 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 30, window=entry05)

entry13 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 80, window=entry13)
entry14 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 80, window=entry14)
entry15 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 80, window=entry15)

entry23 = Entry (root,width=2,font=('arial black',30),fg='red') 
canvas1.create_window(180, 130, window=entry23)
entry24 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 130, window=entry24)
entry25 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 130, window=entry25)


#3rd block
entry06 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 30, window=entry06)
entry07 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 30, window=entry07)
entry08 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 30, window=entry08)

entry16 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 80, window=entry16)
entry17 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 80, window=entry17)
entry18 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 80, window=entry18)

entry26 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 130, window=entry26)
entry27 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 130, window=entry27)
entry28 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 130, window=entry28)



#4th block
entry30 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 180, window=entry30)
entry31 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 180, window=entry31)
entry32 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 180, window=entry32)

entry40 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 230, window=entry40)
entry41 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 230, window=entry41)
entry42 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 230, window=entry42)

entry50 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 280, window=entry50)
entry51 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 280, window=entry51)
entry52 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 280, window=entry52)


#5th block
entry33 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 180, window=entry33)
entry34 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 180, window=entry34)
entry35 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 180, window=entry35)

entry43 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 230, window=entry43)
entry44 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 230, window=entry44)
entry45 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 230, window=entry45)

entry53 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 280, window=entry53)
entry54 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 280, window=entry54)
entry55 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 280, window=entry55)


#6th block
entry36 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 180, window=entry36)
entry37 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 180, window=entry37)
entry38 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 180, window=entry38)

entry46 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 230, window=entry46)
entry47 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 230, window=entry47)
entry48 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 230, window=entry48)

entry56 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 280, window=entry56)
entry57 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 280, window=entry57)
entry58 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 280, window=entry58)


#7th block
entry60 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 330, window=entry60)
entry61 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 330, window=entry61)
entry62 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 330, window=entry62)

entry70 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 380, window=entry70)
entry71 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 380, window=entry71)
entry72 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 380, window=entry72)

entry80 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(30, 430, window=entry80)
entry81 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(80, 430, window=entry81)
entry82 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(130, 430, window=entry82)


#8th block
entry63 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 330, window=entry63)
entry64 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 330, window=entry64)
entry65 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 330, window=entry65)

entry73 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 380, window=entry73)
entry74 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 380, window=entry74)
entry75 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 380, window=entry75)

entry83 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(180, 430, window=entry83)
entry84 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(230, 430, window=entry84)
entry85 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(280, 430, window=entry85)


#9th block
entry66 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 330, window=entry66)
entry67 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 330, window=entry67)
entry68 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 330, window=entry68)

entry76 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 380, window=entry76)
entry77 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 380, window=entry77)
entry78 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 380, window=entry78)

entry86 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(330, 430, window=entry86)
entry87 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(380, 430, window=entry87)
entry88 = Entry (root,width=2,font=('arial balck',30),fg='red') 
canvas1.create_window(430, 430, window=entry88)




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