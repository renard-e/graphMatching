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
from node import node
class GGraph:
    __graph = nx.Graph()
    __node_color= "#b6cef2"
    __edge_color_unmatched = '#ff0000'
    __edge_color_matched = '#00ff04'
    __matchedList = list()
    __unmatchedList = list()
    __listNode = list()
    __listEdge = list()
    
    def getGraph(self):
        return (__graph)
    
    def setGraph(self, mapData, limit, edgesSelect, nodeSelect):
        self.__graph.clear()
        self.__unmatchedList.clear()
        self.__matchedList.clear()
        self.__listEdge().clear()
        self.__listNode().clear()

        self.__graph.add_node("lol")
        self.__graph.add_node("lol2")
        self.__unmatchedList = [(0, 9), (4, 2), (9, 7)]
        self.__matchedList = [(1, 4), (8, 2), ("lol", "lol2")]
        cpt = 0
        while (cpt != 10):
            self.__graph.add_node(cpt)
            cpt += 1
        self.__graph.add_edge(0, 9)
        self.__graph.add_edge(4, 2)
        self.__graph.add_edge(9, 7)
        self.__graph.add_edge(8, 2)
        self.__graph.add_edge(1, 4)
        self.__graph.add_edge("lol", "lol2")
        return (True)
        
    def saveGraph(self, fileName):
        plt.savefig(fileName)
        
    def showGraph(self):
        pos = nx.spring_layout(self.__graph)
        nx.draw(self.__graph,
                pos = pos,
                node_size= 200,
                node_color= self.__node_color,
                edgelist = self.__unmatchedList, 
                edge_color =  self.__edge_color_unmatched,
                font_size= 8,
                width = 1,
                with_labels = True)
        nx.draw(self.__graph,
                pos = pos,
                node_size= 200,
                node_color= self.__node_color,
                edgelist= self.__matchedList, 
                edge_color = self.__edge_color_matched,
                font_size= 8,
                width = 1,
                with_labels = True)
        plt.show()

    def setUnmatchedList(self, newList):
        self.__unmatchedList = newList

    def setMatchedList(self, newList):
        self.__matchedList = newList
