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
    __nodeName = None
    __otherData = None
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
    
    
