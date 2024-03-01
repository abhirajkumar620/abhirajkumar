import tkinter
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import pyrebase


root=Tk()

root.geometry('600x404')
root.maxsize(600,400)
root.minsize(500,400)
root.title('STUDENT FORM')
root.configure(background='grey')



def forward_to_student_login_page():
    wlframe.destroy()
    root.update()
    login_page()


wlframe=Frame(root,borderwidth=2,width=580,height=390,highlightthickness=3)
wlframe.place(x=10,y=5)

wlframe.configure(background='#34495E')



l1=Label(wlframe,text='WELCOME TO STUDENT FORM',bg='black',fg='white',font=('georgia',15))
l1.place(x=150,y=20)

b1=Button(wlframe,text='LOGIN  STUDENT',bg='black',fg='blue',width=20,height=2,font=('georgia',10),command=forward_to_student_login_page)
b1.place(x=230,y=100)

b1=Button(wlframe,text='LOGIN ADMIN',bg='black',fg='blue',width=20,height=2,font=('georgia',10),command=forward_to_student_login_page)
b1.place(x=230,y=200)

W1=PhotoImage(file='STUDENT LOGIN.png')
W2=PhotoImage(file='LOGIN ADMIN.png')

E1=Label(root,text='',image=W1)
E1.place(x=160,y=90,width=70,height=70)

F1=Label(root,text='',image=W2)
F1.place(x=160,y=190,width=70,height=70)


def login_page():

    def back():
        wlframe.destroy()

    def enter():

        wlframe.destroy()
        root.update()
        welcome_page()



    wlframe1= Frame(root,borderwidth=2,width=580,height=390,highlightthickness=3)
    wlframe1.place(x=10,y=5)

    wlframe1.configure(background='#34495E')
    ABHIRAJ=Label(wlframe1,text='STUDENT LOGIN PAGE',font=('georgia',18),fg='white',bg='black')
    ABHIRAJ.place(x=150,y=30)
    Abhiraj=Label(wlframe1,text=' USERS ID NO.',font=('arial,18,bold'),fg='white',bg='black')
    Abhiraj.place(x=210,y=100)
    Abhiraj=Label(wlframe1,text=' PASSWORD',font=('arial,18,bold'),fg='white',bg='black')
    Abhiraj.place(x=220,y=180)

    mihir=Entry(wlframe1,font='10')
    mihir.place(x=185,y=140)
    Abhi=Entry(wlframe1,font='10',show='*')
    Abhi.place(x=185,y=220)

    A1=Button(wlframe1,text='Login',font=('georgia',15),bg='black',fg='white',command=enter)
    A1.place(x=230,y=280)




def welcome_page():


    ad_pth = StringVar()
    ad_pth.set('')

    def sel_adpic():
        pth = askopenfilename()


        if pth :

            img = ImageTk.PhotoImage(Image.open(pth).resize((100,100)))
            ad_pth.set(pth)

            a2_btn.config(image=img)
            a2_btn.image = img

    frame=Frame(root,borderwidth=2,width=580,height=390,highlightthickness=3)
    frame.place(x=10,y=5)
    frame.configure(background='#34495E')

    def registration():
      name = Entry_name.get()
      email= Entry_email.get()
      number = Entry_number.get()
      gender = Entry_gender.get()


      dolo={"name" : name}
      db.child("user").push(dolo)
      mihir={"email" : email}
      db.child("user").push(mihir)
      adi={"number" : number}
      db.child("user").push(adi)
      abhi={"gender" : gender}
      db.child("user").push(abhi)


      if name=='':
          messagebox.showerror('Error','please enter name')
      elif email=='':
          messagebox.showerror('Error','please enter email')
      elif number=='':
          messagebox.showerror('Error','please enter number')
      elif gender=='':
          messagebox.showerror('Error','please enter gender')

      else :
          messagebox.showinfo('congrats','YOUR REGISTRATION SUCCESSFUL')

      print('REGISTRATION')

    def back():
       frame.destroy()
       login_page()



    Entry_name=StringVar()
    Entry_email=StringVar()
    Entry_number=StringVar()
    Entry_gender=StringVar()


    ABHIRAJ=Label(frame,text='REGISTRATION FORM',font=('georgia',18),fg='white',bg='black')
    ABHIRAJ.place(x=170,y=50)

    Abhiraj=Label(frame,text=' ENTER NAME',font=('arial,18,bold'),fg='white',bg='black')
    Abhiraj.place(x=40,y=120)

    Abhiraj=Label(frame,text=' ENTER EMAIL',font=('arial,18,bold'),fg='white',bg='black')
    Abhiraj.place(x=40,y=170)

    Abhiraj=Label(frame,text=' CONTACT NUMBER',font=('arial,18,bold'),fg='white',bg='black')
    Abhiraj.place(x=30,y=220)

    Abhiraj=Label(frame,text=' GENDER',font=('arial,18,bold'),fg='white',bg='black')
    Abhiraj.place(x=60,y=270)



    mihir=Entry(frame,font='10',textvariable=Entry_name)
    mihir.place(x=220,y=120)

    Abhi=Entry(frame,font='10',textvariable=Entry_email)
    Abhi.place(x=220,y=170)

    Abhi=Entry(frame,font='10',textvariable=Entry_number)
    Abhi.place(x=220,y=220)

    Abhi=Entry(frame,font='10',textvariable=Entry_gender)
    Abhi.place(x=220,y=270)


    b1=Button(frame,fg='white',width=20,height=2,bg='black',text='SUBMIT',font=('georgia',10),command=registration)
    b1.place(x=220,y=330)

    A= Button(frame,text='⬅️',font='bold,15',bg='black',fg='white',command=back)
    A.place(x=1,y=1)



    a2=Frame(frame,highlightbackground='grey',highlightthickness=2,background='black')
    a2_btn= Button(a2,width=95,height=110, command=sel_adpic)
    a2_btn.pack()
    a2.place(x=470,y=5,width=100,height=110)





root.mainloop()


