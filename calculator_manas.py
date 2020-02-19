# created BY Manasvi Srivastava 
import tkinter as tk
#create tkinter cal.configure(background='grey')
cal=tk.Tk()
cal.title("Calculator_Manas")
cal.geometry("290x420+500+150")
cal.resizable(0,0)


#variable 
user=tk.StringVar() 
data=tk.StringVar()
opt=""
tmp=0
dt=0
inf=0

#for 1 to 9 definition
def one():
    data=user.get()
    data=data+str(1)
    user.set(data)
    
def two():
    data=user.get()
    data=data+str(2)
    user.set(data)
    
def three():
    data=user.get()
    data=data+str(3)
    user.set(data)

def four():
    data=user.get()
    data=data+str(4)
    user.set(data)

def five():
    data=user.get()
    data=data+str(5)
    user.set(data)

def six():
    data=user.get()
    data=data+str(6)
    user.set(data)

def seven():
    data=user.get()
    data=data+str(7)
    user.set(data)

def eight():
    data=user.get()
    data=data+str(8)
    user.set(data)

def nine():
    data=user.get()
    data=data+str(9)
    user.set(data)
def zero():
    data=user.get()
    data=data+str(0)
    user.set(data)

#for symbol's definition
def PW():
    cal.destroy()
    
def AC():
    global tmp
    user.set('0')
    tmp=0
    
def CE():
    global tmp
    global inf
    global dt
    if(inf==1):
        data=user.get()
        data=str(data)
        i=len(data)
        data=data[:i-1]
        data=data.strip()
        user.set(data)
        dt=0
    else:
        data=int(user.get())
        data=data/10 
        user.set(data)
        dt=0
        
def dot():
    global tmp
    global dt
    global inf
    if dt==0:
        data=user.get()
        data=data+'.'
        user.set(data)
        dt=1
        inf=1

def plus():
    global tmp
    global opt
    global inf
    global dt
    if inf==1:
        if opt=='-':
            tmp=tmp-float(user.get())
            user.set("")
        if opt=='*':
            tmp=tmp*float(user.get())
            user.set("")
        if opt=='/':
            tmp=tmp/float(user.get())
            user.set("")
        if opt=='%':
            tmp=(tmp*float(user.get()))/100
            user.set("")
        opt='+'
        if len(user.get())>0:
            d=float(user.get())
            tmp=tmp+d
            dt=0
            user.set("")
            print (tmp)
    else:
        if opt=='-':
            tmp=tmp-int(user.get())
            user.set("")
        if opt=='*':
            tmp=tmp*int(user.get())
            user.set("")
        if opt=='/':
            tmp=tmp/int(user.get())
            user.set("")
        if opt=='%':
            tmp=(tmp*int(user.get()))/100
            user.set("")
        opt='+'
        if len(user.get())>0:
            d=int(user.get())
            tmp=tmp+d
            dt=0
            user.set("")
            print (tmp)
    
def minus():
    global tmp
    global opt
    global dt
    global inf
    if inf==1:
         if opt=='+':
             tmp=tmp+float(user.get())
             user.set("")
         if opt=='*':
             tmp=tmp*float(user.get())
             user.set("")
         if opt=='/':
             tmp=tmp/float(user.get())
             user.set("")
         if opt=='%':
             tmp=(tmp*float(user.get()))/100
             user.set("")
         opt='-'
         if len(user.get())>0:
            d=float(user.get())
            dt=0
            user.set("")
            if tmp!=0:
                tmp=tmp-d
            else:
                tmp=d
            print (tmp)
    else:
        if opt=='+':
            tmp=tmp+int(user.get())
            user.set("")
        if opt=='*':
            tmp=tmp*int(user.get())
            user.set("")
        if opt=='/':
            tmp=tmp/int(user.get())
            user.set("")
        if opt=='%':
            tmp=(tmp*int(user.get()))/100
            user.set("")
        opt='-'
        if len(user.get())>0:
             d=int(user.get())
             dt=0
             user.set("")
             if tmp!=0:
                 tmp=tmp-d
             else:
                tmp=d
             print (tmp)
