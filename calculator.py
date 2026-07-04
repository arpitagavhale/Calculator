from tkinter import*
w=Tk()
w.title("Calculator")

global ex
ex=""

def click(b):
 global ex
 ex=ex+b
 v.set(ex)

def eq():
    v.set(eval(ex))

def clear():
    global ex
    ex=""
    v.set("")

def cl():
    global ex
    ex=ex[:-1]
    v.set(ex)


f1=Frame(w)
f1.pack()

f2=Frame(w)
f2.pack()

f3=Frame(w)
f3.pack()

f4=Frame(w)
f4.pack()

f5=Frame(w)
f5.pack()

f6=Frame(w)
f6.pack()

v= StringVar()

e1 = Entry(f1,textvariable=v,justify="right",font=("Arial",14,"bold"),width=16,bd=10)
e1.pack()

b1= Button(f1,text="C",font=("Arial",14,"bold"),width=9,command=clear)
b1.pack(side=LEFT)
b2= Button(f1,text="X",font=("Arial",14,"bold"),width=4,command=cl)
b2.pack(side=LEFT)
b3= Button(f1,text="/",font=("Arial",14,"bold"),width=4,command=lambda:click("/"))
b3.pack(side=LEFT)

b4= Button(f2,text="9",font=("Arial",14,"bold"),width=4,command=lambda:click("9"))
b4.pack(side=LEFT)
b5= Button(f2,text="8",font=("Arial",14,"bold"),width=4,command=lambda:click("8"))
b5.pack(side=LEFT)
b6= Button(f2,text="7",font=("Arial",14,"bold"),width=4,command=lambda:click("7"))
b6.pack(side=LEFT)
b7= Button(f2,text="*",font=("Arial",14,"bold"),width=4,command=lambda:click("*"))
b7.pack(side=LEFT)

b8= Button(f3,text="6",font=("Arial",14,"bold"),width=4,command=lambda:click("6"))
b8.pack(side=LEFT)
b9= Button(f3,text="5",font=("Arial",14,"bold"),width=4,command=lambda:click("5"))
b9.pack(side=LEFT)
b10= Button(f3,text="4",font=("Arial",14,"bold"),width=4,command=lambda:click("4"))
b10.pack(side=LEFT)
b11= Button(f3,text="+",font=("Arial",14,"bold"),width=4,command=lambda:click("+"))
b11.pack(side=LEFT)

b12= Button(f4,text="3",font=("Arial",14,"bold"),width=4,command=lambda:click("3"))
b12.pack(side=LEFT)
b13= Button(f4,text="2",font=("Arial",14,"bold"),width=4,command=lambda:click("2"))
b13.pack(side=LEFT)
b14= Button(f4,text="1",font=("Arial",14,"bold"),width=4,command=lambda:click("1"))
b14.pack(side=LEFT)
b15= Button(f4,text="-",font=("Arial",14,"bold"),width=4,command=lambda:click("-"))
b15.pack(side=LEFT)

b16= Button(f5,text="0",font=("Arial",14,"bold"),width=4,command=lambda:click("0"))
b16.pack(side=LEFT)
b17= Button(f5,text=".",font=("Arial",14,"bold"),width=4,command=lambda:click("."))
b17.pack(side=LEFT)
b18= Button(f5,text="=",font=("Arial",14,"bold"),width=9,command=eq)
b18.pack(side=LEFT)

w.mainloop()



