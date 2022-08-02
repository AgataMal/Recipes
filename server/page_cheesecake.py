from struct import pack
import page_recipe_template
from flask import render_template 
name="cheesecake"
picture="https://media.istockphoto.com/photos/cheesecake-slice-new-york-style-classical-cheese-cake-picture-id1167344045?k=20&m=1167344045&s=612x612&w=0&h=y-dYuj5D2v_narosVM-mGDXFXbjpMKCS_8VlEE79tG4="

def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=name, recipe_image=picture, ingredients=["cheese", "flavour", "eggs"])