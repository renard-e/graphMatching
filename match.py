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

class match:
    def makeMatching(self, graph):
        listEdges = graph.getListEdge()
        for edge in listEdges: # probleme ici !!!!!!!!!
            if (edge.firstNode == False and edge.secondNode == False):
                listName = list()
                listName.append(edge.firstNode.getName())
                listName.append(edge.secondNode.getName())
                graph.setUnmatchedToMatched(listName)
        return (True)
