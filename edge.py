##
## edge.py for edge in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Wed Jan 15 08:27:18 2020 renard_e
## Last update Thu Jan 15 08:27:28 2020 renard_e
##

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
        return (list(self.__firstNode, self.__secondNode))
        
