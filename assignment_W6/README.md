## Repo description 

The files found in this folder relates to the assignment of W6 (see below). 

The main script at this repo is called network.py

In order to run the scrip you need to create the venv __network_environment__. To do this you download this folder. Then you cd into the folder and run:

'$ bash network_environment.sh'

You then need to activate the environment by running: 

'$ source network_environment/bin/activate'

You can now use the scrip by running: 

'$ python network.py -op output.png -oc output.csv'


The script takes as its input a weighted edgelist which is saved as a CSV with the column headers "nodeA", "nodeB". 

It produces 1) a network plot 2) an output csv with calculated scores for 'betweenness' and 'eigenvector' for each node.

The script has two required arguments (as provided in the example line above):

* output plot file name (-io)
* output csv file name (-oc)

Additionally the script has two optional arguments: 
* weight cutoff (-w)
* input file name (-i)





## Assignment description 

###Assignment 4 - Network analysis


__Creating reusable network analysis pipeline__

This exercise is building directly on the work we did in class. I want you to take the code we developed together and in you groups and turn it into a reusable command-line tool. You can see the code from class here:

https://github.com/CDS-AU-DK/cds-language/blob/main/notebooks/session6.ipynb

This command-line tool will take a given dataset and perform simple network analysis. In particular, it will build networks based on entities appearing together in the same documents, like we did in class.

Your script should be able to be run from the command line
It should take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB"
For any given weighted edgelist given as an input, your script should be used to create a network visualization, which will be saved in a folder called viz.
It should also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. It should save this as a CSV in a folder called output.


Tips
* You should use argparse() in the Python standard library
* Your code should contain a main() function
* Don't worry too much about efficiency - networkx is really slow, there's no way around i!
* If you have issues with pygraphviz, just use the built-in matplotlib functions in networkx.
* You may want to create an argument for the user to define a cut-off point to filter data. E.g. only include node pairs with more than a certain edge weight.
* Make sure to use all of the Python scripting skills you've learned so far, including in the workshops with Kristoffer Nielbo

__General instructions__
* For this assignment, you should upload a standalone .py script which can be executed from the command line
* Save your script as network.py
* You must include a requirements.txt file and a bash script to set up a virtual environment for the project. You can use those on worker02 as a template
* You can either upload the scripts here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line
