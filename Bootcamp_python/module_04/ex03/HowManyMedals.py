from FileLoader import FileLoader
import pandas as pd
import sys

def howManyMedals(data, name):
    my_dict = {}
    new_data = data[(data["Name"]==name)][["Year","Medal"]]
    for year in new_data['Year'].drop_duplicates():
        my_dict[year]=  {'G': new_data['Medal'][(new_data['Year']== year) & (new_data['Medal'] == 'Gold')].count(),
                        'S': new_data['Medal'][(new_data["Year"]== year) & (new_data['Medal'] == 'Silver')].count(),
                        'B': new_data['Medal'][(new_data["Year"]== year) & (new_data['Medal'] == 'Bronze')].count()}

    return(my_dict)







Loader = FileLoader
data =Loader.load("athlete_events.csv")
print(howManyMedals(data, 'Kjetil Andr Aamodt'))