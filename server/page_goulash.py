import page_recipe_template
from flask import render_template 
from model_recipe import Recipe
goulash= Recipe(["meat","vegetables"],
["1 step","2 step"],
"https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/recipe/0001/100/gulasz-wieprzowy-z-szynki.jpeg",
"Goulash")

def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=goulash.name, recipe_image=goulash.image, ingredients= goulash.ingredients,steps=goulash.steps)