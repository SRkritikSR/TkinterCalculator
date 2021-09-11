from tkinter import *
from tkinter import messagebox

screen=Tk()
screen.title("CALCULATOR")
screen.geometry("250x250")

##welcome_note=Label(text="CALCULATOR",fg="black",bg="white")
##welcome_note.grid(row=0,column=0)
Num_List=[]
Float_Num=0.0
Result_Text=Entry(bd="5")
Result_Text.grid(row=0,column=0,columnspan=4)
def Final_Display():
        Num_Str=''.join([str(elem) for elem in Num_List])
        Result_Text.delete(0,len(Num_List))
        Result_Text.insert(0,eval(Num_Str))
def Warning_Dlt():
        if (type(Num_List[0])!=int) or (type(Num_List[-2])!=int):
                messagebox.showwarning("warning","add number before operator Or delete any previous symbol")
def display():
        Result_Text.insert(len(Num_List)-1,Num_List[-1])
        print(Num_List[-1])

def Button_1():
    Num_List.append(1)
    display()

def Button_2():
    Num_List.append(2)
    display()
def Button_3():
    Num_List.append(3)
    display()
def Button_4():
    Num_List.append(4)
    display()
def Button_5():
    Num_List.append(5)
    display()
def Button_6():
    Num_List.append(6)
    display()
def Button_7():
    Num_List.append(7)
    display()
def Button_8():
    Num_List.append(8)
    display()
def Button_9():
    Num_List.append(9)
    display()
def Button_0():
    Num_List.append(0)
    display()
def Button_dot():
    Num_List.append(".")
    display()
    Warning_Dlt()
    if type(Num_List[0])!=int :
            messagebox.showwarning("warning", "add zero before decimal")
def Add_Them():
    Num_List.append("+")
    display()
    Warning_Dlt()
        
def Subt_Them():
    Num_List.append("-")
    display()
    Warning_Dlt()
def Mult_Them():
    Num_List.append("*")
    display()
    Warning_Dlt()
def Div_Them():
    Num_List.append("/")
    display()
    Warning_Dlt()
def Button_Clear():
    Num_List.pop()
    Result_Text.delete(len(Num_List))
def Equal_Them():
    print(Num_List)
    Final_Display()
    
##    print(Num_Str)
##    print(eval(Num_Str))
   
    

        
    
    
                       
##create the below one with grid
Button_1=Button(text="1",height=2,width=5,command=Button_1)
Button_1.grid(row=1,column=0,padx=0)
Button_2=Button(text="2",height=2,width=5,command=Button_2)
Button_2.grid(row=1,column=1,padx=2)
Button_3=Button(text="3",height=2,width=5,command=Button_3)
Button_3.grid(row=1,column=2,padx=2)
Button_div=Button(text="/",height=2,width=5,command=Div_Them)
Button_div.grid(row=1,column=3,padx=2)
Button_4=Button(text="4",height=2,width=5,command=Button_4)
Button_4.grid(row=2,column=0,padx=2,pady=2)
Button_5=Button(text="5",height=2,width=5,command=Button_5)
Button_5.grid(row=2,column=1,padx=2)
Button_6=Button(text="6",height=2,width=5,command=Button_6)
Button_6.grid(row=2,column=2,padx=2)
Button_mult=Button(text="x",height=2,width=5,command=Mult_Them)
Button_mult.grid(row=2,column=3,padx=2)
Button_7=Button(text="7",height=2,width=5,command=Button_7)
Button_7.grid(row=3,column=0,pady=2)
Button_8=Button(text="8",height=2,width=5,command=Button_8)
Button_8.grid(row=3,column=1,padx=2)
Button_9=Button(text="9",height=2,width=5,command=Button_9)
Button_9.grid(row=3,column=2,padx=2)
Button_add=Button(text="+",height=2,width=5,command=Add_Them)
Button_add.grid(row=3,column=3,padx=2)
Button_0=Button(text="0",height=2,width=5,command=Button_0)
Button_0.grid(row=4,column=0,pady=2)
Button_dot=Button(text=".",height=2,width=5,command=Button_dot)
Button_dot.grid(row=4,column=1,padx=2)
Button_clear=Button(text="clear",height=2,width=5,command=Button_Clear)
Button_clear.grid(row=4,column=2,padx=2)
Button_subt=Button(text="-",height=2,width=5,command=Subt_Them)
Button_subt.grid(row=4,column=3,padx=2)
Button_equal=Button(text="=",height=2,width=5,command=Equal_Them)
Button_equal.grid(row=4,column=4,padx=2)

screen.mainloop()
