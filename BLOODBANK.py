try :
    import mysql.connector
    import tkinter as tk
    import tkinter.messagebox as box
    from tkinter import *
    import random
    import numpy as np
    from matplotlib import pyplot as plt

except:
    import mysql.connector
    import tkinter as tk
    import tkinter.messagebox as box
    from tkinter import *
    import random
    import numpy as np
    from matplotlib import pyplot as plt
    
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="user123",
  database="user"
)


#mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE DATABASE user")
#mycursor.execute("CREATE TABLE blood (id  INTEGER(255) AUTO_INCREMENT Primary key,full_name VARCHAR(255), pass_word VARCHAR(255), gender VARCHAR(255), age VARCHAR(255),mobile_number INTEGER(255),email_id VARCHAR(255),pincode VARCHAR(255),  blood_type VARCHAR(255),number_donations integer(250),volume integer(250))")
#mycursor.execute("Select*FROM blood")
#mycursor.execute("create table admin(admin_name varchar(255), admin_password varchar(255), otp int(5))")
#sql = "INSERT INTO admin (admin_name,admin_password)
#val = [
        #(fname, password, gen, age_, mob, e_id, pin,b_type,"0","0")
      #]
#mycursor.executemany(sql, val)
#mydb.commit()

#mycursor2.execute("create table otp (otp_ integer(5), serial integer(1) primary key)")
#mycursor2.execute("insert into otp values(0,1)")
#mydb.commit()

mycursor = mydb.cursor()
mycursor.execute("use user")
#mycursor.execute("select * from blood")

mycursor1 = mydb.cursor()
mycursor1.execute("use user")
#mycursor1.execute("select * from admin")

mycursor2 =mydb.cursor()
mycursor2.execute("use user")
#mycursor2.execute("select * from otp")

#main
def main():
    main = tk.Tk()
    main.geometry("1920x1020")  
    main.iconbitmap(r'logo.ico')
    
    f = tk.Canvas(bg="red", height =2190 ,width =1520)
    f.grid()
    
    pic_main_lo = tk.PhotoImage(file="blood_donorlo.PNG")
    pic_main = tk.Label(f,bg = 'red',bd = '3',image = pic_main_lo)
    pic_main.place(x=0,y = 0)
    
    main.title("WELCOME TO BLOOD DONOR")
    
    btn = tk.Button(f, text = 'LOGIN', command = login, fg = "White" ,bg="Black", width="15")
    btn.place(x=100,y=125)
    btn = tk.Button(f, text = 'ADMIN LOGIN', command = admins, fg = "White" ,bg="Black", width="15")
    btn.place(x=300,y=125)
    btn = tk.Button(f, text = 'SIGNUP', command = signup, fg = "White" ,bg="Black", width="15")
    btn.place(x=500,y=125)
    btn = tk.Button(f, text = 'ABOUT US', command = abtus, fg = "White" ,bg="Black", width="15")
    btn.place(x=700,y=125)
    btn = tk.Button(f, text = 'PRIVACY POLICIES', command = privpol, fg = "White" ,bg="Black", width="15")
    btn.place(x=900,y=125)
    btn = tk.Button(f, text = 'BLOOD TIPS', command =btips, fg = "White" ,bg="Black", width="15")
    btn.place(x=1100,y=125)
    
    bgg = tk.PhotoImage(file="bloodd.gif")
    bg = tk.Label(f,bg = 'red',bd = '3',image = bgg)
    bg.place(x=150,y = 150)
    
    main.mainloop()
    

