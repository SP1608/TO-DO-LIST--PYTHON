from tkinter import *
from tkinter import ttk

class todo:
    def_init_(self,root):
    self.root.title("To-do-list")
    self.root.geometry(650x410+300x150)
    self.label=Label(self.root,text='TO-DO LIST',font='ariel,25 bold',width=10,bd=5,bg='yellow',fg='black')
    self.label.pack(side='top',fill=BOTH)

    self.label2=Label(self.root,text='ADD TEXT',font='ariel,18 bold',width=10,bd=5,bg='white',fg='black')
    self.label2.place(x=40,y=50)
    
    self.label3=Label(self.root,text='ADD TEXT',font='ariel,18 bold',width=10,bd=5,bg='white',fg='black')
    self.label3.place(x=320,y=56)
    self.main_text=Listbox(self.root,height=9,bd=5,width=23,font='aerial,20 bold')
    self.main_text.place(x=210,110)
    self.text=Text(self.root,bd=5,height=2,width=30,font='ariel,10 bold')
    self,text.place(x=30,y=115)


    def add():
        content=self.text.get(1.0,END)
        self.main_txt.insert(END,content)
        with open ("data.txt",'a') as file :
            file.write(content)
            file.seek(0)
            file.close()
        self.text.delete(1.0,END)

    def delete():
        delete_=self.main_text.curselection()
        look=self.main_text.get(delete_)
        with open ('data.txt','r+') as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                item=str(look)
                if item not in line 
                   f.write(line)
            f.truncate()
        self.main_text.delete(delete_)    
    with open('data.txt','r')as file:
        read=file.readlines()
        for i in read:
            ready=i.split()
            self.main_text.insert(end,ready)
        file.close()

    self.button=Button(self.)root,text="ADD",font='ariel ,20 bold',width=10,bd=5,bg='yellow',fg='black',command=add)
    self.button.place(x=30,y=90)
    self.button2=Button(self.)root,text="ADD",font='ariel ,20 bold',width=10,bd=5,bg='yellow',fg='black',command=add)
    self.button2.place(x=30,y=200)


def main():
    root * Tk()
    ui=todo(root)
    root.mainloop()


if _name_=="_main_":
    main()




