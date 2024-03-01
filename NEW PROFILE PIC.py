import tkinter
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
# import pyrebase
import os


abhiraj=Tk()
abhiraj.geometry('916x600')
abhiraj.minsize(300,100)
abhiraj.maxsize(700,600)
abhiraj.configure(background='grey')
abhiraj.title('DATASCIENCE FORM')
'''img=PhotoImage(file='')
ig=Label(abhiraj,image=img)
ig.pack()'''

# Config ={
#         "apiKey": "AIzaSyBxkZJ0Nb-t6jlmy-xbqUofGONFYIQscrE",
#         "authDomain": "gui-b006c.firebaseapp.com",
#         "databaseURL": "https://gui-b006c-default-rtdb.firebaseio.com",
#         "projectId": "gui-b006c",
#         "storageBucket": "gui-b006c.appspot.com",
#         "messagingSenderId": "630443201038",
#         "appId": "1:630443201038:web:6bb76abb754cf353f5a25f"
#     }
#
# firebase=pyrebase.initialize_app(Config)
# db=firebase.database()


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

    else :
        messagebox.showinfo('congrans','YOUR REGISTRATION SUCCESSFUL')

    print('REGISTRATION')




Entry_name=StringVar()
Entry_email=StringVar()
Entry_number=StringVar()
Entry_gender=StringVar()


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

mihir=Entry(abhiraj,font='10',textvariable=Entry_name)
mihir.place(x=250,y=120)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_email)
Abhi.place(x=250,y=170)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_number)
Abhi.place(x=250,y=220)
Abhi=Entry(abhiraj,font='10',textvariable=Entry_gender)
Abhi.place(x=250,y=270)


b1=Button(abhiraj,fg='white',width=20,height=2,bg='black',text='SUBMIT',font=('georgia',10),command=registration)
b1.place(x=250,y=350)








Abhiraj.mainloop()