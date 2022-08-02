#!/usr/bin/env python3
import page_recipes 
import page_goulash
import page_dumplings
import page_cheesecake
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(page_recipes.template_name,recipies=[
        {"recipe_name":"dumplings","recipe_path":"dumplings"},
        {"recipe_name":"goulash","recipe_path":"goulash"},
        {"recipe_name":"cheesecake","recipe_path":"cheesecake"}])

@app.route('/goulash')
def goulash():
    return page_goulash.recipe()

@app.route('/dumplings')
def dumplings():
    return page_dumplings.recipe()

@app.route('/cheesecake')
def cheesecake():
    return page_cheesecake.recipe()




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
