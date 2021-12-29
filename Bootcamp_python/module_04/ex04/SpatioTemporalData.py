from FileLoader import FileLoader
import pandas as pd
import sys

class  SpatioTemporalData:

    def __init__(self, data):
        self.data = data

    def when(self, location):
        my_list = []
        new_data = self.data[(self.data["City"]==location)]
        my_list = new_data["Year"].drop_duplicates().to_list()
        return (my_list)
       
    def where(self, date):
        my_list = []
        new_data = self.data[(self.data["Year"]==date)]
        my_list = new_data["City"].drop_duplicates().to_list
        return(my_list)


Loader = FileLoader
data =Loader.load("athlete_events.csv")
std = SpatioTemporalData(data)
print(std.when('Paris'))
print(std.where(1992))
