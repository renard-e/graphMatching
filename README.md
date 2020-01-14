Hi, here is the tutorial for the matchingShell.

How to run it :

       - python3 main.py

Library needed :

       - networkx
       - matplotlib.pyplot
       - csv

First if you never use this shell before you can run it and see how it's work with this command line :

       - python3 main.py < cmdTest.txt

if you want to see which command(s) are on cmdTest.txt you can open it.

Here is the description and the details of the commands :

       - load [name file] - load a dataset (file .csv)
       - print - print champs for the edges
       - select [champs value] - select champs for the edges. example : select 1 2 6 8 9
       - match - to execute match function
       - graph - display graph
       - save [path to the file] - use to save the graph
       - set [champs value] - set wich champ will be the nodes, it must be different from the selected champs for the edge(s). example : set 1
       - limit [value] - limit the number of the node
       - quit - leave the shell

