import page_recipe_template
from flask import render_template 
from model_recipe import Recipe


def recipe():
    return render_template(page_recipe_template.template_name, recipe_name=goulash.name, recipe_image=goulash.image, ingredients= goulash.ingredients,steps=goulash.steps)