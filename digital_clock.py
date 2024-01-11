from tkinter import *
import datetime as dt
def date_time():
    time=dt.datetime.now()#it tell the present time
    h=time.strftime('%I')#it is used for denoting the hour ------>These are command ---->if we use capital(H)it tell time for 24 hr if capital(I)used then tell time 12 hr
    m=time.strftime('%M')# it is used for denoting the minute  ------>These are command
    s=time.strftime('%S')#it is used for denoting the second   ------>These are command
    ampm=time.strftime('%p')#it is used for  denoting am ,pm   ------>These are command
    dat=time.strftime('%d')#it is used for the denoting date    ------>These are command
    mnth=time.strftime('%m')#it is used for denoting month     ------>These are command
    yr=time.strftime('%Y')#it is used for denoting year        ------>These are command
    dy=time.strftime('%a')#it is used for denoting day         ------>These are command
    hr.config(text=h)
    min.config(text=m)
    sec.config(text=s)
    am.config(text=ampm)
    date.config(text=dat)
    month.config(text=mnth)
    year.config(text=yr)
    day.config(text=dy)
    

    sec.after(60,date_time)#it recall the function and change the values
clock=Tk()
clock.title('                             --------> @@@@@@@@@@@@@@@@               DIGITAL CLOCK    @@@@@@@@@@@@@     <------')
clock.geometry('1000x500')
clock.config(bg='blue')
#****Time

hr=Label(clock,text='',font=('Time New Roman',30,'bold' ),bg='white',fg='green')
hr.place(x=120,y=40,width=100,height=70)
hr_text=Label(clock,text='hr',font=('Time New Roman',20,'bold'),bg='white',fg='green')
hr_text.place(x=120,y=130,width=100)

min=Label(clock,text='00',font=('Time New Roman',30,'bold' ),bg='white',fg='blue')
min.place(x=320,y=40,width=100,height=70)

min_text=Label(clock,text='mn',font=('Time New Roman',20,'bold' ),bg='white',fg='blue')
min_text.place(x=320,y=130,width=100)

sec=Label(clock,text='00',font=('Time New Roman',30,'bold' ),bg='white',fg='orange')
sec.place(x=520,y=40,width=100,height=70)
sec_text=Label(clock,text='sc',font=('Time New Roman',20,'bold' ),bg='white',fg='orange')
sec_text.place(x=520,y=130,width=100)

am=Label(clock,text='AM/PM',font=('Time New Roman',30,'bold' ),bg='white',fg='black')
am.place(x=720,y=40,width=130,height=70)
am_text=Label(clock,text='AM/PM',font=('Time New Roman',20,'bold' ),bg='white',fg='black')
am_text.place(x=720,y=130,width=130)

#Date 
date=Label(clock,text='00',font=('Time New Roman',30,'bold' ),bg='white',fg='green')
date.place(x=120,y=200,width=100,height=70)
date_text=Label(clock,text='Date',font=('Time New Roman',20,'bold'),bg='white',fg='green')
date_text.place(x=120,y=300,width=100)

month=Label(clock,text='00',font=('Time New Roman',30,'bold' ),bg='white',fg='blue')
month.place(x=320,y=200,width=100,height=70)

month_text=Label(clock,text='Month',font=('Time New Roman',20,'bold' ),bg='white',fg='blue')
month_text.place(x=320,y=300,width=100)

year=Label(clock,text='00',font=('Time New Roman',30,'bold' ),bg='white',fg='orange')
year.place(x=520,y=200,width=100,height=70)
year_text=Label(clock,text='Year',font=('Time New Roman',20,'bold' ),bg='white',fg='orange')
year_text.place(x=520,y=300,width=100)

day=Label(clock,text='day',font=('Time New Roman',30,'bold' ),bg='white',fg='black')
day.place(x=720,y=200,width=130,height=70)
day_text=Label(clock,text='Day',font=('Time New Roman',20,'bold' ),bg='white',fg='black')
day_text.place(x=720,y=300,width=130)

date_time()
clock.mainloop()