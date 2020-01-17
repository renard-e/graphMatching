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
    isMatched = False
    firstNode = None
    secondNode = None
    
    def __init__(self, firstNode, secondNode):
        self.firstNode = firstNode
        self.secondNode = secondNode

    def setIsMatched(self, newValue):
        self.isMatched = newValue

    def getIsMatched(self):
        return (self.isMatched)

    def getNodes(self):
        listNode = list()
        
        listNode.append(self.firstNode.getNodeName())
        listNode.append(self.secondNode.getNodeName())
        return (listNode)
    
    def nodeIsMatched(self):
        if (self.firstNode.getIsmatched() == True or self.secondNode.isMatched() == True):
            return (True)
        return (False)
    
    def setBothNodeMatched(self):
        self.firstNode.setIsMatched(True)
        self.secondNode.setIsMatched(True)
