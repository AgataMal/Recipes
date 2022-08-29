from struct import pack
import page_recipe_template
from flask import render_template
from model_recipe import Recipe

cheesecake= Recipe (["cheese", "flavour", "eggs"],
["1 step","2 step"],
"https://media.istockphoto.com/photos/cheesecake-slice-new-york-style-classical-cheese-cake-picture-id1167344045?k=20&m=1167344045&s=612x612&w=0&h=y-dYuj5D2v_narosVM-mGDXFXbjpMKCS_8VlEE79tG4=", 
"cheesecake")

def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=cheesecake.name, recipe_image=cheesecake.image, ingredients=cheesecake.ingredients,steps=cheesecake.steps)