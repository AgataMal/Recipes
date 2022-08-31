from struct import pack
from flask import render_template
from model_recipe import Recipe


cheesecake= Recipe (["cheese", "flavour", "eggs"],
["1 step","2 step"],
"https://media.istockphoto.com/photos/cheesecake-slice-new-york-style-classical-cheese-cake-picture-id1167344045?k=20&m=1167344045&s=612x612&w=0&h=y-dYuj5D2v_narosVM-mGDXFXbjpMKCS_8VlEE79tG4=", 
"cheesecake")

devolay= Recipe(["meat","butter","spices"],
["1 step","2 step"],
"https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/default/0001/24/6ebf5afdab82aed3a98232569344003fb31172ac.jpeg",
"devolay")

dumplings= Recipe (["flavour", "eggs","water"],
["1 step","2 step"],
"https://www.everyday-delicious.pl/wp-content/uploads/2019/01/Potato-and-cheese-pierogi-the-american-way-%E2%80%93-homemade-cheddar-pierogi-Pierogi-ruskie-po-ameryka%C5%84sku-z-ziemniakami-i-%C5%BC%C3%B3%C5%82tym-serem-www.maine-cook.com-2.jpg",
"dumplings")

goulash= Recipe(["meat","vegetables"],
["1 step","2 step"],
"https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/recipe/0001/100/gulasz-wieprzowy-z-szynki.jpeg",
"Goulash")


recipes = {
    "cheesecake": cheesecake,
    "devolay": devolay,
    "dumplings":dumplings,
    "goulash":goulash
}

def get_recipe(recipe_name):
    return recipes[recipe_name]

def recipe(recipe_name):
    recipe = get_recipe(recipe_name)
    return render_template(
        "recipe.html", 
        recipe_name=recipe.name, 
        recipe_image=recipe.image, 
        ingredients= recipe.ingredients,
        steps=goulash.steps
        )