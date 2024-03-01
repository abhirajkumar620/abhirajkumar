from tkinter import *
root=Tk()
root.geometry('600x400')

root.title('ABHRAJ NOTEBBOOK')

scroll=Scrollbar(root,bg='black')
scroll.pack(side=RIGHT, fill=Y)

root.config(background='blue')

text=Text(root,yscrollcommand=scroll.set)

scroll.configure(command=text.yview)
text.pack(expand=1,fill=BOTH)


root.mainloop()




























