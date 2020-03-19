from tkinter import *

root =Tk()
root.title("Simple calculator")
display= Entry(root,width=35)
display.grid(row=0,column=0,columnspan=3)
def myClick(quote):
    cal=display.get()
    display.delete(0,END)
    display.insert(0,str(cal)+quote)

def equals():
    final=display.get().split("+")
    ans=0
    for num in final:
        ans=ans+int(num)
        print(ans)
    cal=str(ans)   
    print(cal)
    display.delete(0,END)
    display.insert(0,cal) 

def clear():
    display.delete(0,END)


b1= Button(root,text="1",padx=30,pady=10,command=lambda: myClick("1"))
b2= Button(root,text="2",padx=30,pady=10,command=lambda: myClick("2"))
b3= Button(root,text="3",padx=30,pady=10,command=lambda: myClick("3"))
b4= Button(root,text="4",padx=30,pady=10,command=lambda: myClick("4"))
b5= Button(root,text="5",padx=30,pady=10,command=lambda: myClick("5"))
b6= Button(root,text="6",padx=30,pady=10,command=lambda: myClick("6"))
b7= Button(root,text="7",padx=30,pady=10,command=lambda: myClick("7"))
b8= Button(root,text="8",padx=30,pady=10,command=lambda: myClick("8"))
b9= Button(root,text="9",padx=30,pady=10,command=lambda: myClick("9"))
b0= Button(root,text="0",padx=105,pady=10,command=lambda: myClick("0"))
b_add= Button(root,text="+",padx=29,pady=10,command=lambda: myClick("+"))
b_equal= Button(root,text="=",padx=29,pady=10,command= equals)
b_clear=Button(root,text="CLS",padx=23,pady=10,command= clear)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1 ,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,columnspan=3)
b_add.grid(row=5,column=0)
b_equal.grid(row=5,column=1)
b_clear.grid(row=5,column=2)




root.mainloop()