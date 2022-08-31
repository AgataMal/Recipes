#!/usr/bin/env python3
import page_recipes 
import page_add
import page_recipe
from flask_restful import Resource, Api
from flask import Flask, render_template, request

app = Flask(__name__)
api = Api(app)

class RecipeResource(Resource):
    def get(self, recipe_name):
        return page_recipe.get_recipe(recipe_name).__dict__

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        return "OK"
    def delete(self, recipe_name):
        page_recipe.delete_recipe(recipe_name)
        return "OK"



api.add_resource(RecipeResource, '/api/recipie','/api/recipe/<string:recipe_name>')


@app.route('/')
def home():
    return render_template(page_recipes.template_name,recipies=page_recipe.get_recipe_list(),recipe_name="Recipes")


@app.route('/<string:recipe_name>')
def recipe_page(recipe_name):
    return page_recipe.recipe(recipe_name)

@app.route('/Add')
def add():
    return page_add.add()  


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
