##
## edge.py for edge in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Wed Jan 15 08:27:18 2020 renard_e
## Last update Thu Jan 15 08:27:28 2020 renard_e
##

from node import Node

class Edge:
    
    __isMatched = False
    __firstNode = None
    __secondNode = None
    
    def __init__(self, firstNode, secondNode):
        self.__firstNode = firstNode
        self.__secondNode = secondNode

    def setIsMatched(self, newValue):
        self.__isMatched = newValue

    def getIsMatched(self):
        return (self.__isMatched)

    def getNodes(self):
        listNode = list()
        
        listNode.append(self.__firstNode.getNodeName())
        listNode.append(self.__secondNode.getNodeName())
        return (listNode)
    
    def nodeIsMatched(self):
        if (self.__firstNode.getIsMatched() == True or self.__secondNode.getIsMatched() == True):
            return (True)
        return (False)
    
    def setBothNodeMatched(self):
        self.__firstNode.setIsMatched(True)
        self.__secondNode.setIsMatched(True)
