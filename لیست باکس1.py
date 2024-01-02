from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('500x450+500+100')
win.resizable(0,0)
win.title('Final Project')
win.configure(bg = '#8C6EEE')
#================Function====================
def Insert():
    if ent_name.get() == '' or ent_family.get() == '':
        messagebox.showinfo('Caution' , 'Enter name and family both')
    else:
        listbox1.insert(END, ent_name.get() + ' ' + ent_family.get() + ' ' + ent_score.get())
    ent_name.delete(0 , END)
    ent_family.delete(0 , END)
    ent_score.delete(0 , END)
    
def Delete():
    x = messagebox.askquestion('Warning' , 'Are you sure?')
    if x == 'yes':
        y = listbox1.curselection()
        listbox1.delete(y)
        
def Clear():
    z = messagebox.askquestion('Warning' , 'This action clear all the box!!!!')
    if z == 'yes':
        listbox1.delete(0,END)
        
def Fetch():
    ent_name.delete(0 , END)
    ent_family.delete(0 , END)
    ent_score.delete(0 , END)
    v = listbox1.curselection()
    lst = listbox1.get(v)
    n = lst.split()
    ent_name.insert(0, n[0])
    ent_family.insert(0, n[1])
    ent_score.insert(0, n[2])
    
    
    
def Exit():
    result = messagebox.askquestion('Warning' , 'Do you want to exit?')
    if result == 'yes':
        win.destroy()
  
# def chang_color():
#     from random import choice
#     lst=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','f']
#     color ='#'
#     for i in range(6):
#         x = choice(lst)
#         color += x
#     win.configure(bg = color)
#     win.lb1_color(text= 'color')
                    
    
#===============Widget=======================
listbox1 = Listbox(win , bg = 'white' , font= 'arial 12' , fg = 'black' , height= 22)
listbox1.place(x= 20 , y=20)
lbl_star = Label(win , text= '*' , font= 'arial 23' , bg = '#8C6EEE' , fg = 'red')
lbl_star.place(x= 230 , y= 40)
lbl_name = Label(win , text = 'Name :' , bg= '#8C6EEE' , font= 'arial 14')
lbl_name.place(x= 250 , y= 40)
ent_name = Entry(win , font= 'arial 10')
ent_name.place(x=340 , y=42)
lbl_family = Label(win , text= ' Family :' , bg = '#8C6EEE' , font= 'arial 14')
lbl_family.place(x=250 , y=90)
ent_family = Entry(win , font = 'arial 10')
ent_family.place(x= 340 , y=93)
lbl_star1 = Label(win , text= '*' , font= 'arial 23' , bg = '#8C6EEE' , fg = 'red')
lbl_star1.place(x= 230 , y= 90)
lbl_score = Label(win , text= 'Score :' , bg = '#8C6EEE' , font= 'arial 14')
lbl_score.place(x=255 , y=140)
ent_score = Entry(win , font= 'arial 10')
ent_score.place(x= 340 , y=143)

btn_insert = Button(win , text = 'Insert' , font= 'arial 12' , bg = '#2163E7' , fg = 'black' , command= Insert , width= 12)
btn_insert.place(x=320 , y=200)
btn_delete = Button(win , text= 'Delete' , font= 'arial 12' , command= Delete , width= 12, bg= '#06E8C8')
btn_delete.place(x= 320 , y= 250)
btn_clear = Button(win , text= 'Clear' , font = 'arial 12' , command= Clear , width= 12, bg= '#06E8C8')
btn_clear.place(x=320 , y=300)
btn_fetch = Button(win , text= 'Fetch' , font= 'arial 12' , command= Fetch , width= 12, bg= '#06E8C8')
btn_fetch.place(x=320 , y= 350)
btn_exit = Button(win , text = 'Exit' , font= 'arial 12' , bg= '#2163E7' , fg= 'black' , command= Exit , width= 12)
btn_exit.place(x=320 , y=400)
# btn_start=Button(win,text='color',font='arial 10',command=chang_color)
# btn_start.place(x=20,y=20)











win.mainloop()