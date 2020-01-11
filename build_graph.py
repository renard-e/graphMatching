##
## build_graph.py for graphMatch in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Thu Jan 9 13:56:04 2020 renard_e
## Last update Sat Jan 10 15:27:16 2020 renard_e
##

import networkx as nx
import matplotlib.pyplot as plt

class GGraph:
    __graph = nx.Graph()
    __fileNameData = "data.csv"
    __fileNameSaveImage = "./image/saved_graph"
    __node_color= "#b6cef2"
    __edge_color_unmatched = '#ff0000'
    __edge_color_matched = '#00ff04'
    __loader = Loader()
    __list_champs_data = list()
    
    def __init__(self):
        print("init graph")
        
    def getGraph(self):
        return (__graph)
    
    def setGraph(self, mapData):
        self.__graph.clear()
        list_station = self.__loader.loadDataFromFile(self.__fileNameData)

        self.__list_champs_data = list_station[0]
        print(self.__list_champs_data[0])
        cpt = 0
        while (cpt != 10):
            self.__graph.add_node(cpt)
            cpt += 1
        self.__graph.add_edge(0, 9)
        self.__graph.add_edge(4, 2)
        self.__graph.add_edge(9, 7)
        self.__graph.add_edge(8, 2)
        self.__graph.add_edge(1, 4)
    def saveGraph(self):
        plt.savefig(self.__fileNameSaveImage)
        
    def showGraph(self, unmatchedList, matchedList):
        pos = nx.spring_layout(self.__graph)
        nx.draw(self.__graph,
                pos = pos,
                node_size= 200,
                node_color= self.__node_color,
                edgelist=unmatchedList, 
                edge_color =  self.__edge_color_unmatched,
                font_size= 8,
                width = 1,
                with_labels = True)
        nx.draw(self.__graph,
                pos = pos,
                node_size= 200,
                node_color= self.__node_color,
                edgelist=matchedList, 
                edge_color = self.__edge_color_matched,
                font_size= 8,
                width = 1,
                with_labels = True)
        plt.show()

graph = GGraph()
#creation des edges et des nodes puis le matching se chargera de determiner les deux lists "unmatched" et "matched", set devra aussi faire les liens entre les nodes en fonctions des critere demander
#cree les liens apres la selection des champs voulu 
graph.setGraph()
graph.showGraph([(0, 9), (4, 2), (9, 7)], [(1, 4), (8, 2)]) 
