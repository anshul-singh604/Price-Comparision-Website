from tkinter import *
from tkinter import ttk
import os
import pathlib  #for making a new dir
class comparison():
    root = Tk()
    root.title("Price comparision Website")
    root.geometry('2024x2024')

    def home(self):
        
        self.fg_color='red'
        self.bk_color='#35B481'
        
        self.root.configure(background=self.bk_color)
        
        self.label1=Label(self.root,text="\t Price Comparison Website\n",font=("Copperplate Gothic Bold",40),fg=self.fg_color,bg=self.bk_color)
        self.label1.grid(row=1,column=1)

        self.dummy=Label(self.root,text="",bg=self.bk_color)
        self.dummy.grid(row=1,columnspan=3,sticky=E+W+N+S,pady=120)

        
        self.label2=Label(self.root,text="Username:",font=("",25),fg=self.fg_color,bg=self.bk_color)
        self.label2.grid(row=2,column=0,sticky=E+W+N+S,padx=0)
        
        self.entry1=Entry(self.root,font=("",15),width=25)
        self.entry1.grid(row=2,column=1,sticky=W,padx=0)
        
        
        self.label3=Label(self.root,text="Password:",font=("",25),fg=self.fg_color,bg=self.bk_color)
        self.label3.grid(row=3,column=0,sticky=E+W+N+S)
        
        self.entry2=Entry(self.root,font=("",15),width=25)
        self.entry2.grid(row=3,column=1,sticky=W)
        
        self.button1=Button(self.root,text="Login",font=("",15),fg=self.fg_color,bg=self.bk_color,command=self.login)
        self.button1.grid(row=4,column=0,columnspan=2,sticky=W)
        
        self.button2=Button(self.root,text="Register",font=("",15),fg=self.fg_color,bg=self.bk_color,command=self.Register)
        self.button2.grid(row=4,column=1,columnspan=2,sticky=W)
        
        self.label4=Label(self.root,font=("",25),bg=self.bk_color)
        self.label4.grid(row=6,column=0,sticky=W+E)
        
   
        self.root.mainloop()
    def destroy_home(self):
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()   
        self.entry1.destroy()
        self.entry2.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.label4.destroy()
        self.dummy.destroy()
    def Register(self):
        self.destroy_home()
        self.rlabel1=Label(self.root,text="\t\tSignup Form\n\n",font=("",25),fg=self.fg_color,bg=self.bk_color)
        self.rlabel1.grid(row=0,column=0,sticky=E+W)
        
        
        self.rname=Label(self.root,text="Name:",font=("",25),fg=self.fg_color,bg=self.bk_color)
        self.rname.grid(row=1,column=0,sticky=E)
        
        self.rname_entry=Entry(self.root,font=("",15),width=25)
        self.rname_entry.grid(row=1,column=1,sticky=W)
        
        self.rlabel2=Label(self.root,text="Username:",font=("",25),fg=self.fg_color,bg=self.bk_color)
        self.rlabel2.grid(row=2,column=0,sticky=E)
        
        self.rentry1=Entry(self.root,font=("",15),width=25)
        self.rentry1.grid(row=2,column=1,sticky=W)
        
        
        self.rlabel3=Label(self.root,text="Password",font=("",25),fg=self.fg_color,bg=self.bk_color)
        self.rlabel3.grid(row=3,column=0,sticky=E)
        
        self.rentry2=Entry(self.root,font=("",15),width=25)
        self.rentry2.grid(row=3,column=1,sticky=W)
        
        self.rbutton1=Button(self.root,text="Register",font=("",15),fg=self.fg_color,bg=self.bk_color,command=self.register_sucess)
        self.rbutton1.grid(row=4,columnspan=2,sticky=E)
        
        self.rbutton2=Button(self.root,text="Back to Login",font=("",15),fg=self.fg_color,bg=self.bk_color,command=self.destroy_signup)
        self.rbutton2.grid(row=5,columnspan=2,sticky=E)
       
        self.rsucess=Label(self.root,font=("calibri",30),bg=self.bk_color)
        self.rsucess.grid(row=6,columnspan=3,sticky=E+W)
        
    
    def destroy_signup(self):
        self.rlabel1.destroy()
        self.rlabel2.destroy()
        self.rlabel3.destroy()
        self.rentry1.destroy()
        self.rentry2.destroy()
        self.rname.destroy()
        self.rbutton1.destroy()
        self.rbutton2.destroy()
        self.rsucess.destroy()
        self.rname_entry.destroy()
        self.home()
    def register_sucess(self):
        username_info=self.rentry1.get()
        password_info=self.rentry2.get()
        if(username_info ==''):
            self.rsucess.config(text="Invalid Username")
        elif(password_info ==''):
            self.rsucess.config(text="Invalid Password")
        else:
            fname=username_info+".txt"
            file=open(fname,"w+")
            file.write(username_info+"\n")
            file.write(password_info)
            file.close()
        
            self.rentry1.delete(0,END)
            self.rentry2.delete(0,END)
            self.rname_entry.delete(0,END)
        
            self.rsucess.config(text="Register Sucess")
      
    def login(self):
        username1=self.entry1.get()
        password1=self.entry2.get()
        fname=username1+".txt"
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        list_of_files=os.listdir()
        if(len(username1)==0):
            self.label4.config(text="Enter Credential")
        elif(len(username1)==0):
            self.label4.config(text="Enter Credential")
        elif fname in list_of_files:
            file1=open(fname,"r")
            verify=file1.read().splitlines()
            if password1 in verify:
                self.front()
            else:
                self.label4.config(text="Wrong Password")
        else:
            self.label4.config(text="User not found")
       
    
    
        
    def front(self):
        self.destroy_home()
        self.flabel=Label(self.root,text="\t\tWELCOME TO PRICE COMPARISION WEBSITE \n\n",font=("",20),fg=self.fg_color,bg=self.bk_color)
        self.flabel.grid(row=0,column=0)
        
        self.product_name=Label(self.root,text="PRODUCT NAME:",font=("",20),fg=self.fg_color,bg=self.bk_color)
        self.product_name.grid(row=1,column=0,sticky=E)
        
        self.product_name_entry=Entry(self.root,font=("",15),width=25)
        self.product_name_entry.grid(row=1,column=1,sticky=W)
        
        self.submit=Button(self.root,text="Submit",font=("",15),fg=self.fg_color,bg=self.bk_color,command=self.product_detail)
        self.submit.grid(row=2,columnspan=2,sticky=E)
        
        self.flipkart_label=Label(self.root,font=("",20),fg=self.fg_color,bg=self.bk_color)
        self.flipkart_label.grid(row=3,column=0)
        
        self.amazon_label=Label(self.root,font=("",20),fg=self.fg_color,bg=self.bk_color)
        self.amazon_label.grid(row=3,column=1)
            
    def product_detail(self):
        product=self.product_name_entry.get()+".txt"
        path1="F:/Btech 2nd year/3rd Semester/Projeccts 2nd year/anshul/Flipkart/"
        cpath1=path1+product
        entries1=os.listdir(path1)
        if product in entries1:
            file1=open(cpath1,"r")
            flipkart_data=file1.read()
        path2="F:/Btech 2nd year/3rd Semester/Projeccts 2nd year/anshul/Amazon/"
        cpath2=path2+product
        entries2=os.listdir(path2)
        if product in entries2:
            file2=open(cpath2,"r")
            amazon_data=file2.read()
            if(flipkart_data!='' and amazon_data!=''):
                self.flipkart_label.config(text=("FLIPKART\n"+flipkart_data))
                self.amazon_label.config(text=("AMAZON\n"+amazon_data))
   
        else:
            self.flipkart_label.config(text="DATA NOT FOUND")
               
            
        
        
        
            

if __name__=="__main__":
    user=comparison()        #making an object for user
    user.home()