def multiply():
    global tmp
    global opt
    global dt
    global inf
    if inf==1:
        if opt=='+':
            tmp=tmp+float(user.get())
            user.set("")
        if opt=='-':
            tmp=tmp-float(user.get())
            user.set("")
        if opt=='/':
            tmp=tmp/float(user.get())
            user.set("")
        if opt=='%':
            tmp=(tmp*float(user.get()))/100
            user.set("")
        opt='*'
        if len(user.get())>0:
           d=float(user.set())
           if tmp==0:
               tmp=1
           else:
               user.set("")
               if(d>0):
                   tmp=tmp*d
                   dt=0
                   user.set("")
                   print (tmp)
    else:
        if opt=='+':
            tmp=tmp+int(user.get())
            user.set("")
        if opt=='-':
            tmp=tmp-int(user.get())
            user.set("")
        if opt=='/':
            tmp=tmp/int(user.get())
            user.set("")
        if opt=='%':
            tmp=(tmp*int(user.get()))/100
            user.set("")
        opt='*'
        if len(user.get())>0:
            d=int(user.get())
            if tmp==0:
                tmp=1
            else:
                user.set("")
            if(d>0):
                tmp=tmp*d
                dt=0
                user.set("")
                print (tmp)

def divide():
    global tmp
    global opt
    global dt
    global inf
    if inf==1:
        if opt=='+':
            tmp=tmp+float(user.get())
            user.set("")
        if opt=='-':
            tmp=tmp-float(user.get())
            user.set("")
        if opt=='*':
            tmp=tmp*float(user.get())
            user.set("")
        if opt=='%':
            tmp=(tmp*float(user.get()))/100
            user.set("")
        opt='/'
        if len(user.get())>0:
            tmp=float(user.get())
            dt=0
            user.set("")
            print (tmp)
    else:
        if opt=='+':
            tmp=tmp+int(user.get())
            user.set("")
        if opt=='-':
            tmp=tmp-int(user.get())
            user.set("")
        if opt=='*':
            tmp=tmp*int(user.get())
            user.set("")
        if opt=='%':
            tmp=(tmp*int(user.get()))/100
            user.set("")
        opt='/'
        if len(user.get())>0:
            tmp=int(user.get())
            dt=0
            user.set("")
            print (tmp)

def percent():
    global tmp
    global opt
    global dt
    global inf
    if inf==1:
        if opt=='+':
            tmp=tmp+float(user.get())
            user.set("")
        if opt=='-':
            tmp=tmp-float(user.get())
            user.set("")
        if opt=='*':
            tmp=tmp*float(user.get())
            user.set("")
        if opt=='/':
            tmp=tmp/float(user.get())
            user.set("")
        opt='%'
        if len(user.get())>0:
            tmp=float(user.get())
            dt=0
            user.set("")
            print (tmp)
    else:
        if opt=='+':
            tmp=tmp+int(user.get())
            user.set("")
        if opt=='-':
            tmp=tmp-int(user.get())
            user.set("")
        if opt=='*':
            tmp=tmp*int(user.get())
            user.set("")
        if opt=='/':
            tmp=tmp/int(user.get())
            user.set("")
        opt='%'
        if len(user.get())>0:
            tmp=int(user.get())
            dt=0
            user.set("")
            print (tmp)

         

