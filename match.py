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
        listEdges = graph.getListEdge()
        for edge in listEdges:
            if (edge.nodeIsMatched() == False):
                graph.setUnmatchedToMatched(edge.getNodes())
                edge.setBothNodeMatched()
        return (True)
