from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry('700x700')
window.title('Bmi calculater')
window.resizable(0,0)

frame=Frame(window,relief='raised',cursor='hand2',
            width=700,height=700,bg='light blue')
frame.grid(row=0,column=0)

#Weight
label1=Label(frame,text='Weight(Kg):',background='cyan',
             bd=15,relief='raised',font='Helvetica 15 bold')
label1.place(x=10,y=135)

entry1= Entry(frame,insertbackground='blue',font='Helvetica 15 bold',bg='grey')
entry1.place(x=160,y=135,relwidth=0.2,relheight=0.1)

#Height
label2=Label(frame,text='Height(Cm):',background='cyan',
             bd=15,relief='raised',font='Helvetica 15 bold')
label2.place(x=10,y=200)

entry2=Entry(frame,insertbackground='blue',
             cursor='hand1',font='Helvetica 15 bold',bg='grey')
entry2.place(x=160,y=200,relwidth=0.2,relheight=0.1)


def results():
    w=IntVar()
    h=IntVar()
    w = float(entry1.get())
    h=float(entry2.get())
    bmi=w/((h/100)**2) 
    if bmi<18.5:
        bmi_result='Underweight'
    elif bmi>=18.5 and bmi<=24.9:
        bmi_result='Normal'
    elif bmi>=25.0 and bmi<=29.9:
        bmi_result='Overweight'
    else:
        bmi_result='Obese'
    messagebox.showinfo('BMI result',
                        'your BMI result is %s and you are %s'%(bmi,bmi_result))

btn=Button(frame,text='BMI',relief='ridge',bg='yellow green',
           activeforeground='yellow green',font='Helvetica 15 bold',command=results)
btn.place(x=10,y=400,relwidth=0.3,relheight=0.05)


window.mainloop()