def equal():
    global tmp
    global opt
    global inf
    global dt
    if opt=='+':
         if(inf==0):
             tmp=tmp+int(user.get())
             user.set(tmp)
             tmp=0
             opt=""
         else:
             tmp=tmp+float(user.get())
             user.set(tmp)
             tmp=0
             opt=""
    elif opt=='-':
        if(inf==0):
            tmp=tmp-int(user.get())
            user.set(tmp)
            tmp=0
            opt=""
        else:
            tmp=tmp-float(user.get())
            user.set(tmp)
            tmp=0
            opt=""
    elif opt=='*':
        if (inf==0):
            if(str(user.get())>0.0):
                tmp=tmp*int(user.get())
                user.set(tmp)
                tmp=0
        else:
            if(str(user.get())>0):
                tmp=tmp*float(user.get())
                user.set(tmp)
                tmp=0
            
    elif opt=='/':
        if(inf==0):
            tmp=tmp/float(user.get())
            user.set(tmp)
            tmp=0
        else:
            tmp=tmp/float(user.get())
            user.set(tmp)
            tmp=0
    elif opt=='%':
        if(inf==0):
            tmp=(tmp*int(user.get()))/100
            user.set(tmp)
            tmp=0
        else:
            tmp=(tmp*float(user.get()))/100
            user.set(tmp)
            tmp=0

#for entry
E77=tk.Entry(cal,textvariable=user,width=9,bg='grey',bd=13 ,font=('Arial',40,),justify="right")
E77.place(x=0,y=0)


#for symbols
# for +
B11=tk.Button(cal,text="+",command=plus,height=1,width=3,bd=6,bg='white',font=('Arial',20,'bold'))
B11.place(x=5,y=90)

# for -
B22=tk.Button(cal,text="-",command=minus,height=1,width=3,bd=6,bg='white',font=('Arial',20,'bold'))
B22.place(x=75,y=90)

# for *
B33=tk.Button(cal,text="*",command=multiply,height=1,width=3,bd=6,bg='white',font=('Arial',20,'bold'))
B33.place(x=145,y=90)

# for /
B44=tk.Button(cal,text="/",command=divide,height=1,width=3,bd=6,bg='white',font=('Arial',20,'bold'))
B44.place(x=215,y=90)

# for %
B55=tk.Button(cal,text="%",command=percent,height=1,width=3,bd=6,bg='pink',font=('Arial',20,'bold'))
B55.place(x=215,y=155)

# for =
B66=tk.Button(cal,text="=",command=equal,height=1,width=3,bd=6,bg='pink',font=('Arial',20,'bold'))
B66.place(x=215,y=220)

# for PW
B111=tk.Button(cal,text="PW",command=PW,height=1,width=3,bd=6,bg='black',fg='white',font=('Arial',20,'bold'))
B111.place(x=5,y=350)

# for CE
B222=tk.Button(cal,text="CE",command=CE,height=1,width=3,bd=6,bg='pink',font=('Arial',20,'bold'))
B222.place(x=75,y=350)

# for AC
B333=tk.Button(cal,text="AC",command=AC,height=1,width=3,bd=6,bg='pink',font=('Arial',20,'bold'))
B333.place(x=145,y=350)

# for .
B444=tk.Button(cal,text=".",command=dot,height=1,width=3,bd=6,bg='pink',font=('Arial',20,'bold'))
B444.place(x=215,y=350)



#for 0 to 9 button
# for 1
B1=tk.Button(cal,text="1",command=one,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B1.place(x=5,y=285)

# for 2
B2=tk.Button(cal,text="2",command=two,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B2.place(x=75,y=285)

# for 3
B3=tk.Button(cal,text="3",command=three,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B3.place(x=145,y=285)

# for 4
B4=tk.Button(cal,text="4",command=four,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B4.place(x=5,y=220)

# for 5
B5=tk.Button(cal,text="5",command=five,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B5.place(x=75,y=220)

# for 6
B6=tk.Button(cal,text="6",command=six,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B6.place(x=145,y=220)

# for 7
B7=tk.Button(cal,text="7",command=seven,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B7.place(x=5,y=155) 

# for 8
B8=tk.Button(cal,text="8",command=eight,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B8.place(x=75,y=155)

# for 9
B9=tk.Button(cal,text="9",command=nine,height=1,width=3,bd=6,bg='grey',font=('Arial',20,'bold'))
B9.place(x=145,y=155)

# for 0
B0=tk.Button(cal,text="0",command=zero,height=1,width=3,bd=6,bg='pink',font=('Arial',20,'bold'))
B0.place(x=215,y=285) 

cal.mainloop()

