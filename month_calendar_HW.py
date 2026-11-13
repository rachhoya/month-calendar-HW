from tkinter import *
import calendar

window=Tk()
window.geometry("400x350")
window.title("Calendar")
window.config(background="green")

def show_calendar():
    window1=Toplevel(window)
    window1.geometry("550x600")
    window1.title("CALENDAR")
    window1.config(background="white")
    year=int(entry_box.get())
    month=int(entry_box2.get())
    year2=calendar.month(year,month)

    contents=Label(window1,text=year2,font=("Consolas",10,"bold"))
    contents.grid(row=5,column=1,padx=40,pady=20)


    
    window1.mainloop()


cal=Label(window,text="CALENDAR",bg="dark grey",font=("Times",28,"bold"))
cal.place(x=95,y=20)

enter=Label(window,text="Enter Year",bg="light grey",font=("Arial",16,"bold"))
enter.place(x=150,y=90)

entry_box=Entry(window,width=15,font=("Arial",16,"bold"),justify="center")
entry_box.place(x=112,y=130)

month=Label(window,text="Enter Month",bg="light grey",font=("Arial",15,"bold"))
month.place(x=40,y=175)

entry_box2=Entry(window,width=15,font=("Arial",16,"bold"))
entry_box2.place(x=170,y=175)

show=Button(window,text="Show Month",bg="light grey",font=("Arial",16,"bold"),command=show_calendar,justify="center")
show.place(x=130,y=220)

exit=Button(window,text="Exit",bg="pink",font=("Arial",13,"bold"),bd=3,relief="raised",command=window.destroy)
exit.place(x=175,y=280)

window.mainloop()