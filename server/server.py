#!/usr/bin/env python3
import page_recipes 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return page_recipes.page_content
    
if __name__ == '__main__':
    app.run(debug=True)
