import sys
import datetime
from recipe import Recipe

class Book:
    def     __init__(self, name):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipe_list = {'starter':[], 'lunch': [], 'dessert': []}


    def     get_recipe_by_name(self, name): 
        if isinstance(name, Recipe):
            for elem in self.recipe_list.values():
                if elem == name:
                    print(f'{elem} ok')
                    return(elem)


    def     get_recipe_by_type(self, type):
        return self.recipe_list[type]


    def     add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipe_list[recipe.type] = recipe
