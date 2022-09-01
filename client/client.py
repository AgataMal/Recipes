#!/usr/bin/env python3
from tkinter import *
import requests

def add():
    print("kliklem")
    name = recipe_name_txt.get()
    ingredients = ingredients_txt.get()
    image = image_txt.get()
    steps = steps_text.get()

    requests.post('http://192.168.1.150:5000/api/recipie', json={
        'name': name, 
        'image':image, 
        'ingredients':[ingredients], 
        'steps':[steps]
    })



window=Tk()

window.title('Recipe Client')
window.geometry("800x600+10+10")

recipe_name_txt=Entry(window, text="Name", bd=5)
recipe_name_txt.place(x=30, y=50)


steps_text=Entry(window, text="Steps", bd=5)
steps_text.place(x=30, y=80)

ingredients_txt=Entry(window, text="Ingredients", bd=5)
ingredients_txt.place(x=30, y=110)

image_txt=Entry(window, text="Image", bd=5)
image_txt.place(x=30, y=140)

btn=Button(window, text="Add recipe", fg='blue', command=add)
btn.place(x=80, y=170)



window.mainloop()


