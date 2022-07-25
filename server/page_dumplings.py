import page_recipe_template
name="dumplings"
picture="https://www.everyday-delicious.pl/wp-content/uploads/2019/01/Potato-and-cheese-pierogi-the-american-way-%E2%80%93-homemade-cheddar-pierogi-Pierogi-ruskie-po-ameryka%C5%84sku-z-ziemniakami-i-%C5%BC%C3%B3%C5%82tym-serem-www.maine-cook.com-2.jpg"

def recipe():
    return page_recipe_template.page_template.format(name, picture)