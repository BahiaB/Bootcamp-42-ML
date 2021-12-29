from FileLoader import FileLoader
import pandas as pd
import sys



def proportionBySport(data, year, sport, gender):
    new_data = data[(data["Year"]==year) & (data["Sex"]==gender)]
    new_data = new_data.drop_duplicates(subset="Name")
    new_data1 = new_data[new_data["Sport"]==sport]
    return(float(new_data1.shape[0]/new_data.shape[0]))
    

Loader = FileLoader
data =Loader.load("athlete_events.csv")
print(proportionBySport(data, 2004, 'Tennis', 'F'))