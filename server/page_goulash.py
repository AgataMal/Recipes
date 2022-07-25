import page_recipe_template
name="goulash"
picture="https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/recipe/0001/100/gulasz-wieprzowy-z-szynki.jpeg"

def recipe():
    return page_recipe_template.page_template.format(name, picture)