from tkinter import*


def onclk(num):
    global op
    
    op=op+str(num)
    text_input.set(op)

def onclear():
    global op
    op=""
    text_input.set("")
    
def onequal():
    global op
    result=str(eval(op))
    text_input.set(result)


cal = Tk()
cal.title("Calculator")
cal.geometry("450x450")
op=""




text_input = StringVar()

textDisplay=Entry(cal,font=('arial',20,'bold'),
                  textvariable=text_input).pack(padx=28,pady=10,fill=BOTH)
#Line1
btn7=Button(cal,font=('arial',20,'bold'),text="7",padx=20,pady=10,command=lambda:onclk(7)).place(x=26,y=50)

btn8=Button(cal,font=('arial',20,'bold'),text="8",padx=20,pady=10,command=lambda:onclk(8)).place(x=130,y=50)

btn9=Button(cal,font=('arial',20,'bold'),text="9",padx=20,pady=10,command=lambda:onclk(9)).place(x=236,y=50)

add=Button(cal,font=('arial',20,'bold'),text="+",padx=20,pady=10,command=lambda:onclk("+")).place(x=344,y=50)

#Line2
btn4=Button(cal,font=('arial',20,'bold'),text="4",padx=20,pady=10,command=lambda:onclk(4)).place(x=26,y=150)

btn5=Button(cal,font=('arial',20,'bold'),text="5",padx=20,pady=10,command=lambda:onclk(5)).place(x=130,y=150)

btn6=Button(cal,font=('arial',20,'bold'),text="6",padx=20,pady=10,command=lambda:onclk(6)).place(x=236,y=150)

sub=Button(cal,font=('arial',20,'bold'),text="-",padx=20,pady=10,command=lambda:onclk("-")).place(x=344,y=150)

#Line3
btn3=Button(cal,font=('arial',20,'bold'),text="3",padx=20,pady=10,command=lambda:onclk(3)).place(x=26,y=250)

btn2=Button(cal,font=('arial',20,'bold'),text="2",padx=20,pady=10,command=lambda:onclk(2)).place(x=130,y=250)

btn1=Button(cal,font=('arial',20,'bold'),text="1",padx=20,pady=10,command=lambda:onclk(1)).place(x=236,y=250)

mul=Button(cal,font=('arial',20,'bold'),text="*",padx=20,pady=10,command=lambda:onclk("*")).place(x=344,y=250)

#Line4
btn0=Button(cal,font=('arial',20,'bold'),text="0",padx=20,pady=10,command=lambda:onclk(0)).place(x=26,y=350)

C=Button(cal,font=('arial',14,'bold'),text="Clear",padx=15,pady=20,command=onclear).place(x=130,y=350)

div=Button(cal,font=('arial',20,'bold'),text="/",padx=20,pady=10,command=lambda:onclk("/")).place(x=236,y=350)

eq=Button(cal,font=('arial',20,'bold'),text="=",padx=20,pady=10,command=onequal).place(x=344,y=350)










cal.mainloop()
