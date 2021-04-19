#!/usr/bin/env python

"""
Predicting season of GOT from sentences from the manuscripts using tensorflow.keras.

"""
# system tools
import os
import sys

# pandas, numpy, gensim
import pandas as pd
import numpy as np
import gensim.downloader


# language tools
import spacy
nlp = spacy.load("en_core_web_sm")


# utility functions 
from got_utils import load_data
from got_utils import one_hot
from got_utils import train_network
from got_utils import model_structure_viz
from got_utils import plot_train_hist
from got_utils import evaluate_model
from got_utils import base_model
from got_utils import create_embedding_matrix
from got_utils import prepro_cnn



# parsing arguments
import argparse


def main():
    print("\n[INFO] Initialising analysis...")
    
    # Initialise argumentparser
    ap = argparse.ArgumentParser()
    
    # Define arguments
    ap.add_argument("-i", "--infile", required=False, help="Input path, training data", type = str, default="Game_of_Thrones_Script.csv")
    ap.add_argument("-e", "--epochs", required=False, help="Train/test split", type=int, default=10)
    ap.add_argument("-b", "--batchsize", required=False, help="Batchsize in model training", type=int, default = 32)
    ap.add_argument("-ed", "--embed_dim", required=False, help="Dimensions for storing pretrained word embeddings from glove", type=int, default = 50)
    ap.add_argument("-ge", "--glove_embedding", required=False, help="Path to the pretrained word embedding to use from glove", type=str, default = "glove/glove.6B.50d.txt")


    # Parse arguments to args
    args = vars(ap.parse_args())
    
    # fetch args
    epochs = args["epochs"]
    batch_size = args["batchsize"]
    path_to_glove_embedding = args["glove_embedding"]
    embedding_dim = args["embed_dim"]

    
    # define input filepath 
    infile = os.path.join("data", args["infile"])

    # load train and validation set
    X_train, X_test, y_train, y_test, label_names = load_data(infile)

    print("\n[INFO] Train baseline model...")
    # train baseline model 
    y_pred_basemodel = base_model(X_train, X_test, y_train)
    
    
    # make labels onehot encoding for the cnn
    trainY = one_hot(y_train)
    testY = one_hot(y_test)
    
    # make data ready for the cnn  
    X_train_pad, X_test_pad, vocab_size, embedding_matrix, maxlen = prepro_cnn(X_train, X_test, embedding_dim, path_to_glove_embedding)
    
    print("\n[INFO] Train CNN model...")
    # train cnn network and get training history
    cnn_model, y_pred_cnn, cnn_history = train_network(X_train_pad, trainY, X_test_pad, testY, batch_size, epochs, vocab_size, embedding_matrix, maxlen, embedding_dim)
    
    # make visualization of the model architecture
    model_structure_viz(cnn_model)
    
    # create visualization of training history
    plot_train_hist(H = cnn_history, epochs=epochs)
    
    
    #### EVALUATE MODELS ####
    print("\n[INFO] Evaluate models...")
    # create classification report basemodel 
    evaluate_model(y_test, y_pred_basemodel, label_names, "clf_basemodel")
    
    # create classification report CNN
    evaluate_model(testY.argmax(axis = 1), y_pred_cnn.argmax(axis = 1), label_names, "clf_CNN")
    
    print("\n[INFO] ALL DONE!")
# define behaviour from command line 
if __name__=="__main__":
    main()
    
 
    
    
    
    
    
    