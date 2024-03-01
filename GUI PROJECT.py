from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
# import pyrebase
import os


abhiraj=Tk()
abhiraj.geometry('916x720')
abhiraj.minsize(300,100)
abhiraj.maxsize(700,600)

img=PhotoImage(file='AI.png')
ig=Label(abhiraj,image=img)
ig.pack()


def registration():
    name = Entry_name.get()
    email= Entry_email.get()
    number = Entry_number.get()
    gender = Entry_gender.get()
    registration= Entry_registration.get()
    father = Entry_father.get()
    mother = Entry_mother.get()

    dolo={"name" : name}
    db.child("user").push(dolo)
    mihir={"email" : email}
    db.child("user").push(mihir)
    adi={"number" : number}
    db.child("user").push(adi)
    abhi={"gender" : gender}
    db.child("user").push(abhi)
    aman={"registration no" : registration}
    db.child("user").push(aman)
    su={"father" : father}
    db.child("user").push(su)
    ab={"mother" : mother}
    db.child("user").push(ab)





    if name=='':
        messagebox.showerror('Error','please enter name')
    elif email=='':
        messagebox.showerror('Error','please enter email')
    elif number=='':
        messagebox.showerror('Error','please enter number')
    elif gender=='':
        messagebox.showerror('Error','please enter gender')
    elif registration=='':
        messagebox.showerror('Error','please enter registration')
    elif father=='':
        messagebox.showerror('Error','please enter father')
    elif mother=='':
            messagebox.showerror('Error', 'please enter mother')
    else :
        messagebox.showinfo('congrans','YOUR REGISTRATION SUCCESSFUL')

    print('REGISTRATION')




Entry_name=StringVar()
Entry_email=StringVar()
Entry_number=StringVar()
Entry_gender=StringVar()
Entry_registration=StringVar()
Entry_father=StringVar()
Entry_mother=StringVar()


abhiraj.title('DATASCIENCE FORM')
ABHIRAJ=Label(abhiraj,text='REGISTRATION FORM',font=('georgia',18),fg='white',bg='black')
ABHIRAJ.place(x=200,y=50)
Abhiraj=Label(text=' ENTER NAME',font=('arial,18,bold'),fg='white',bg='black')
Abhiraj.place(x=40,y=120)
Abhiraj=Label(text=' ENTER EMAIL',font=('arial,18,bold'),fg='white',bg='black')
Abhiraj.place(x=40,y=170)
Abhiraj=Label(text=' CONTACT NUMBER',font=('arial,18,bold'),fg='white',bg='black')
Abhiraj.place(x=40,y=220)
Abhiraj=Label(text=' GENDER',font=('arial,18,bold'),fg='white',bg='black')
Abhiraj.place(x=40,y=270)
Abhiraj=Label(text=' REGISTRATION NO.',font=('arial,18,bold'),fg='white',bg='black')
Abhiraj.place(x=40,y=320)
Abhiraj=Label(text=' FATHER NAME',font=('arial,18,bold'),fg='white',bg='black')
Abhiraj.place(x=40,y=370)
Abhiraj=Label(text=' MOTHER NAME',font=('arial,18,bold'),fg='white',bg='black')
Abhiraj.place(x=40,y=420)

mihir=Entry(abhiraj,font='10',textvariable=Entry_name)
mihir.place(x=250,y=120)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_email)
Abhi.place(x=250,y=170)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_number)
Abhi.place(x=250,y=220)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_gender)
Abhi.place(x=250,y=270)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_registration)
Abhi.place(x=250,y=320)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_father)
Abhi.place(x=250,y=370)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_mother)
Abhi.place(x=250,y=420)


b1=Button(abhiraj,fg='white',width=20,height=2,bg='black',text='SUBMIT',font=('georgia',10),command=registration)
b1.place(x=250,y=500)

def selection():
    value=radio.get()
    if value==1:
        GENDER='male'
        print(GENDER)
    else:
        GENDER='female'
        print(GENDER)








abhiraj.mainloop()