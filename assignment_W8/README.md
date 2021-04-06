## Repo description 

The files found in this folder relates to the assignment of W8 (see below). 

__Research question:__

* Which topics have played a significant role in the debate on vaccinations in the past years?

To investigate this question I have downloaded a data set from kaggle which is constituted by all tweets containing the string 'vaccination' from the year 2006 to 30th of November 2019. The data set, which is also placed in the data folder, can be found here: https://www.kaggle.com/keplaxo/twitter-vaccination-dataset

If you want to redo this analysis you need to download the data from kaggle set and place the data subset called 'vaccination2.csv' in the data folder of this repo. 


__Answer to research question:__
In textfile final_output.txt it seems that five dominant topics have been prevalent on the topic of vaccines in the past years. Examples of interesting topics is topic 0 and topic 1.
Topic 0 seems to be related to the HPV vaccine with words like "hpv", "women", "girl" and "age". 
Topic 1 seems to be related to whether vaccines should be mandatory with words like "anti","force", "mandatory" and "issue"'),
When looking at the plot (topics_over_time.jpg) in the out folder it seems that topic no 1 is relative prevalent in the discussion at all times. And then topic no 1 is not as prevalent but there are some distinct spikes in the blue line at some points. 

I have not managed to put dates on the x-axis. Right now the tweets are ordered by date before they are made into chunks which means that the plot should show the development in the topic prevalence over time... but I would like to work more on the line plot and maybe put some date time stamps at least at some poinst of the x-axis. 


__Work flow__

To investigate the research question I used unsupervised machine learning (latent dirichlet allocation). In order to run the analysis I also created a script for preprocessing twitter data.

There are therefore two scripts at this repo: 
* preproc.py (for prerprocessing)
* LDA_model.py (for topic modelling) 

In order to run the scripts you need to create the venv __lang101__. To do this you download this folder. Then you cd into the folder and run:

`$ bash create_lang_venv.sh`

You then need to activate the environment by running: 

`$ source lang101/bin/activate`

You can now run the preprocessing script by running: 

`$ python preproc.py`

This will produce a preprocessed version of the sample data __vaccination2.csv__ from the data folder, which will also be placed in the data folder. 

You can now run the topic modelling on this preprocessed data set by running: 

`$ python -W ignore::DeprecationWarning LDA_model.py`

The model first tries to find the optimal number of topics based on coherence score. 
The model therefore outputs to the out folder:
1. A visualization in the out folder of different no. of topics and their coherence score. 
2. A textfile with the coherence scores for different no. of topics. 

The script automatically chooses the number of topics which gives the highest coherence score and trains a model. 
This model training will produce: 
1. A plot of the different topics prevalence over time. 
2. A textfile with the number of topics, the coherence and perplexity score and the different topics. 




## Assignment description 

###Assignment 5 - (Un)supervised machine learning


__Creating reusable network analysis pipeline__

Applying (un)supervised machine learning to text data

The assignment this week involves a little bit of a change of pace and a slightly different format. As we have the Easter break next week, you also have a longer period assigned to complete the work.

For this task, you will pick your own dataset to study.

This dataset might be something to do with COVID-19 discourse on Reddit; IMDB reviews; newspaper headlines; whatever it is that catches your eye. However, I strongly recommend using a text dataset from somewhere like Kaggle - https://www.kaggle.com/datasets

When you've chosen the data, do one of the following tasks. One of them is a supervised learning task; the other is unsupervised.

EITHER

Train a text classifier on your data to predict some label found in the metadata. For example, maybe you want to use this data to see if you can predict sentiment label based on text content.

OR

Train an LDA model on your data to extract structured information that can provide insight into your data. For example, maybe you are interested in seeing how different authors cluster together or how concepts change over time in this dataset.


You should formulate a short research statement explaining why you have chosen this dataset and what you hope to investigate. This only needs to be a paragraph or two long and should be included as a README file along with the code. E.g.: I chose this dataset because I am interested in... I wanted to see if it was possible to predict X for this corpus.

In this case, your peer reviewer will not just be looking to the quality of your code. Instead, they'll also consider the whole project including choice of data, methods, and output. Think about how you want your output to look. Should there be visualizations? CSVs?

You should also include a couple of paragraphs in the README on the results, so that a reader can make sense of it all. E.g.: I wanted to study if it was possible to predict X. The most successful model I trained had a weighted accuracy of 0.6, implying that it is not possible to predict X from the text content alone. And so on.


Tips
* Think carefully about the kind of preprocessing steps your text data may require - and document these decisions!
* Your choice of data will (or should) dictate the task you choose - that is to say, some data are clearly more suited to supervised than unsupervised learning and vice versa. Make sure you use an appropriate method for the data and for the question you want to answer
* Your peer reviewer needs to see how you came to your results - they don't strictly speaking need lots of fancy command line arguments set up using argparse(). You should still try to have well-structured code, of course, but you can focus less on having a fully-featured command line tool

__General instructions__
* For this assignment, you should upload a standalone .py script which can be executed from the command line
* Save your script as network.py
* You must include a requirements.txt file and a bash script to set up a virtual environment for the project. You can use those on worker02 as a template
* You can either upload the scripts here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line
=======
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
