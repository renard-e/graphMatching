##
## lexer.py for lexer in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Sat Jan 11 10:34:56 2020 renard_e
## Last update Sun Jan 11 10:35:02 2020 renard_e
##

from loader import Loader

class Lexer:
    __cmd = {}
    __loader = Loader()
    __dataFromDataSet = list()
    __listChampsForEdge = list()
    __nodeSelected = None
    __limitNode = None
    
    def __init__(self):
        self.__cmd = {"load" : self.loadFunc,
                    "print" : self.printFunc,
                    "select" : self.selectFunc,
                    "match" : self.matchFunc,
                    "graph" : self.graphFunc,
                    "save" : self.saveFunc,
                    "set" : self.setFunc,
                    "limit" : self.limitFunc}
        
    def makeChoice(self, line):
        line_cmd = line.split(' ')
        if (line_cmd[0] in self.__cmd):
            self.__cmd[line_cmd[0]](line_cmd)
        else:
            print("Error : Invalid command. try --help or -h to print the valid command")

    def loadFunc(self, line_cmd):
        if (len(line_cmd) >= 2):
            self.__dataFromDataSet.clear()
            self.__listChampsForEdge.clear()
            self.__selectedNode = None
            self.__dataFromDataSet = self.__loader.loadDataFromFile(line_cmd[1])
            if (len(self.__dataFromDataSet) > 0):
                print("Data set", line_cmd[1], "loaded")
        else:
            print("Error : load invalid arguments.")

    def printFunc(self, line_cmd):
        if (len(self.__dataFromDataSet) != 0):
            for cpt in range(len(self.__dataFromDataSet[0])): 
                print (cpt, end = " - ") 
                print (self.__dataFromDataSet[0][cpt])
        else:
            print("Error : no data set is loaded")

    def selectFunc(self, line_cmd):
        if (len(line_cmd) >= 2):
            if (len(self.__dataFromDataSet) != 0):
                cpt = 1
                while (cpt < len(line_cmd)):
                    if (line_cmd[cpt].isdigit()
                        and int(line_cmd[cpt]) <= len(self.__dataFromDataSet[0]) - 1
                        and not (line_cmd[cpt] in self.__listChampsForEdge)
                        and (self.__selectedNode == None or line_cmd[cpt] != self.__selectedNode)):
                        self.__listChampsForEdge.append(line_cmd[cpt])
                    cpt += 1
            else:
                print("Error : no data set is loaded")
        else:
            print("Error : bad argument(s) for select edges")

    def matchFunc(self, line_cmd):
        print("MATCH FUNCTION")

    def graphFunc(self, line_cmd):
        #check if le node est different des edges
        print("GRAPH FUNCTION")

    def saveFunc(self, line_cmd):
        print("SAVE FUNCTION")

    def setFunc(self, line_cmd):
        if (len(line_cmd) >= 2):
            if (len(self.__dataFromDataSet) != 0):
                if (line_cmd[1].isdigit() and (not line_cmd[1] in self.__listChampsForEdge) and int(line_cmd[1]) <= len(self.__dataFromDataSet[0]) - 1 ):
                    self.__selectedNode = line_cmd[1]
                else:
                    print("Error : bad argument for set a node")
            else:
                print("Error : no data set is loaded")
        else:
            print("Error : set bad argument(s)")            
        
    def limitFunc(self, line_cmd):
        if (len(line_cmd) >= 2):
            if (line_cmd[1].isdigit()):
                self.__limitNode = int(line_cmd[1])
                print("limit set to ", line_cmd[1])
            else:
                print("Error : limit need to be a number")
        else:
            print("Error : bad argument(s)")
