import page_recipe_template
from flask import render_template 

name="devolay"
picture="https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/default/0001/24/6ebf5afdab82aed3a98232569344003fb31172ac.jpeg"

def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=name, recipe_image=picture, ingredients= ["meat","butter","spices"],steps=["1 step","2 step"])