def login():
    def dialog1():
        mycursor.execute("select * from blood")
        flag = 0
        global fname
        fname = e1.get()
        password = e2.get()
        e_id = e3.get()
        l = list(mycursor)
        #print (l)
        for x in l:
          if ((x[1] == fname) & (x[2] == password) & (x[6] == e_id)):
            flag = flag +1
        if (flag == 1):
            box.showinfo("info","You have been logged in")
            login.destroy()
            dashboard(fname)    
        else:
           box.showinfo("info","wrong try again")
   
    login = tk.Toplevel()
    login.title('WELCOME TO BLOOD DONOR Login page')
    login.geometry("1196x1080")
    login.iconbitmap(r'logo.ico')

    f = tk.Canvas(login,bg="red", height =2190 ,width =1200)
    f.grid()

    pic_main_sh = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label (f,  bg = 'red',bd = '3', image = pic_main_sh)
    labpic.place(x=0,y = 0)

    label = tk.Label(f, text= "Login",fg = "White",bg = "red",width=15,font=("Courier", 35))
    label.place(x=400,y = 130)
   
    label1 = tk.Label(f,text = 'Full name:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
    label1.place(x=300,y=200)
    e1 = tk.Entry(f)
    e1.place(x=620,y=213)

    label2=tk.Label(f,text='Password:',fg="white",bg = 'red',width=20,font=("Bold", 25))
    label2.place(x=300,y=270)
    e2 = tk.Entry(f,show="*",width=30)
    e2.place(x=620,y=283)

    label3 = tk.Label(f,text = "Email:" ,fg="white",bg = 'red',width=20,font=("Bold", 25))
    label3.place(x=300,y=340)              
    e3 = tk.Entry(f)
    e3.place(x=620,y=353)
   
    btn = tk.Button(f, text = 'Login',command = dialog1, fg = "White" ,bg="Black", width="15")
    btn.place(x=560,y=450)
    
    about =tk.Label(f,text = 'About us:' ,fg="white",bg = 'red',font=("Bold", 18))
    about1 =tk.Label(f,fg="white",bg = 'red',text = 'We help to donate blood in the most effective way through our portal and try our best to give the user a friendly and easy environment for blood donation procedures' , font=("Courier", 15),wraplength="1200")
    about.place (x=30,y=500)
    about1.place (x=30,y=550)
    about3 =tk.Label(f,text = 'You can contact us on: 9878956436(Moblie) or 080-2545674(land-line)' ,fg="white",bg = 'red',font=("Courier", 15))
    about3.place(x=30,y=600)
   
    login.mainloop()



def admins():
        
    def update():
        global a_name
        a_name = e1.get()
        otpp = random.randint(10000,99999)
        print (otpp)

        sql = """update otp
                 set otp_ = %s
                 where serial = '1'
              """
       
        val = [
              (otpp,)
            ]
        mycursor2.executemany(sql,val)
        mydb.commit()
        box.showinfo("info","OTP updated")  
       
    def action():
        flag = 0
        mycursor1.execute("select * from admin")
        a_name = e1.get()
        password = e2.get()
        otpp = e3.get()
        l = list(mycursor1)
        mycursor2.execute("select * from otp")
        l1 = list(mycursor2)
        for x in l:
            if ((x[0] == a_name) and (x[1] == password) and (str(l1[0][0]) == otpp)):
                flag = flag +1  
        if (flag == 1):
            sql = """update otp
                     set otp_ = %s
                     where serial ='1'
                  """
           
            val = [
                   (None,)    
                  ]                
            mycursor2.executemany(sql,val)
            mydb.commit()
            box.showinfo("info","You have been logged in")
            admin.destroy()
            admin_dashboard(a_name)
        else:
           box.showinfo("info","wrong try again")


    def admin_dashboard(a_name):       
        
        def search():
            uid = a.get()
            uid = int (uid)
            display=""
            mycursor.execute("select*from blood where id= %s",(uid,))
            query = mycursor.fetchone()
            if (query== None):              
                ans1 = tk.Label(f, text="Not Found",fg= 'white',bg="red",width = "20",font=("Courier", 20))
                ans1.place(x=830,y =350)

                ans2 = tk.Label(f, text="Not Found",fg= 'white',bg="red",width = "20",font=("Courier", 20))
                ans2.place(x=830,y =390)

                ans3 = tk.Label(f, text="Not Found",fg= 'white',bg="red",width = "20",font=("Courier", 20))
                ans3.place(x=830,y =430)
             
                
            else:
                ans1 = tk.Label(f, text=query[1],fg= 'white',bg="red",width = "20",font=("Courier", 20))
                ans1.place(x=830,y =350)

                ans2 = tk.Label(f, text=query[8],fg= 'white',bg="red",width = "20", font=("Courier", 20))
                ans2.place(x=830,y=390)

                ans3 = tk.Label(f, text=query[10],fg= 'white',bg="red",width = "20",font=("Courier", 20))
                ans3.place(x=830,y=430)

        def remove():
            uid = a.get()
            uid = int(uid)
            mycursor.execute("DELETE FROM blood WHERE id= %s",(uid,))
            mydb.commit()
            box.showinfo("info","User Deleted")
                             
        def update_volume():
            uid = int(a.get())
            num = int(b.get())
            mycursor.execute("update blood set volume = volume + %s where id= %s; ",(num,uid))
            mycursor.execute("update blood set number_donations = number_donations + '1' where id= %s; ",(uid,))
            mydb.commit()
            box.showinfo("info","Updated Volume")

            
        def new_admin():
            def add_admin():
                a_name=e1.get()
                a_pass=e2.get()
                sql = "INSERT INTO admin (admin_name,admin_password) VALUES (%s,%s)"
                val = [
                    (a_name,a_pass)
                  ]
                mycursor1.executemany(sql, val)
                mydb.commit()
                n_admin.destroy()
            


            n_admin = tk.Toplevel()
            n_admin.geometry('1920x1080')  
            n_admin.iconbitmap(r'logo.ico')
            n_admin.title("NEW ADMIN")
            f = tk.Canvas(n_admin,bg="red", height =2190 ,width =1520)
            f.grid()    

            pic_dash_lo = tk.PhotoImage(file="blood_donorlo.PNG")
            pic_dash = tk.Label(f,bg = 'black',bd = '3',image = pic_dash_lo)
            pic_dash.place(x=0,y = 0)

            label = tk.Label(f, text= "Add New Admin",fg = "White",bg = "red",width=15,font=("Courier", 35))
            label.place(x=400,y = 130)
               
            label1 = tk.Label(f,text = 'Admin Name:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
            label1.place(x=300,y=200)
            e1 = tk.Entry(f,width=30)
            e1.place(x=650,y=213)

            label2 = tk.Label(f,text = 'Admin Password:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
            label2.place(x=300,y=270)
            e2 = tk.Entry(f,show="*",width=30)
            e2.place(x=650,y=283)
               
            btn = tk.Button(f, text = 'ADD',command = add_admin, fg = "White" ,bg="Black", width="15")
            btn.place(x=560,y=350)

            n_admin.mainloop()

            
        def changepass():
            def change1():
                password1 = e1.get()
                password2 = e2.get()
               
                if password1==password2 :
                   
                    sql = """update admin
                            set admin_password= %s
                            where admin_name= %s"""
                    val = [ 
                        (password,a_name)
                      ]
                
                    mycursor.executemany(sql, val)
                    mydb.commit()
                    box.showinfo("info","Password successfully changed")
                    change.destroy()
                else:
                    box.showinfo("info","Passwords do not match!")
                
            change = tk.Toplevel()
            change.geometry('1920x1080')  
            change.iconbitmap(r'logo.ico')
            change.title("CHANGE PASSWORD")
            f = tk.Canvas(change,bg="red", height =2190 ,width =1520)
            f.grid()    

            pic_dash_lo = tk.PhotoImage(file="blood_donorlo.PNG")
            pic_dash = tk.Label(f,bg = 'black',bd = '3',image = pic_dash_lo)
            pic_dash.place(x=0,y = 0)

            label = tk.Label(f, text= "Change password",fg = "White",bg = "red",width=15,font=("Courier", 35))
            label.place(x=400,y = 130)
            
            label1 = tk.Label(f,text = 'New password:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
            label1.place(x=300,y=200)
            e1 = tk.Entry(f,show="*",width=30)
            e1.place(x=650,y=213)

            label2 = tk.Label(f,text = 'Re-enter password:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
            label2.place(x=300,y=270)
            e2 = tk.Entry(f,show="*",width=30)
            e2.place(x=650,y=283)
            
            btn = tk.Button(f, text = 'Change',command = change1, fg = "White" ,bg="Black", width="15")
            btn.place(x=560,y=350)
        
            
            change.mainloop()

        a_dashboard = tk.Toplevel()
        a_dashboard.geometry('1920x1080')  
        a_dashboard.iconbitmap(r'logo.ico')
        a_dashboard.title("DASHBOARD")
        f = tk.Canvas(a_dashboard,bg="red", height =2190 ,width =1520)
        f.grid()    

        pic_dash_lo = tk.PhotoImage(file="blood_donorlo.PNG")
        pic_dash = tk.Label(f,bg = 'black',bd = '3',image = pic_dash_lo)
        pic_dash.place(x=0,y = 0)
   
        label1 = tk.Label(f,relief="solid",bg = "red",width=187,height=5)
        label1.place(x=200,y = 120)

        label2 = tk.Label(f, text= "Welcome Admin " + ";",fg = "White",bg = "red",width=27,font=("Courier", 16))
        label2.place(x=190,y = 150)
       
        label3 = tk.Label(f, text= "Admin Dashboard",fg = "White",bg = "red",width=37,font=("Bold", 28))
        label3.place(x=440,y = 140)        

        label4 = tk.Label(f,relief="solid",bg = "red",width=37,height=47)
        label4.place(x=0,y = 120)

        label = tk.Label(f,text = "Enter user id:" ,fg="white",bg = 'red',width=20,font=("Bold", 20))
        label.place(x=550,y=240)              
        a= tk.Entry(f)
        a.place(x=800,y=250)
        uid = a.get()
        
        label5 = tk.Label(f, text="Full Name :",fg= 'white',bg="red", width=23,font=("Courier", 20))
        label5.place(x=500,y=350)

        label6 = tk.Label(f, text="Blood Type:",fg= 'white',bg="red", width=23,font=("Courier", 20))
        label6.place(x=500,y=390)
        
        label7 = tk.Label(f, text="    Volume:",fg= 'white',bg="red", width=23,font=("Courier", 20))
        label7.place(x=500,y=430)
        

        btn1 = tk.Button(f, text = 'Search ID',fg = "black" ,activebackground="blue",bg="white", width=23,font=("Courier", 13),command=search)
        btn1.place(x=660,y=300)

        label8 = tk.Label(f, text="Add Volume:",fg = "white" ,activebackground="blue",bg="red", width=23,font=("bold", 20))
        label8.place(x=490,y=570)

        b= tk.Entry(f,width = 23)
        b.place(x=850,y=580)   
           
        btn2 = tk.Button(f, text = 'Update Volume',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=update_volume)
        btn2.place(x=670,y=650)
        
        btn3 = tk.Button(f, text = 'Remove user',fg = "black" ,bg="white", width=19,font=("Courier", 11),command=remove)
        btn3.place(x=1100,y=240)
         
        
        btn4 = tk.Button(f, text = 'Sign out',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=a_dashboard.destroy)
        btn4.place(x=10 ,y=300)
        
        btn5 = tk.Button(f, text = 'Change password',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=changepass)
        btn5.place(x=10 ,y=400)
        
        btn6 = tk.Button(f, text = 'Register new admin',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=new_admin)
        btn6.place(x=10,y=500)
        
        a_dashboard.mainloop()

        

    admin = tk.Toplevel()
    admin.title('WELCOME TO BLOOD DONOR Admin Login page')
    admin.geometry("1196x1080")
    admin.iconbitmap(r'logo.ico')

    f = tk.Canvas(admin,bg="red", height =2190 ,width =1200)
    f.grid()

    pic_main_sh = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label (f,  bg = 'red',bd = '3', image = pic_main_sh)
    labpic.place(x=0,y = 0)

    label = tk.Label(f, text= "Admin Login",fg = "White",bg = "red",width=15,font=("Courier", 35))
    label.place(x=400,y = 130)
           
    label1 = tk.Label(f,text = 'Admin Name:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
    label1.place(x=300,y=200)
    e1 = tk.Entry(f)
    e1.place(x=620,y=213)
    label2 =tk.Label(f,text = 'Password:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
    label2.place(x=300,y=270)
    e2 = tk.Entry(f,show="*",width=30)
    e2.place(x=620,y=283)

    label3 = tk.Label(f,text = "Enter OTP:" ,fg="white",bg = 'red',width=20,font=("Bold", 25))
    label3.place(x=300,y=340)              
    e3 = tk.Entry(f)
    e3.place(x=620,y=353)
         
    btn = tk.Button(f, text = 'Login',command = action, fg = "White" ,bg="Black", width="15")
    btn.place(x=500,y=450)
    btn = tk.Button(f, text = 'Update OTP',command = update, fg = "White" ,bg="Black", width="15")
    btn.place(x=660,y=450)
    
    admin.mainloop()  
    
    
def signup():

    def dialog2():
        global b_type
        mycursor.execute("select * from blood")
        global fname
        fname = e1.get()
        mob=e6.get()
        password= e2.get()
        flag = 0
        l = list(mycursor)
        
        for x in l:
          if ( (x[1] == fname) and (x[2] == password)):
            flag = 1
            
          if ( (x[1] != fname or fname=="")and len (password)>4 ):
              flag = 2
              
          if ((len(fname)<4) or (len(password)<=2)):
              flag = -1
        
          if ((len(str(mob))!=10)):
              flag = 5  
              
          if (click.get() == 0 ):
              flag = 3
              
        if (flag==0):
           box.showinfo ("info","Please enter all the details")
            
        elif (flag == 1):
            box.showinfo("info","Sorry this User name and Password is taken")
            
        elif (flag == -1):
            box.showinfo("info","The length of user name must be minimum of 5 characters and the length of the password must be greater than 2 character")

        elif(flag == 3):
            box.showinfo("info","Please accept the terms and condition")

        elif(flag == 5):
            box.showinfo("info","Please enter a 10 digit mobile number")
            
        elif (flag == 2):
           
            if var.get()==1:
                gen = "M"
            else:
                gen="F"
                
            b_type =d.get()
            e_id = e5.get()
            age=e7.get()
            mob=e6.get()
            
            pin=e9.get()
            box.showinfo("info","You have been registered")
            
            sql = "INSERT INTO blood (full_name, pass_word, gender, age,mobile_number ,email_id , pincode,  blood_type, number_donations,volume) VALUES (%s, %s,%s, %s, %s,%s,%s,%s,%s, %s)"
            val = [ 
                    (fname,password,gen,age,mob,e_id,pin,b_type,"0","0")
                  ]
            
            mycursor.executemany(sql, val)
            mydb.commit()
            top.destroy()
            dashboard(fname)            
       
        
    top = tk.Toplevel()
    top.geometry('1196x1080')
    top.iconbitmap(r'logo.ico')
    top.title('WELCOME TO BLOOD DONOR Sign up page')
    
    f=tk.Canvas(top,bg="red",height =2190 ,width =1520)
    f.grid()
        
    pic_main_sh = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label(f,bg = 'red',bd = '3',image = pic_main_sh)
    labpic.place(x=0,y = 0)
    pic_yes = tk.PhotoImage(file="yes.PNG")
    yes = tk.Label(f,bg = 'red',image = pic_yes)
    yes.place(x=800,y = 120)

    label = tk.Label(f, text="Become a Blood Donor",fg = "White",bg = "red",width=35,font=("Courier", 34))
    label.place(x=100,y = 130)


    label1 = tk.Label(f, text="Full Name",width=25,font=("bold", 12))
    label1.place(x=300,y = 230)

    e1 = tk.Entry(f,width = 30)
    e1.place(x=600,y = 230)

    label2 = tk.Label(f, text="Password",width=20,font=("bold", 12))
    label2.place(x=300,y=270)

    e2= tk.Entry(f,width = 30)
    e2.place(x=600,y = 270)

    label3 = tk.Label(f,text="Gender",width=20,font=("bold", 12))
    label3.place(x=300,y = 310)
    var = IntVar()
    r = tk.Radiobutton(f, text="Male",font=("bold", 12),variable=var, value=1)
    r.place(x=600,y = 310)
    r1=Radiobutton(f, text="Female",font=("bold", 12),variable=var, value=2)
    r1.place(x=700,y = 310)

    label4 = tk.Label(f, text="Blood Type",width=20,font=("bold", 12))
    label4.place(x=300,y = 350)


    list1 = ['A+','A-','B+','B-','AB+','AB-','O+','O-']
    d = StringVar()
    droplist = OptionMenu(f,d, *list1)
    droplist.config(width=20)
    d.set('Select your Blood Type')
    droplist.place(x=600,y = 350)
    
    label5 = tk.Label(f,text="Email id ",width=20,font=("bold", 12))
    label5.place(x=300,y = 390)
    e5 = tk.Entry(f,width = 30)
    e5.place(x=600,y = 390)

    label6 = tk.Label(f,text="Mobile Number",width=20,font=("bold", 12))
    label6.place(x=300,y = 430)
    e6 =tk.Entry(f,width = 30)
    e6.place(x=600,y = 430)

    label7 = tk.Label(f,text="Age",width=20,font=("bold", 12))
    label7.place(x=300,y = 470)
    e7= tk.Entry(f,width = 30)
    e7.place(x=600,y = 470)

    label8 = tk.Label(f,text="City",width=20,font=("bold", 12))
    label8.place(x=300,y = 510)
    labelb = tk.Label(f,text="Bangalore",width=20,font=("bold", 12))
    labelb.place(x=600,y = 510)

    label9 = tk.Label(f,text="Pin code",width=20,font=("bold", 12))
    label9.place(x=300,y = 550)
    e9 = tk.Entry(f,width = 30)
    e9.place(x=600,y = 550)

    click = IntVar()
    c = tk.Checkbutton(f, text = "I Agree to all the terms and conditions", variable = click, \
                 offvalue = 0,onvalue = 1,activebackground= "white",
                 bg='red', width = 30,font=("bold", 12))
    
    c.place(x=480,y = 580)
    Button(f, text='Submit',command = dialog2 , width=20,bg='Black',fg='white').place(x=500,y = 620)

   
    
    
    top.mainloop()



def abtus():
    topa=tk.Toplevel()
    topa.geometry('1196x1080')
    topa.iconbitmap(r'logo.ico')
    topa.config(bg='red')
    topa.title('WELCOME TO BLOOD DONOR About us page')

    pic = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label(topa,bg = 'red',image = pic)
    labpic.place(x=0,y = 0)
    
    head=tk.Label(text="ABOUT US:",font=("Helvetica",25))
    display="Universally, 'Blood' is recognized as the most precious element that sustains life.\n It saves innumerable lives across the world in a variety of conditions. Once in every 2- seconds, someone, somewhere is desperately in need of blood.\n More than 29 million units of blood components are transfused every year. The need for blood is great - on any given day, approximately 39,000 units of Red Blood Cells are needed. \n Each year, we could meet only up to 1% (approx) of our nation’s demand for blood transfusion.Despite the increase in the number of donors, blood remains in short supply during emergencies, mainly attributed to the lack of information and accessibility. \n We positively believe this tool can overcome most of these challenges by effectively connecting the blood donors with the blood recipients."
    

    about =tk.Label(topa,text = 'ABOUT US:' ,fg="black",bg = 'red',font=("Helvetica", 25,"bold"))
    about1 =tk.Label(topa,fg="black",bg = 'red',text = display , font=("Courier", 18),wraplength="1200")
    about.place (x=450,y=150)
    about1.place (x=10,y=200)
    about3 =tk.Label(topa,text = 'You can contact us on: 9878956436(Moblie) or 080-2545674(land-line)' ,fg="black",bg = 'red',font=("Courier", 15))
    about3.place(x=10,y=600)

    topa.mainloop()



def btips():
    topa=tk.Toplevel()
    topa.geometry('1196x1080')
    topa.iconbitmap(r'logo.ico')
    topa.config(bg='red')
    topa.title('WELCOME TO BLOOD DONOR Blood tips')

    pic = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label(topa,bg = 'red',image = pic)
    labpic.place(x=0,y = 0)
    
    head=tk.Label(text="BLOOD TIPS",font=("Helvetica",25))
    display="""
Q)Who can give blood?
*Overall health- The donor must be fit and healthy, and should not be suffering from transmittable diseases.
*Age and weight- The donor must be 18–65 years old and should weigh a minimum of 50 kg.
*Pulse rate- Between 50 and 100 without irregularities.
*Hemoglobin level- A minimum of 12.5 g/dL.
*Blood pressure- Diastolic: 50–100 mm Hg, Systolic: 100–180 mm Hg.
*The time period between successive blood donations should be more than 3 months.

Q)How much blood is drawn? Is it safe for my body to lose that much blood?
450 ml. The average person has 4.7 to 5.5 liters, so the small loss is easily afforded. The fluid (plasma) is replaced within 24 hours. The red cells take about five weeks. You can donate again in eight weeks!

Q)Is donating blood safe?
Absolutely. Blood donation conditions are sanitary, and needles are sterile and disposable.


"""
    

    blo =tk.Label(topa,text = 'BLOOD TIPS' ,fg="black",bg = 'red',font=("Helvetica", 25,"bold"))
    blo1 =tk.Label(topa,fg="black",bg = 'red',text = display , font=("Courier", 16),wraplength="1200")
    blo.place (x=450,y=150)
    blo1.place (x=10,y=200)
    blo3 =tk.Label(topa,text = 'You can contact us on: 9878956436(Moblie) or 080-2545674(land-line)' ,fg="black",bg = 'red',font=("Courier", 15))
    blo3.place(x=10,y=600)

    topa.mainloop()




def privpol():
    topa=tk.Toplevel()
    topa.geometry('1196x1080')
    topa.iconbitmap(r'logo.ico')
    topa.config(bg='red')
    
    pic = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label(topa,bg = 'red',image = pic)
    labpic.place(x=0,y = 0)

    topa.title('WELCOME TO BLOOD DONOR Privacy policies page')
    head=tk.Label(text="ABOUT US:",font=("Helvetica",25))
    
    display="When you visit certain areas of this blood bank including the registration form, you may be asked to provide personal information (such as name, address, e-mail address, and phone number) that we need to process your request. In the event that you decline to provide such information, we will be unable to process your request.This privacy policy extends to this blood bank only.If you have any questions or concerns about the online policy for this site or its implementation you may contact us using the details posted on the ‘contact us’ page on our website. \n Terms of use \n This is purely a non-profit directed towards the welfare of our community. Any individual or entity that enrolls for our service does so with his/her own will and at no obligation to any one else or any other entity. We seriously condemn the use of this project for any commercial purpose, including solicitation for commercial gain based on the contact details posted by the registered users. We take the privacy of our users very seriously and therefore reserve the right to pursue a legal action against the individuals or entities violating our terms of use. The formal complaints procedure should only be used where the complainant feels that the nature of the complaint is too serious to be dealt with informally, or where a satisfactory conclusion has not been reached after following the informal procedure. A formal complaint should be made in writing to BloodBank team, who will acknowledge receipt and ensure that the matter is looked into at the earliest possible."
    

    about =tk.Label(topa,text = 'PRIVACY POLICIES' ,fg="black",bg = 'red',font=("Helvetica", 25,"bold"))
    about1 =tk.Label(topa,fg="black",bg = 'red',text = display , font=("Courier", 12),wraplength="1200")
    about.place (x=450,y=150)
    about1.place (x=10,y=200)
    about3 =tk.Label(topa,text = 'You can contact us on: 9878956436(Moblie) or 080-2545674(land-line)' ,fg="black",bg = 'red',font=("Courier", 15))
    about3.place(x=10,y=500)

    

    
    topa.mainloop()

    
def dashboard(fname):
    def graph1():
        #PIE CHART
        
        mycursor = mydb.cursor()
        mycursor.execute('select count(id) as "O+ donors" from blood where blood_type="O+"');
        op = mycursor.fetchall()
        mycursor.execute('select count(id) as "O- donors" from blood where blood_type="O-"')
        on = mycursor.fetchall()
        mycursor.execute('select count(id) as "A+ donors" from blood where blood_type="A+"')
        ap = mycursor.fetchall()
        mycursor.execute('select count(id) as "A- donors" from blood where blood_type="A-"')
        an = mycursor.fetchall()
        mycursor.execute('select count(id) as "AB+ donors" from blood where blood_type="AB+"')
        abp = mycursor.fetchall()
        mycursor.execute('select count(id) as "AB- donors" from blood where blood_type="AB-"')
        abn = mycursor.fetchall()
        mycursor.execute('select count(id) as "B+ donors" from blood where blood_type="B+"')
        bp = mycursor.fetchall()
        mycursor.execute('select count(id) as "B- donors" from blood where blood_type="B-"')
        bn = mycursor.fetchall()

        plt.title("Availability of blood types")

        col=["pink","blue","magenta","green","cyan","purple","HotPink","red"]
        l=[op[0][0],on[0][0],ap[0][0],an[0][0],bp[0][0],bn[0][0],abp[0][0],abn[0][0]]
        h=["O+","O-","A+","A-","B+","B-","AB+","AB-"]

        plt.pie(l,labels=h,colors=col,autopct="%1.1F%%",shadow=True)
        plt.axis('equal')  
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')

        plt.show()
        #END OF PIE CHART

        
    def graph2():
        
        mycursor = mydb.cursor()
        mycursor.execute('select sum(volume) as "O+ donors" from blood where blood_type="O+"');
        opp = mycursor.fetchall()
        op=opp[0][0]
        mycursor.execute('select sum(volume) as "O- donors" from blood where blood_type="O-"')
        onn = mycursor.fetchall()
        on=onn[0][0]
        mycursor.execute('select sum(volume) as "A+ donors" from blood where blood_type="A+"')
        app = mycursor.fetchall()
        ap=app[0][0]
        mycursor.execute('select sum(volume) as "A- donors" from blood where blood_type="A-"')
        ann = mycursor.fetchall()
        an=ann[0][0]
        mycursor.execute('select sum(volume) as "AB+ donors" from blood where blood_type="AB+"')
        abpp = mycursor.fetchall()
        abp=abpp[0][0]
        mycursor.execute('select sum(volume) as "AB- donors" from blood where blood_type="AB-"')
        abnn = mycursor.fetchall()
        abn=abnn[0][0]
        mycursor.execute('select sum(volume) as "B+ donors" from blood where blood_type="B+"')
        bpp = mycursor.fetchall()
        bp=bpp[0][0]
        mycursor.execute('select sum(volume) as "B- donors" from blood where blood_type="B-"')
        bnn = mycursor.fetchall()
        bn=bnn[0][0]
        #print(op,on,ap,an,bp,bn,abp,abn)
        #print(opp,onn,app,ann,bpp,bnn,abpp,abnn)

        #values
        o_posv=[op,on]
        o_negv=[on]
        a_posv=[op,on,ap,an]
        a_negv=[on,an]
        ab_posv=[ap,bp,op,on,an,bn,abp,abn]
        ab_negv=[on,an,bn,abn]
        b_posv=[bp,op,on,bn]
        b_negv=[on,bn]
        

        
        #labels
        o_pos=["O+","O-"]
        o_neg=["O-"]
        a_pos=["O+","O-","A+","A-"]
        a_neg=["O-","A-"]
        ab_pos=["A+","B+","O+","O-","A-","B-","AB+","AB-"]
        ab_neg=["O-","A-","B-","AB-"]
        b_pos=["B+","O+","O-","B-"]
        b_neg=["O-","B-"]


        def apos():
            x=np.arange(4)
            plt.xticks(x,a_pos)
            plt.title("Available donors for A+")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,a_posv,color="red",edgecolor='black',width=.35)
            for i in range(len(a_posv)):
                if a_posv[i]==max(a_posv):
                    mv=a_pos[i]
            maxx="Preferred blood type for your requirement: "+mv
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        
        def opos():
            x=np.arange(2)
            plt.xticks(x,o_pos)
            plt.title("Available donors for O+")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,o_posv,color="red",edgecolor='black',width=.35)
            for i in range(len(o_posv)):
                if o_posv[i]==max(o_posv):
                    mv=o_pos[i]
            maxx="Preferred blood type for your requirement: "+mv
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        
            
        def bpos():
            x=np.arange(4)
            plt.xticks(x,b_pos)
            plt.title("Available donors for B+")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,b_posv,color="red",edgecolor='black',width=.35)
            for i in range(len(b_posv)):
                if b_posv[i]==max(b_posv):
                    mv=b_pos[i]
            maxx="Preferred blood type for your requirement: "+mv
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        

        def abpos():
            x=np.arange(8)
            plt.xticks(x,ab_pos)
            plt.title("Available donors for AB+")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,ab_posv,color="red",edgecolor='black',width=.35)
            for i in range(len(ab_posv)):
                if ab_posv[i]==max(ab_posv):
                    mv=ab_pos[i]
            maxx="Preferred blood type for your requirement: "+str(max(ab_posv))
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        

        def aneg():
            x=np.arange(2)
            plt.xticks(x,a_neg)
            plt.title("Available donors for A-")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,a_negv,color="red",edgecolor='black',width=.35)
            for i in range(len(a_negv)):
                if a_negv[i]==max(a_negv):
                    mv=a_neg[i]
            maxx="Preferred blood type for your requirement: " +mv
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        

        def oneg():
            x=np.arange(1)
            plt.xticks(x,o_neg)
            plt.title("Available donors for O-")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,o_negv,color="red",edgecolor='black',width=.35)
            for i in range(len(o_negv)):
                if o_negv[i]==max(o_negv):
                    mv=o_neg[i]
            maxx="Preferred blood type for your requirement: "+mv
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        

        def bneg():
            x=np.arange(2)
            plt.xticks(x,b_neg)
            plt.title("Available donors for B-")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,b_negv,color="red",edgecolor='black',width=.35)
            for i in range(len(b_negv)):
                if b_negv[i]==max(b_negv):
                    mv=b_neg[i]
            maxx="Preferred blood type for your requirement: "+mv
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        
            
        def abneg():
            x=np.arange(4)
            plt.xticks(x,ab_neg)
            plt.title("Available donors for AB-")
            plt.xlabel("Blood types")
            plt.ylabel("Blood available")
            plt.bar(x,ab_negv,color="red",edgecolor='black',width=.35)
            for i in range(len(ab_negv)):
                if ab_negv[i]==max(ab_negv):
                    mv=ab_neg[i]
            maxx="Preferred blood type for your requirement: "+mv
            maximum =tk.Label(f,fg="white",bg = 'red',text = maxx , font=("Courier", 20),wraplength="1200")
            maximum.place (x=350,y=600)
            print(maxx)
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.show()
        
    
            
        mycursor.execute("select blood_type from blood where full_name= %s",(fname,))
        l=mycursor.fetchone()

        bb=str(l[0])
        #print(bb)
        if (bb=="A+"):
            apos()
        if (bb=="A-"):
            aneg()
        if (bb=="O+"):
            opos()
        if (bb=="O-"):
            oneg()
        if (bb=="B+"):
            bpos()
        if (bb=="B-"):
            bneg()
        if (bb=="AB-"):
            abneg()
        if (bb=="AB+"):
            abpos()

    def mapp():
        mapp = tk.Toplevel()
        mapp.geometry('1920x1080')  
        mapp.iconbitmap(r'logo.ico')
        mapp.title('MAPS')
        ma=tk.Canvas(mapp,bg="red", height = 2190 ,width =1540)
        ma.grid()
        
        pic_dash_lo = tk.PhotoImage(file="blood_donorlo.PNG")
        pic_dash = tk.Label(ma,bg = 'black',bd = '3',image = pic_dash_lo)
        pic_dash.place(x=0,y = 0)
            
        location = tk.PhotoImage(file="maps.PNG")
        locations = tk.Label(ma,bg = 'red',bd = '3',image = location)
        locations.place(x=130,y = 120)
        mapp.mainloop()
        
        
        

    def changepass():
        def change1():
     
            password1 = e1.get()
            password2 = e2.get()
           
            if password1==password2 :
               
                sql = """update blood
                        set pass_word= %s
                        where full_name= %s"""
                val = [ 
                    (password1,fname)
                  ]
            
                mycursor.executemany(sql, val)
                mydb.commit()
                box.showinfo("info","Password successfully changed")
                change.destroy()
            else:
                box.showinfo("info","Passwords do not match!")
            
        change = tk.Toplevel()
        change.geometry('1920x1080')  
        change.iconbitmap(r'logo.ico')
        change.title("CHANGE PASSWORD")
        f = tk.Canvas(change,bg="red", height =2190 ,width =1520)
        f.grid()    

        pic_dash_lo = tk.PhotoImage(file="blood_donorlo.PNG")
        pic_dash = tk.Label(f,bg = 'black',bd = '3',image = pic_dash_lo)
        pic_dash.place(x=0,y = 0)



        label = tk.Label(f, text= "Change password",fg = "White",bg = "red",width=15,font=("Courier", 35))
        label.place(x=400,y = 130)
        
        label1 = tk.Label(f,text = 'New password:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
        label1.place(x=300,y=200)
        e1 = tk.Entry(f,show="*",width=30)
        e1.place(x=650,y=213)

        label2 = tk.Label(f,text = 'Re-enter password:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
        label2.place(x=300,y=270)
        e2 = tk.Entry(f,show="*",width=30)
        e2.place(x=650,y=283)
        
        btn = tk.Button(f, text = 'Change',command = change1, fg = "White" ,bg="Black", width="15")
        btn.place(x=560,y=350)
    
        
        change.mainloop()

    dashboard = tk.Toplevel()
    dashboard.geometry('1920x1080')  
    dashboard.iconbitmap(r'logo.ico')
    dashboard.title("DASHBOARD")
    f = tk.Canvas(dashboard,bg="red", height =2190 ,width =1520)
    f.grid()    

    pic_dash_lo = tk.PhotoImage(file="blood_donorlo.PNG")
    pic_dash = tk.Label(f,bg = 'black',bd = '3',image = pic_dash_lo)
    pic_dash.place(x=0,y = 0)

    label1 = tk.Label(f,relief="solid",bg = "red",width=187,height=5)
    label1.place(x=200,y = 120)

    label2 = tk.Label(f, text= "Welcome "+fname+";",fg = "White",bg = "red",font=("Courier", 20))
    label2.place(x=270,y = 220)
    
    label3 = tk.Label(f, text= "DASHBOARD",fg = "White",bg = "red",width=37,font=("Bold", 28))
    label3.place(x=440,y = 140)

    label4 = tk.Label(f,relief="solid",bg = "red",width=37,height=47)
    label4.place(x=0,y = 120)

    btn1 = tk.Button(f, text = 'BLOOD AVAILABLE IN BANK',fg = "black" ,bg="white",width=23,font=("Courier", 13),command=graph1)
    btn1.place(x=10,y=250)

    btn2 = tk.Button(f, text = 'POSSIBLE DONORS FOR YOU',fg = "black" ,bg="white",width=23,font=("Courier", 13),command=graph2)
    btn2.place(x=10,y=300)

    btn3 = tk.Button(f, text = 'CHANGE PASSWORD',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=changepass)
    btn3.place(x=10,y=350)

    btn4 = tk.Button(f, text = 'PRIVACY POLICIES',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=privpol)
    btn4.place(x=10,y=400)

    btn5 = tk.Button(f, text = 'ABOUT US',fg = "black" ,activebackground="blue",bg="white", width=23,font=("Courier", 13),command=abtus)
    btn5.place(x=10,y=450)

    btn6 = tk.Button(f, text = 'SIGN OUT',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=dashboard.destroy)
    btn6.place(x=10,y=600)

    btn7 = tk.Button(f, text = 'LOCATIONS TO DONATE',fg = "black" ,bg="white", width=23,font=("Courier", 13),command=mapp)
    btn7.place(x=1000,y=500)

    namee="Name:"
    namee1=fname
    name = tk.Label(f,text=namee,fg = "white",bg = "red",font=("Courier", 20))
    name.place(x=450,y = 300)
    name1 = tk.Label(f,text=namee1,fg = "white",bg = "red",font=("Courier", 20))
    name1.place(x=750,y = 300)

    gend=""
    mycursor.execute("select gender from blood where full_name= %s",(fname,))
    gender=mycursor.fetchone()
    if gender[0][0]=="F":
        gend="Female"
    if gender[0][0]=="M":
        gend="Male"   
    genderr="Gender:"
    genderr1=gend
    gen = tk.Label(f,text=genderr,fg = "white",bg = "red",font=("Courier", 20))
    gen.place(x=450,y = 350)
    gen1 = tk.Label(f,text=genderr1,fg = "white",bg = "red",font=("Courier", 20))
    gen1.place(x=750,y = 350)

    mycursor.execute("select blood_type from blood where full_name= %s",(fname,))
    b_type=mycursor.fetchone()
    bloodtype="Blood Type:"
    bloodtype1=b_type[0]
    blood = tk.Label(f,text=bloodtype,fg = "white",bg = "red",font=("Courier", 20))
    blood.place(x=450,y = 400)
    blood1 = tk.Label(f,text=bloodtype1,fg = "white",bg = "red",font=("Courier", 20))
    blood1.place(x=750,y = 400)

    mycursor.execute("select number_donations from blood where full_name= %s",(fname,))
    no=mycursor.fetchone()
    no_don="No. of donations:"
    no_don1=str(no[0])
    donations = tk.Label(f,text=no_don,fg = "white",bg = "red",font=("Courier", 20))
    donations.place(x=450,y = 450)
    donations1 = tk.Label(f,text=no_don1,fg = "white",bg = "red",font=("Courier", 20))
    donations1.place(x=750,y = 450)


    mycursor.execute("select volume from blood where full_name= %s",(fname,))
    volu=mycursor.fetchone()
    vol="Volume donated:"
    vol1=str(volu[0])
    volume = tk.Label(f,text=vol,fg = "white",bg = "red",font=("Courier", 20))
    volume.place(x=450,y = 500)
    volume1 = tk.Label(f,text=vol1,fg = "white",bg = "red",font=("Courier", 20))
    volume1.place(x=750,y = 500)

 
    dashboard.mainloop()


    
main()           
