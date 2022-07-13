import tkinter as tk
root = tk.Tk("SMS",'SMS',"TK",1,0,None)
m = 0 ;
columns = ['RollNo','Name','Date of Birth','Address','Contact No','Email Id','Sem-I Percent','Sem-II Percent'];
#function add
def add():
    global window,rollno,rollno,name,email,address,semIper,semIIper,dob,contact;
    window = tk.Tk("SMS",'SMS',"TK",1,0,None)
    window.minsize(600,500);
    window.title("Registration Form")
    window.configure(bg="azure")
    lblrollno = tk.Label(window,text="Roll No ",font=('Vardana',12))
    lblrollno.configure(bg='azure',fg='black')
    lblrollno.place(x='100',y='60');
    rollno = tk.Entry(window)
    rollno.place(x='220',y='65')
    lblname = tk.Label(window,text="Name ",font=('Vardana',12))
    lblname.configure(bg='azure',fg='black')
    lblname.place(x='100',y='90');
    name = tk.Entry(window)
    name.place(x='220',y='95')
    lbldob = tk.Label(window,text="Date of Birth ",font=('Vardana',12))
    lbldob.configure(bg='azure',fg='black')
    lbldob.place(x='100',y='120');
    dob = tk.Entry(window)
    dob.place(x='220',y='125')
    lbladdress = tk.Label(window,text="Address ",font=('Vardana',12))
    lbladdress.configure(bg='azure',fg='black')
    lbladdress.place(x='100',y='150');
    address = tk.Entry(window)
    address.place(x='220',y='155')
    lblemail = tk.Label(window,text="Email ",font=('Vardana',12))
    lblemail.configure(bg='azure',fg='black')
    lblemail.place(x='100',y='180');
    email = tk.Entry(window)
    email.place(x='220',y='185')
    lblcontact = tk.Label(window,text="Contact No ",font=('Vardana',12))
    lblcontact.configure(bg='azure',fg='black')
    lblcontact.place(x='100',y='210');
    contact = tk.Entry(window)
    contact.place(x='220',y='215')
    lblsemIper = tk.Label(window,text="Sem-I percent ",font=('Vardana',12))
    lblsemIper.configure(bg='azure',fg='black')
    lblsemIper.place(x='100',y='240');
    semIper = tk.Entry(window)
    semIper.place(x='220',y='245')
    lblsemIIper = tk.Label(window,text="Sem-II percent ",font=('Vardana',12))
    lblsemIIper.configure(bg='azure',fg='black')
    lblsemIIper.place(x='100',y='270');
    semIIper = tk.Entry(window)
    semIIper.place(x='220',y='275')
    btnSave = tk.Button(window,text='Save',command=save)
    btnSave.configure(bg='steelblue',fg='white')
    btnSave.place(x='180',y='295')
    window.mainloop()
#end add
#function save
def save():
    if m==1:        
        file = open("FY_Data.txt",'a')
    if m==2:
        file = open("SY_Data.txt",'a')
    if m==3:
        file = open("TY_Data.txt",'a')
    file.write("\n"+columns[0]+" : "+rollno.get())
    file.write("\n"+columns[1]+" : "+name.get())
    file.write("\n"+columns[2]+" : "+dob.get())
    file.write("\n"+columns[3]+" : "+address.get())
    file.write("\n"+columns[4]+" : "+contact.get())
    file.write("\n"+columns[5]+" : "+email.get())
    file.write("\n"+columns[6]+" : "+semIper.get())
    file.write("\n"+columns[7]+" : "+semIIper.get())
    file.write("\n--------------------------------\n")
    print("Student added successfully")
    file.close()
    window.destroy()
#end save
def view():
    m = var.get()
    if m==1:        
        file = open("FY_Data.txt",'r')
    if m==2:
        file = open("SY_Data.txt",'r')
    if m==3:
        file = open("TY_Data.txt",'r')
    print(file.read());
def search():
    line = 0
    if m==1:        
        file = open("FY_Data.txt")
    if m==2:
        file = open("SY_Data.txt")
    if m==3:
        file = open("TY_Data.txt")
    rno =str("RollNo : "+input("Enter Roll No : "))
    flag = 0
    for i in file:
        line += 1
        if rno in i:
            flag = 1
            count = line;
            break;
    if flag==1:
        print("\nStudent Details : ")
        while count<(line+8):
            print(file.readline())
            count +=1
        file.close()
        FY()
    else:
        file.close()
        print("Student is not present.")
        FY()
    #function NextPage
