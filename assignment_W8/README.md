## Repo description 

The files found in this folder relates to the assignment from W8. 

__Research question__
* What topics have dominated the discourse on the topic of vaccination in the past few years?


__Answer__





The main script at this repo is called network.py

In order to run the scrip you need to create the venv __network_environment__. To do this you download this folder. Then you cd into the folder and run:

`$ bash network_environment.sh`

You then need to activate the environment by running: 

`$ source network_environment/bin/activate`

You can now use the scrip by running: 

`$ python network.py -op output.png -oc output.csv`


The script takes as its input a weighted edgelist which is saved as a CSV with the column headers "nodeA", "nodeB". 

It produces 1) a network plot 2) an output csv with calculated scores for 'betweenness' and 'eigenvector' for each node.

The script has two required arguments (as provided in the example line above):

* output plot file name (-io)
* output csv file name (-oc)

Additionally the script has two optional arguments: 
* weight cutoff (-w)
* input file name (-i)


