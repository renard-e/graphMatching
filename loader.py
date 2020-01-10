##
## loader.py for loader in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Fri Jan 10 15:06:21 2020 renard_e
## Last update Sat Jan 10 15:30:42 2020 renard_e
##

import csv

class Loader:
    def __init__(self):
        print("init loader")

    def loadDataFromFile(self, fileName):
        with open(fileName, mode='r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            list_station = list(reader)
        return (list_station)
