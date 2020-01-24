##
## node.py for node in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Wed Jan 15 08:27:42 2020 renard_e
## Last update Thu Jan 15 08:27:52 2020 renard_e
##

class Node:
    __isMatched = None
    __nodeName = None
    __otherData = None
    __heuristique = 0
    __listEdge = list()
    
    def __init__(self, nodeName, otherData):
        self.__nodeName = nodeName
        self.__otherData = otherData

    def getNodeName(self):
        return (self.__nodeName)

    def setNodeName(self, nodeName):
        self.__nodeName = nodeName

    def getEdge(self):
        return (self.__listEdge)

    def addEdge(self, newEdge):
        self.__listEdge.append(newEdge)

    def getDataNode(self):
        return (self.__otherData);
    
    def getIsMatched(self):
        return (self.__isMatched)

    def setIsMatched(self, newValue):
        self.__isMatched = newValue

    def countAndSetHeuristique(self):
        self.__heurisitique = len(self.__listEdge)
    
    def getHeuristique(self):
        return (self.__heuristique)
