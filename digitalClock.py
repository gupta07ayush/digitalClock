# Make a digital clock in python
from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    

    lab_hr.after(200,date_time)



clock = Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.config(bg='black')

# ***** Time
lab_hr =Label(clock,text="00", font=("Times New Roman",60,"bold"),
              bg="indigo", fg="white")
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_txt =Label(clock,text="Hour", font=("Times New Roman",18,"bold"),
              bg="grey", fg="black")
lab_hr_txt.place(x=120,y=180,height=25,width=100)



lab_min =Label(clock,text="00", font=("Times New Roman",60,"bold"),
              bg="indigo", fg="white")
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_txt =Label(clock,text="Min", font=("Times New Roman",18,"bold"),
              bg="grey", fg="black")
lab_min_txt.place(x=340,y=180,height=25,width=100)



lab_sec =Label(clock,text="00", font=("Times New Roman",60,"bold"),
              bg="indigo", fg="white")
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_txt =Label(clock,text="Sec", font=("Times New Roman",18,"bold"),
              bg="grey", fg="black")
lab_sec_txt.place(x=560,y=180,height=25,width=100)



lab_am =Label(clock,text="00", font=("arial",40,"bold"),
              bg="blue", fg="black")
lab_am.place(x=780,y=50,height=110,width=100)
lab_am_txt =Label(clock,text="AM/PM", font=("Times New Roman",16,"bold"),
              bg="grey", fg="black")
lab_am_txt.place(x=780,y=180,height=25,width=100)



# **** Date
lab_date =Label(clock,text="00", font=("Times New Roman",35,"bold"),
              bg="indigo", fg="white")
lab_date.place(x=120,y=300,height=80,width=100)
lab_date_txt =Label(clock,text="Date", font=("Times New Roman",18,"bold"),
              bg="grey", fg="black")
lab_date_txt.place(x=120,y=400,height=25,width=100)


lab_mo =Label(clock,text="00", font=("Times New Roman",35,"bold"),
              bg="indigo", fg="white")
lab_mo.place(x=340,y=300,height=80,width=100)
lab_mo_txt =Label(clock,text="Month", font=("Times New Roman",18,"bold"),
              bg="grey", fg="black")
lab_mo_txt.place(x=340,y=400,height=25,width=100)



lab_year =Label(clock,text="00", font=("Times New Roman",35,"bold"),
              bg="indigo", fg="white")
lab_year.place(x=560,y=300,height=80,width=100)
lab_year_txt =Label(clock,text="Year", font=("Times New Roman",18,"bold"),
              bg="grey", fg="black")
lab_year_txt.place(x=560,y=400,height=25,width=100)


lab_day =Label(clock,text="00", font=("arial",32,"bold"),
              bg="blue", fg="black")
lab_day.place(x=780,y=300,height=80,width=100)
lab_day_txt =Label(clock,text="Day", font=("Times New Roman",18,"bold"),
              bg="grey", fg="black")
lab_day_txt.place(x=780,y=400,height=25,width=100)


date_time()

clock.mainloop()
