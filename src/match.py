##
## match.py for match in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Thu Jan 9 13:56:24 2020 renard_e
## Last update Fri Jan 9 13:56:37 2020 renard_e
##

from build_graph import GGraph
from edge import Edge
from node import Node

class match:
    def makeMatching(self, graph):
        listEdges = self.findTheBestWay(graph)
        for edge in listEdges:
            if (edge.nodeIsMatched() == False):
                graph.setUnmatchedToMatched(edge.getNodes())
                edge.setBothNodeMatched()
        return (True)

    def findTheBestWay(self, graph):
        listNodes = graph.getListNodes()
        
        for node in listNodes:
            self.setCorrectHeuristiqueValue(node)
        return (self.calculatHeuristiqueForEdge(graph.getListEdge()))
        
    def setCorrectHeuristiqueValue(self, node):
        node.countAndSetHeuristique()

    def calculatHeuristiqueForEdge(self, listEdges):
        for edge in listEdges:
            heuristiqueFirstNode = edge.getFirstNode()
            heuristiqueSecondNode = edge.getSecondNode()
            edge.setHeuristiqueSum(heuristiqueFirstNode.getHeuristique(), heuristiqueSecondNode.getHeuristique())
        return (self.triEdgeByHr(listEdges))

    def triEdgeByHr(self, listEdges):
        change = True
        while (change == True):
            change = False
            cpt = 0
            while (cpt <= len(listEdges) - 2):
                if (listEdges[cpt].getHeuristiqueSum() < listEdges[cpt + 1].getHeuristiqueSum()):
                    tmpEdge = listEdges[cpt]
                    listEdges[cpt] = listEdges[cpt + 1]
                    listEdges[cpt + 1] = tmpEdge
                    change = True
                cpt += 1
        return (listEdges)
