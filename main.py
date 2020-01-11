##
## main.py for main in /home/renard_e/Documents/algo_matching/graphMatching
##
## Made by renard_e
## Login   <renard_e>
##
## Started on  Fri Jan 10 16:24:42 2020 renard_e
## Last update Sat Jan 10 16:27:12 2020 renard_e
##

from lexer import Lexer
def print_help():
    print("\tload [name file] - load a dataset (file .csv)")
    print("\tprint - print champs for the edges")
    print("\tselect [champs value] - select champs for the edges. example : select 1 2 6 8 9")
    print("\tmatch - to execute match function")
    print("\tgraph - display graph")
    print("\tsave [path to the file] - use to save the graph")
    print("\tset [champs value] - set wich champ will be the nodes, it must be different from the selected champs for the edge(s). example : set 1")
    print("\tlimit [value] - limit the number of the node")
    print("\tquit - leave the shell")

lexer = Lexer()
print("Hello welcome to the shell of matching ! type --help for command list")
while (True):
    line = input("$> ")
    if (line == "--help" or line == "-h"):
        print_help()
    elif (line == "quit" or line == "exit"):
        exit(1)
    else:
        lexer.makeChoice(line)
    
