import sys
import string


class Recipe:

    def __init__(self, c_name, c_lvl, c_time, c_ingredients, c_type, c_descrip=None ):
        self.name = check_name(c_name)
        self.lvl = check_lvl(c_lvl)
        self.time = check_time(c_time)
        self.ingredients = check_ingredients(c_ingredients)
        self.description = check_descript(c_descrip)
        self.type = c_type

    def __str__(self):
        ingredients = ','.join(self.ingredients)
        txt = (f'Recipe name: {self.name} \n'
               f'cooking lvl: {self.lvl} \n'
               f'preparation time: {self.time} minutes \n'
               f'ingredients: {ingredients} \n'
               f'recipe type: {self.type} \n'
               f'description: {self.description} \n')
        return(txt)



def check_name(name):
    if isinstance(name, str):
        return name
    else:
        sys.exit(f'{name} must be a string')

def check_lvl(lvl):
    if isinstance(lvl, int):
        if (lvl > 5 or lvl < 1):
            sys.exit(f'{lvl} range lvl 1 - 5')
        return lvl
    else:
        sys.exit(f'{lvl} must be an int')

def check_time(time):
    if isinstance(time, int):
        if (time <= 0):
            sys.exit(f'{time} your time preparation in minutes is wrong')
        return time
    else:
        sys.exit(f'{time} must be an int')

def     check_ingredients(ingredients):
    if isinstance(ingredients, str):
        ingredients = ingredients.split()
        return ingredients
    else: 
        sys.exit(f'{ingredients} must be a string')


def     check_descript(descript):
    if isinstance(descript, str) or not descript:
        #print("ok!!!")
        return descript
    else :
        sys.exit(f'{descript} must be a string or an empty parameters')

def     check_type(type):
    if isinstance(type, str):
        return type
    else:
        sys.exit(f'{type} must be a string')

      