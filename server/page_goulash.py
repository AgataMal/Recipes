import page_recipe_template
from flask import render_template 

name="goulash"
picture="https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/recipe/0001/100/gulasz-wieprzowy-z-szynki.jpeg"

def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=name, recipe_image=picture, ingredients= ["meat","vegetables"],steps=["1 step","2 step"])