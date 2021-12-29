from FileLoader import FileLoader
import pandas as pd
import sys

def youngestFellah(data, year):

    
    mydict = { 'f': data["Age"][(data["Sex"] == 'F') & (data["Year"] == year)].min(),
            'm': data['Age'][(data['Sex'] == 'M') & (data['Year'] == year)].min()}
    return(mydict)
    


loader = FileLoader
data = loader.load("athlete_events.csv")

print(youngestFellah(data, 1996))