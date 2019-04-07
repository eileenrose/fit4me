'''GUI''' 

from tkinter import * 
from ul import ul as top
from dv import dv as bott
from input import findNutrients
from collections import defaultdict 

#Main window 
root = Tk() 
root.title("Fit4Me") 
root.configure(background="#bee3f7") 
root.geometry("500x500") 
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

ageBox=Text(root,height=1, width=20)
ageBox.pack()
input_age=ageBox.get("1.0","end-1c")
if(input_age): age=input_age
        


age=0 #Default age is 0 
levels=defaultdict(int)

#Calculates age range 
for rang in [(0,0.5),(0.5,1),(1,3),(4,8),(9,13),(14,18),(19,150)]:
    if rang[0]<=int(age)<=rang[1]: 
        age_range=rang 
        break 
    
for nut in top: levels[nut]=0

nutrient_list = Listbox(root, yscrollcommand = scrollbar.set, bg="#fcd4f0",font=('Arial',12), height=1, width = 40)
nutrient_list.update()

textBox=Text(root, height=1, width=20)
textBox.pack()

key_list=list(top.keys())

def keyFood(event): 
    '''Given an input food, calculates nutritional value of 100g and prints it in table format'''
    inp=textBox.get("1.0","end-1c") 
    info = findNutrients(inp.strip())
    for nut in info:
        levels[nut]+=info[nut]
    
    for line in range(len(key_list)): 
        descript="" 
        if levels[key_list[line]] > top[key_list[line]][age_range]:descript=" (TOO MUCH!!!)" 
        elif levels[key_list[line]]<bott[key_list[line]][age_range]:descript=" (TOO LITTLE!!!)" 
        nutrient_list.insert(END,key_list[line]+":" + str(levels[key_list[line]])+descript)
        
    textBox.delete("1.0",END)
    nutrient_list.pack(side=LEFT,fill=BOTH)
    
def keyAge(event): 
    '''Given string rep. age, calculates age range of user'''
    global age 
    age = ageBox.get("1.0","end-1c")
    ageBox.delete("1.0",END)
    for rang in [(0,0.5),(0.5,1),(1,3),(4,8),(9,13),(14,18),(19,150)]:
        if rang[0]<=int(age)<=rang[1]: 
            age_range=rang 
            break 

#Binds return key to updating functions 
textBox.bind("<Return>",keyFood) 
ageBox.bind("<Return>",keyAge) 

#Continuously updates window 
nutrient_list.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=nutrient_list.yview)
mainloop()

