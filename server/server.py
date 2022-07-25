#!/usr/bin/env python3
import page_recipes 
import page_goulash
import page_dumplings
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return page_recipes.page_content

@app.route('/goulash')
def goulash():
    return page_goulash.recipe()

@app.route('/dumplings')
def dumplings():
    return page_dumplings.recipe()


if __name__ == '__main__':
    app.run(debug=True)
