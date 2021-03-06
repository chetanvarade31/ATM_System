import matplotlib.pyplot as plt
import pandas as pd
from tkinter.scrolledtext import ScrolledText
from tkinter import*
from tkinter.ttk import * 
from tkinter import *
from PIL import Image, ImageTk
import datetime
import time

named_tuple = time.localtime() 
time1 = time.strftime("%H:%M:%S", named_tuple)
present = datetime.datetime.now()
date = present.date()
day = present.strftime("%A")



global var1
global var2
global var3
global var4
global var5
global var6
global var7

class Events():
   
    def __init__(self,win):

        self.img = Image.open("bg.png")
        self.img = self.img.resize((3000,1000),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

        canava = Canvas(win, width= 800 ,height= 500)
        canava.create_image(0,0,image = self.photo)

        self.label1 = Label(win, text= "WELCOME IN ATM !!",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black",bd= "2")
        self.label1.place(x = 300, y= 15)

        self.create_account0 = Button(win, text= "CREATE ACCOUNT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= self.create_account)
        self.create_account0.place(x = 50, y= 100)

        self.enter_pin0  = Button(win,text= "ENTER PIN",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= self.enter_pin )
        self.enter_pin0.place(x = 350, y= 100)

        self.exit0 = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= self. exit_btn)
        self.exit0.place(x = 650, y= 100)
     
        canava.pack()
  
    def create_account(self):
        try:

            try :

                x = open("atm3.csv","r")
                x.read(5)

                self.label2 = Label(win, text= "Already Have A Account !! ",fg = "cyan", bg= "black",bd= "2",font = ("Arial",15,"bold"))
                self.label2.place(x = 200, y = 250)

                self.create_account0.destroy()
                self.enter_pin0.destroy()
            

            except FileNotFoundError as k:

                
                self.enter_pin0.destroy()
                
                self.label3 = Label(win,text= "CREDIT SOME AMOUNT TO CREATE YOUR ACCOUNT : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
                self.label3.place(x= 50,y= 200)

                self.lable0 = Label(win,text= "ENTER AMOUNT : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
                self.lable0.place(x= 50,y= 300)

                self.entry0 = Entry(win, textvariable= var1,font= ("Arial",15,"bold"),fg= "red",bg= "black",width= 15)
                self.entry0.place(x = 250, y = 300)
                
                self.submit0 = Button(win, text= "SUBMIT",font = ("Arial",15,"bold"),bd = "5",fg= "red" , bg= "black",command= root.submit_btn0)
                self.submit0.place(x = 50, y= 400)
            
                self.login.destroy()
                self.lable2.destroy()

        except AttributeError as at:
            pass   

    def submit_btn0(self):
        
        try:
            self.create_account0.destroy()
            self.label3.destroy()
            self.lable0.destroy()
            self.submit0.destroy()
            
            x =  self.entry0.get()
            y = int(x)
            global avl_balance
            avl_balance = 0
            avl_balance = avl_balance + y
            df = pd.DataFrame(
                {
                "CREDIT" :[y],
                "DEBIT" : [0],
                "DATE" :[date],
                "DAY" : [day],
                "TIME" : [time1],
                "AVL_BALANCE" :[avl_balance]
                }
            )
            
            df.to_csv("atm3.csv",mode = "a")
            t = pd.read_csv("atm3.csv",index_col= "AVL_BALANCE")

            self.entry0.destroy()

            self.create_pin0 = Button(win, text= "CREATE PIN ",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root.create_pin)
            self.create_pin0.place(x = 50, y= 100)

            self.entry1.destroy()
            self.label.destroy()
            self.label.destroy()
        except AttributeError as n:
            pass
       
    def create_pin(self):

        self.label3 = Label(win,text= "CREATE PIN : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.label3.place(x= 50,y= 200)
 
        self.entry = Entry(win, textvariable= var4,font= ("Arial",15,"bold"),fg= "red",bg= "black",width= 15)
        self.entry.place(x = 215, y = 200)
        
        self.submit = Button(win, text= "SUBMIT",font = ("Arial",15,"bold"),fg= "red",bd=  "5" , bg= "black",command= root.submit_btn)
        self.submit.place(x = 50, y= 300)
        try: 

            self.entry1.destroy()
            self.login.destroy()
            self.label.destroy()
            self.enter_pin0.destroy()
            self.lable2.destroy()
        except AttributeError :
            pass
    def submit_btn(self):
        x = self.entry.get()
        x = int(x)
        
        df = pd.DataFrame(
            {
                "PIN":[x]
            }
        )

        df.to_csv("pinatm.csv",mode="a")
        
        
        self.label3.destroy()
        self.entry.destroy()
        self.submit.destroy()

        self.label3 = Label(win,text= "CONFIRM PIN : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.label3.place(x= 50,y= 200)
 
        self.entry = Entry(win, textvariable= var4,font= ("Arial",15,"bold"),fg= "red",bg= "black",width= 15)
        self.entry.place(x = 215, y = 200)
        

        self.submit = Button(win, text= "SUBMIT",font = ("Arial",15,"bold"),fg= "red",bd = "5" , bg= "black",command= root.submit00_btn)
        self.submit.place(x = 50, y= 300)

    def submit00_btn(self):

        x = self.entry.get()
        x = int(x)     
        
        df = pd.DataFrame(
            {
                "PIN":[x]
            }
        )
        

        df.to_csv("pinatm.csv",mode="a")
        
        self.label3.destroy()
        self.entry.destroy()
        self.submit.destroy()
        self.create_pin0.destroy()

        self.enter_pin0  = Button(win,text= "ENTER PIN",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= self.enter_pin )
        self.enter_pin0.place(x = 350, y= 100)

        
    def enter_pin(self):
        try:
                
            file = open("atm3.csv","r")

            self.create_account0.destroy()

            self.label = Label(win,text= "ENTER PIN : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
            self.label.place(x= 180,y= 200)

            self.entry1 = Entry(win, textvariable= var2,font= ("Arial",15,"bold"),fg= "red",bg= "black",width= 15,show= "*")
            self.entry1.place(x = 380, y = 200)
            

            self.login = Button(win, text= "LOGIN",font = ("Arial",15,"bold"),fg= "red",bd = "5" , bg= "black",command= root.login_btn)
            self.login.place(x = 180, y= 300)

        except FileNotFoundError as file:
            self.create_account0.destroy()

            self.label13 = Label(win, text= "ACCOUNT NOT FOUND PLZ CREATE ACCOUNT !!",fg = "cyan",bg= "black", font = ("Arial",15,"bold"))       
            self.label13.place(x = 185,y= 300)

    def login_btn(self):

        x = self.entry1.get()
        
        try:
                
            df1  = pd.read_csv("pinatm.csv")
            self.label.destroy()

            if x in df1.values:
            
                self.entry1.destroy()
                self.login.destroy()
                self.label.destroy()
                self.enter_pin0.destroy()
        
                self.credit = Button(win, text= "CREDIT",font = ("Arial",15,"bold"),fg= "red", bd = "5" , bg= "black",command= root.credit_btn)
                self.credit.place(x = 250, y= 200)
                
                self.debit = Button(win, text= "DEBIT",font = ("Arial",15,"bold"),fg= "red",bd = "5" , bg= "black",command= root.debit_btn)
                self.debit.place(x = 400, y= 200)
                
                self.balance = Button(win, text= "BALANCE",font = ("Arial",15,"bold"),fg= "red",bd  = '5' , bg= "black",command= root.balance_btn)
                self.balance.place(x = 250, y= 300)
                
                self.history = Button(win, text= "TRN HISTORY",font = ("Arial",15,"bold"),fg= "red",bd=  "5" , bg= "black",command= root.history_btn)
                self.history.place(x = 400, y= 300)

                self.lable4 = Label(win,text= "SELECT BELOW ONE : ",font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
                self.lable4.place(x= 300,y= 100)
          
            else:
                
                self.label = Label(win,text= "ENTER VALID PIN :",font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
                self.label.place(x= 180,y= 200)

                var2.set("INVALID PIN")
                
        except FileNotFoundError as ab :

            self.lable2 = Label(win,text= "PLZ CREATE PIN !! ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
            self.lable2.place(x= 300,y= 300)

            self.create_pin0 = Button(win, text= "CREATE PIN ",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root.create_pin)
            self.create_pin0.place(x = 50, y= 100)

    def credit_btn(self):

        self.credit.destroy()
        self.debit.destroy()
        self.balance.destroy()
        self.history.destroy()
        self.lable4.destroy()

        self.lable3 = Label(win,text= "ENTER AMOUNT : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable3.place(x= 180,y= 100)

        self.entry3 = Entry(win, textvariable= var3,font= ("Arial",15,"bold"),fg= "red",bg= "black",width= 15)
        self.entry3.place(x = 400, y = 100)
        
        self.credit2 = Button(win, text= "CREDIT",font = ("Arial",15,"bold"),fg= "red" ,bd = "5", bg= "black",command= root.credit_btn2)
        self.credit2.place(x = 180, y= 200)


    def credit_btn2(self):
        
        # progress bar start
        import time

        self.lable11 = Label(win,text= " WAIT FEW SECONDS !! : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable11.place(x= 180,y= 300)

        self.progress = Progressbar(win, orient= HORIZONTAL,length=250,mode="determinate")
        self.progress.place(x = 180,y = 400)

        self.progress['value'] = 10
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 30
        win.update_idletasks()
        time.sleep(1)


        self.progress['value'] = 50
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 60
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 70
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 85
        win.update_idletasks()
        time.sleep(1)

    
        self.progress['value'] = 100
        win.update_idletasks()

        self.progress.destroy()

        # progress bar end 
        
        self.exit0.destroy()

        x =  self.entry3.get()
        y = int(x)
        t = pd.read_csv("atm3.csv")
        f = t["AVL_BALANCE"]
        b = f.tail(1)
        v = int(b)
        
        
        avl_balance = v + y
        
        df = pd.DataFrame(
            {
              "CREDIT" :[y],
              "DEBIT" : [0],
              "DATE" :[date],
              "DAY" : [day],
              "TIME" : [time1],
              "AVL_BALANCE" :[avl_balance]
            }
        )
        
        self.lable3.destroy()
        self.entry3.destroy()
        self.credit2.destroy()
        self.lable11.destroy()
       # self.clear0.destroy()

        df.to_csv("atm3.csv",mode = "a")
        t = pd.read_csv("atm3.csv",index_col= "CREDIT")
        t.dropna(axis= 0,inplace= True)

        t.drop("Unnamed: 0",axis= 1,inplace=True)
        
        t["DEBIT"] = t["DEBIT"].str.pad(10, side = "right")        
        
        t.reset_index(drop=True).style.set_properties(**{"text-align": "right"})
        
        x = t.tail(1)
        self.text_area = ScrolledText(win, 
                        wrap = "word",
                        width = 65,
                        height = 5,
                        font = 5,
                        fg = "yellow",
                        bg = "black"
                                     )
     
        self.text_area.place(x = 40, y = 100)
        
        self.text_area.insert(INSERT, x)

        self.lable5= Label(win,text = "AMOUNT IS SUCCESSFULLY CREDITED !!" ,font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable5.place(x= 180,y= 260)

        self.lable5= Label(win,text = "THANKS FOR USE !!\n  VISIT AGAIN !!" ,font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable5.place(x= 260,y= 320)

        self.exit = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root. exit_btn)
        self.exit.place(x = 320, y= 400)


    def debit_btn(self):
        self.credit.destroy()
        self.debit.destroy()
        self.balance.destroy()
        self.history.destroy()
        self.lable4.destroy()

        self.lable5 = Label(win,text= "ENTER AMOUNT : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable5.place(x= 180,y= 100)

        self.entry5 = Entry(win, textvariable= var3,font= ("Arial",15,"bold"),fg= "red",bg= "black",width= 15)
        self.entry5.place(x = 400, y = 100)
        
        self.debit2 = Button(win, text= "DEBIT",font = ("Arial",15,"bold"),fg= "red" ,bd= "5", bg= "black",command= root.debit_btn2)
        self.debit2.place(x = 180, y= 200)

    def debit_btn2(self):

        # progress bar start

        import time

        self.lable11 = Label(win,text= "  WAIT FEW SECONDS !! : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable11.place(x= 180,y= 300)

        self.progress = Progressbar(win, orient= HORIZONTAL,length=250,mode="determinate")
        self.progress.place(x = 180,y = 400)

        self.progress['value'] = 10
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 30
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 50
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 60
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 70
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 85
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 100
        win.update_idletasks()

        self.progress.destroy()

        # progress bar end

        self.exit0.destroy()

        h = self.entry5.get()
        h = int(h)
        t = pd.read_csv("atm3.csv")
        f = t["AVL_BALANCE"]
        b = f.tail(1)
        v = int(b)
        if h <= v :

            avl_balance = v - h

            df1 = pd.DataFrame(
                {
                "CREDIT" :[0],
                "DEBIT" : [h],
                "DATE" :[date],
                "DAY" : [day],
                "TIME" : [time1],
                "AVL_BALANCE" :[avl_balance]
                }
            )

            self.entry5.destroy()
            self.lable5.destroy()
            self.debit2.destroy()
            self.lable11.destroy()
       
            df1.to_csv("atm3.csv",mode = "a")
            t = pd.read_csv("atm3.csv",index_col= "DEBIT")
            t.dropna(axis= 0,inplace= True)

            t.drop("Unnamed: 0",axis= 1,inplace=True)
            
            t["CREDIT"] = t["CREDIT"].str.pad(10, side = "right")
            
            t.reset_index(drop=True).style.set_properties(**{"text-align": "right"})
            
            x = t.tail(1)
            self.text_area = ScrolledText(win, 
                            wrap = "word",
                            width = 65,
                            height = 5,
                            font = 5,
                            fg = "yellow",
                            bg = "black"
                                        )

            
            self.text_area.place(x = 30, y = 100)
            
            self.text_area.insert(INSERT, x)

            self.lable5= Label(win,text = "AMOUNT IS SUCCESSFULLY DEBITED !!" ,font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
            self.lable5.place(x= 180,y= 260)

            self.lable5= Label(win,text = "THANKS FOR USE !!\n  VISIT AGAIN !!" ,font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
            self.lable5.place(x= 260,y= 320)

            self.exit = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root. exit_btn)
            self.exit.place(x = 320, y= 400)

        else :
            
            self.entry5.destroy()
            self.lable5.destroy()
            self.debit2.destroy()
            self.lable11.destroy()


            self.exit = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root. exit_btn)
            self.exit.place(x = 320, y= 400)

            self.label12 = Label(win, text= "INSUFFICIENT  BALANCE !!", fg = "cyan", bg= "black",font= ("Arial", 15,"bold"))
            self.label12.place(x = 200, y = 300)
            

    def balance_btn(self):

        self.exit0.destroy()
        self.credit.destroy()
        self.debit.destroy()
        self.balance.destroy()
        self.history.destroy()
        self.lable4.destroy()

        self.lable3 = Label(win,text= "AVAILABLE BALANCE : ",textvariable= var7,font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable3.place(x= 250,y= 80)
        t = pd.read_csv("atm3.csv")
        f = t["AVL_BALANCE"]
        b = f.tail(1)
        avl_balance = int(b)
        var7.set(f"AVAILABLE BALANCE :   {avl_balance}")

        self.lable6= Label(win,text = "THANKS FOR USE !!\n  VISIT AGAIN !!" ,font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable6.place(x= 280,y= 150)

        self.exit = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root. exit_btn)
        self.exit.place(x = 320, y= 250)
        
    def history_btn(self):
         
        self.credit.destroy()
        self.debit.destroy()
        self.balance.destroy()
        self.history.destroy()
        self.lable4.destroy()
        
        self.last_ten = Button(win, text= "LAST TEN",font = ("Arial",15,"bold"),fg= "red",bd = "5" , bg= "black",command= root.last_tenbtn)
        self.last_ten.place(x = 250, y= 200)
        
        self.first_ten = Button(win, text= "FIRST TEN",font = ("Arial",15,"bold"),fg= "red",bd = "5" , bg= "black",command= root.first_tenbtn)
        self.first_ten.place(x = 400, y= 200)
        
        self.all = Button(win, text= "ALL",font = ("Arial",15,"bold"),fg= "red" ,bd = "5", bg= "black",command= root.all_btn)
        self.all.place(x = 250, y= 300)
        
        
        self.lable8 = Label(win,text= "SELECT BELOW ONE : ",font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable8.place(x= 300,y= 100)

    def last_tenbtn(self):
        # progress bar start
        import time

        self.lable11 = Label(win,text= " WAIT FEW SECONDS !! : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable11.place(x= 300,y= 360)

        self.progress = Progressbar(win, orient= HORIZONTAL,length=250,mode="determinate")
        self.progress.place(x = 300,y = 420)

        self.progress['value'] = 10
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 30
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 50
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 60
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 70
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 85
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 100
        win.update_idletasks()

        self.progress.destroy()

        # progress bar end

        self.exit0.destroy()
        self.all.destroy()
        self.last_ten.destroy()
        self.first_ten.destroy()
        self.lable8.destroy()
        self.lable11.destroy()

        t = pd.read_csv("atm3.csv",index_col= "DATE")
        t.dropna(axis= 0,inplace= True)

        t.drop("Unnamed: 0",axis= 1,inplace=True)
        
        t["CREDIT"] = t["CREDIT"].str.pad(15, side = "right")
        
        
        t.reset_index(drop=True).style.set_properties(**{"text-align": "right"})
        
        x = t.tail(10)
        self.text_area = ScrolledText(win, 
                        wrap = "word",
                        width = 65,
                        height = 7,
                        font = 3,
                        fg = "yellow",
                        bg = "black"
                                        )

        
        self.text_area.place(x = 30, y = 120)
        
        self.text_area.insert(INSERT, x)

        self.lable7 = Label(win,text= "LAST 10 TRANSACTIONS HISTORY : ",font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable7.place(x= 235,y= 65)

        self.lable6= Label(win,text = "THANKS FOR USE !!\n  VISIT AGAIN !!" ,font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable6.place(x= 280,y= 300)

        self.exit = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root. exit_btn)
        self.exit.place(x = 340, y= 380)
        
        
    def first_tenbtn(self):

        # progress bar start
        import time

        self.lable11 = Label(win,text= " WAIT FEW SECONDS !! : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable11.place(x= 300,y= 360)

        self.progress = Progressbar(win, orient= HORIZONTAL,length=250,mode="determinate")
        self.progress.place(x = 300,y = 420)

        self.progress['value'] = 10
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 30
        win.update_idletasks()
        time.sleep(1)


        self.progress['value'] = 50
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 60
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 70
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 85
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 100
        win.update_idletasks()

        self.progress.destroy()

        # progress bar end

        self.exit0.destroy()
        self.all.destroy()
        self.last_ten.destroy()
        self.first_ten.destroy()
        self.lable8.destroy()
        self.lable11.destroy()
        
        t = pd.read_csv("atm3.csv",index_col= "DATE")
        t.dropna(axis= 0,inplace= True)

        t.drop("Unnamed: 0",axis= 1,inplace=True)
        
        t["CREDIT"] = t["CREDIT"].str.pad(15, side = "right")
            
        t.reset_index(drop=True).style.set_properties(**{"text-align": "right"})
        
        x = t.head(10)
        self.text_area = ScrolledText(win, 
                        wrap = "word",
                        width = 65,
                        height = 7,
                        font = 3,
                        fg = "yellow",
                        bg = "black"
                                        )

        
        self.text_area.place(x = 30, y = 120)
        
        self.text_area.insert(INSERT, x)

        self.lable7 = Label(win,text= "FIRST 10 TRANSACTIONS HISTORY : ",font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable7.place(x= 235,y= 65)

        self.lable6= Label(win,text = "THANKS FOR USE !!\n  VISIT AGAIN !!" ,font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable6.place(x= 280,y= 300)

        self.exit = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root. exit_btn)
        self.exit.place(x = 340, y= 380)

    def all_btn(self):

        # progress bar start
        import time

        self.lable11 = Label(win,text= " WAIT FEW SECONDS !! : ",font = ("Arial",15,"bold"),fg= "yellow" , bg= "black")
        self.lable11.place(x= 300,y= 360)

        self.progress = Progressbar(win, orient= HORIZONTAL,length=250,mode="determinate")
        self.progress.place(x = 300,y = 420)

        self.progress['value'] = 10
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 30
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 50
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 60
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 70
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 85
        win.update_idletasks()
        time.sleep(1)

        self.progress['value'] = 100
        win.update_idletasks()

        self.progress.destroy()

        # progress bar end

        self.exit0.destroy()
        self.all.destroy()
        self.last_ten.destroy()
        self.first_ten.destroy()
        self.lable8.destroy()
        self.lable11.destroy()
        
        t = pd.read_csv("atm3.csv",index_col= "DATE")
        pd.set_option('display.max_row',t.shape[0]+1)
        pd.set_option('display.max_columns',t.shape[0]+1)
        t.dropna(axis= 0,inplace= True)

        t.drop("Unnamed: 0",axis= 1,inplace=True)
        
        t["CREDIT"] = t["CREDIT"].str.pad(15, side = "right")
        
        
        t.reset_index(drop=True).style.set_properties(**{"text-align": "right"}) 
        
        self.text_area = ScrolledText(win, 
                        wrap = "word",
                        width = 65,
                        height = 7,
                        font = 3,
                        fg = "yellow",
                        bg = "black"
                                        )

        
        self.text_area.place(x = 30, y = 120)
        
        self.text_area.insert(INSERT, t)

        self.lable7 = Label(win,text= "ALL TRANSACTIONS HISTORY : ",font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable7.place(x= 235,y= 65)


        self.lable6= Label(win,text = "THANKS FOR USE !!\n  VISIT AGAIN !!" ,font = ("Arial",15,"bold"),fg= "cyan" , bg= "black")
        self.lable6.place(x= 280,y= 300)

        self.exit = Button(win,text= "EXIT",font = ("Arial",15,"bold"),fg= "red" , bg= "black",bd= "5",command= root.exit_btn)
        self.exit.place(x = 250, y= 380)

        self.showgraph = Button(win, text= "SHOW GRAPH",font= ("Arial",15,"bold"),fg= "red",bg= "black",bd= "5",command= root.showgraph_btn)
        self.showgraph.place(x = 400, y= 380)

    def showgraph_btn(self):
        
        df = pd.read_csv("atm3.csv")
        df.dropna(axis= 0,inplace= True)

        x = df["CREDIT"]
        z = df["AVL_BALANCE"]

        font1 = {"family" : "serif","color" : "darkred","size" : 15}

        plt.subplot(2,1,1)
        plt.scatter(x,z,c = "red",lw = 5)
        plt.title("Comapare Two Graphs",fontdict= font1)

        plt.xlabel("CREDIT",fontdict= font1)
        plt.ylabel("AVL_BALANCE",fontdict= font1)
        plt.grid(axis= "y",color = "black",ls = "--",lw = "0.8")

        df = pd.read_csv("atm3.csv")
        df.dropna(axis= 0,inplace= True)

        x = df["DEBIT"]
        z = df["AVL_BALANCE"]

        font1 = {"family" : "serif","color" : "darkred","size" : 15}

        plt.subplot(2,1,2)
        plt.scatter(x,z,c = "red",lw = 5)

        plt.xlabel("DEBIT",fontdict= font1)
        plt.ylabel("AVL_BALANCE",fontdict= font1)
        plt.grid(axis= "y",color = "black",ls = "--",lw = "0.8")

        plt.show()
                
     
    def exit_btn(self):
        win.destroy() 

if __name__ == '__main__':
    
    win = Tk()
    win.geometry("800x500")
    win.maxsize(800,500)
    win.minsize(800,500)
    win.title("ATM SYSTEM")
    root = Events(win)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()

    win.mainloop()