def NextPage():
    global m
    m = var.get()
    lblHead.pack_forget()
    lblMsg.destroy()
    btnNext.destroy()
    l = tk.Label(root,text="                                                 ");
    l.configure(bg='azure')
    l.place(x='300',y='120')
    l1 = tk.Label(root,text="                                                 ");
    l1.configure(bg='azure')
    l1.place(x='300',y='140')
    l2 = tk.Label(root,text="                                                 ");
    l2.configure(bg='azure')
    l2.place(x='300',y='160')
    l3 = tk.Label(root,text="                                                 ");
    l3.configure(bg='azure')
    l3.place(x='300',y='180')
    lblLogin.place(x='20',y='40')
    lblUser.place(x='60',y='90')
    txtUser.place(x='165',y='95')
    lblPass.place(x='60',y='120')
    txtPass.place(x='165',y='125')
    btnLogin.place(x='125',y='160')
#end NextPage
#function FY
def FY():
    if unm=="FYadmin" and passwd=="0018FY":
        print("\nLogin Successful......")
        print("\nFirst Year Students Account : ")
        print("\n Which operation you want to perform : \n 1.Add Student\n 2.View Students\n 3.Search Student\n 4.Exit")
        ch = int(input("Enter your choice : "));
        while ch!=4:
            if ch==1:
                add()
            elif ch==2:
                view()
            elif ch==3:
                search()
            elif ch==4:
                break;
            else:
                print("Wrong choice")
            ch = int(input("\nEnter your choice : "));
    else:
        print("\nYou are not a valid user...System can't give you permission to access the account....")
#end FY          
#function SY
def SY():
    if unm=="SYadmin" and passwd=="0018SY":
        print("\nLogin Successful......")
        print("\nSecond Year Students Account : ")
        print("\n Which operation you want to perform : \n 1.Add Student\n 2.View Students\n 3.Search Student\n 4.Exit")
        ch = int(input("Enter your choice : "));
        while ch!=4:
            if ch==1:
                add()
            elif ch==2:
                view()
            elif ch==3:
                search()
            elif ch==4:
                break;
            else:
                print("Wrong choice")
            ch = int(input("Which operation do you want to perform : "));
    else:
        print("\nYou are not a valid user...System can't give you permission to access the account....")
#end SY    
#function TY
def TY():
    if unm=="TYadmin" and passwd=="0018TY":
        print("\nLogin Successful......")
        print("\nThird Year Students Account : ")
        print("\nWhich operation do you want to perform : \n 1.Add Student\n 2.View Students\n 3.Search Student\n 4.Exit")
        ch = int(input("Enter your choice : "));
        while ch!=4:
            if ch==1:
                add()
            elif ch==2:
                view()
            elif ch==3:
                search()                
            elif ch==4:
                break;
            else:
                print("Wrong choice")
            ch = int(input("Which operation do you want to perform : "));
    else:
        print("\nYou are not a valid user...System can't give you permission to access the account....")
#end TY    
#function login
def login():
    global unm,passwd;
    unm = txtUser.get()
    passwd = txtPass.get()
    root.destroy()
    if m==1:
        FY()
    if m==2:
        SY()
    if m==3:
        TY()
#end login        
var = tk.IntVar()
root.title("Student Management System")
root.minsize(500,300)
root.configure(bg='azure')
lblHead = tk.Label(root,text="Student Management System",font=('Vardana',20))
lblHead.pack(side='top',pady=10)
lblHead.configure(bg='azure',fg='navy')
lblMsg = tk.Label(root,text="Select Year of a student : ",font=('Vardana',14))
lblMsg.place(x='25',y='70')
lblMsg.configure(bg='azure',fg='darkslategrey');
radioFY = tk.Radiobutton(root,text="First Year",variable=var,value=1,font=('Vardana',10)).place(x='300',y='120')
radioSY = tk.Radiobutton(root,text="Second Year",variable=var,value=2,font=('Vardana',10)).place(x='300',y='140')
radioTY = tk.Radiobutton(root,text="Third Year",variable=var,value=3,font=('Vardana',10)).place(x='300',y='160')
lblLogin = tk.Label(root,text="Login",font=('Vardana',17))
lblLogin.configure(bg='azure',fg='navy')
lblUser = tk.Label(root,text="User Name ",font=('Vardana',14))
lblUser.configure(bg='azure',fg='black')
txtUser = tk.Entry(root)
lblPass = tk.Label(root,text="Password ",font=('Vardana',14))
lblPass.configure(bg='azure',fg='black')
txtPass = tk.Entry(root)
btnLogin = tk.Button(root,text="Login",command=login)
btnNext = tk.Button(root,text="Next",command=NextPage);
btnNext.configure(bg='steelblue',fg='white')
btnNext.place(x='130',y='200')
root.mainloop()
