import sys

cookbook = {'sandwich': {'ingredient' :['ham', 'bread', 'cheese', 'tomatoes'], 
                        'meal':'lunch',
                        'prep-time' :'10'},
            'cake': {'ingredient' :['flour', 'sugar', 'eggs'],
                    'meal' :'dessert',
                    'prep-time' : '60'},
            'salad': {'ingredient' :['avocado', 'arugula', 'tomatoes', 'spinach'],
                    'meal': 'lunch',
                    'prep-time':'15'}}


def print_recipe(name):
    if name in cookbook.keys():
        print(f'recipe for {name}\n'
              f'Ingredients list: {cookbook[name]["ingredient"]}\n'
              f'To be eaten for: {cookbook[name]["meal"]}\n'
              f'Takes {cookbook[name]["prep-time"]} minutes of cooking.')

def del_recipe(name):
    if name in cookbook.keys():
        del cookbook[name]
    print(f'Deleted {name} recipe.')

def add_recipe(name, ingredient, meal, time):
    cookbook.update({name:{'ingredient' :ingredient, 'meal' :meal, 'prep-time' :time}})
    print(f'{name} add to cookcook')

def print_all():
    print(*cookbook.keys())


print(f'Please select an option by typing the corresponding number:\n'
      f'1: Add a recipe\n'
      f'2: Delete a recipe\n'
      f'3: Print a recipe\n'
      f'4: Print the cookbook\n'
      f'5; Quit\n')
i = input()
while i != '5':
    if i == "1":
        name = input("give a name to your recipe\n")
        ingredient = input("enter the ingredients\n")
        meal = input(" enter the type of meal\n" )
        time = input("time preparation in minutes\n")
        add_recipe(name, ingredient, meal, time)
        i = input
    elif i == '2':
        input(f"Enter the recipe's name you want to remove\n")
        del_recipe(input())
        i = input()
    elif i == '3':
        input("enter the recipe's name you want to print\n")
        print_recipe(input())
        i = input()
    elif i == '4':
        print_all()
        i = input()
    




