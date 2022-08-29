import page_recipe_template
from flask import render_template 
from model_recipe import Recipe
devolay= Recipe(["meat","butter","spices"],
["1 step","2 step"],
"https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/default/0001/24/6ebf5afdab82aed3a98232569344003fb31172ac.jpeg",
"devolay")

def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=devolay.name, recipe_image=devolay.image, ingredients= devolay.ingredients,steps=devolay.steps)