## Repo description 

The files found in this folder relates to the assignment of W10 (see below). 

In order to run the script at this repo you need to create the venv __lang101__. To do this you download this folder. Then you cd into the folder and run:

`$ bash create_lang_venv.sh`

You then need to activate the environment by running: 

`$ source lang101/bin/activate`

You can now run the preprocessing script by running: 

`$ python -W ignore::DeprecationWarning got_cnn.py`

If you wish, you can specify the following arguments: 
* "-i", "--infile", required=False, help="Input path, training data", type = str, default="Game_of_Thrones_Script.csv"
* "-e", "--epochs", required=False, help="Train/test split", type=int, default=10
* "-b", "--batchsize", required=False, help="Batchsize in model training", type=int, default = 32
* -ed", "--embed_dim", required=False, help="Dimensions for storing pretrained word embeddings from glove", type=int, default = 100
*  -ge", "--glove_embedding", required=False, help="Path to the pretrained word embedding to use from glove", type=str, default = "glove/glove.6B.100d.txt"
NB if you want to change this parameter you need to firs unzip the embeding file you want to use in the __glove__ folder. 


The script will train two models using the data set __Game_of_Thrones_Script.csv__ from the data folder: 1) a simple baseline model which uses count vectorization + logistic regression, 2) a CNN which uses pre-trained word embeddings from the folder named glove. 

The model therefore outputs to the output folder:
1. A classification report for the baseline model 
2. A classification report for the cnn model 

Additionally the script outputs
3. A visualization of the cnn model architecture
4. A visualization of the training of the cnn model showing the accuracy/loss after the epochs. 





## Assignment description 

###Assignment 6 - Text classification using Deep Learning


__Text classification using Deep Learning__

Winter is... hopefully over.

In class this week, we've seen how deep learning models like CNNs can be used for text classification purposes. For your assignment this week, I want you to see how successfully you can use these kind of models to classify a specific kind of cultural data - scripts from the TV series Game of Thrones.

You can find the data here: https://www.kaggle.com/albenft/game-of-thrones-script-all-seasons

In particular, I want you to see how accurately you can model the relationship between each season and the lines spoken. That is to say - can you predict which season a line comes from? Or to phrase that another way, is dialogue a good predictor of season?

Start by making a baseline using a 'classical' ML solution such as CountVectorization + LogisticRegression and use this as a means of evaluating how well your model performs. Then you should try to come up with a solution which uses a DL model, such as the CNNs we went over in class.

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
