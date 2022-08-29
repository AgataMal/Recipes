from struct import pack
import page_recipe_template
from flask import render_template 
from model_recipe import Recipe
dumplings= Recipe (["flavour", "eggs","water"],
["1 step","2 step"],
"https://www.everyday-delicious.pl/wp-content/uploads/2019/01/Potato-and-cheese-pierogi-the-american-way-%E2%80%93-homemade-cheddar-pierogi-Pierogi-ruskie-po-ameryka%C5%84sku-z-ziemniakami-i-%C5%BC%C3%B3%C5%82tym-serem-www.maine-cook.com-2.jpg",
"dumplings")

def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=dumplings.name, recipe_image=dumplings.image, ingredients=dumplings.ingredients,steps=dumplings.steps)