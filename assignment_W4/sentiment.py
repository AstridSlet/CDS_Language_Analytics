# ! /usr/bin/python

from pathlib import Path # for fetching path
import pandas as pd # for creating df 
import numpy as np 
import os
import spacy 
from spacytextblob.spacytextblob import SpacyTextBlob
import matplotlib.pyplot as plt


#create plot function
def plot_func(sentiment_df, window_size, title = "title_string"):
    # make rolling mean
    smooth_sent = sentiment_df.rolling(window_size).mean()
    # get the dates for the x-xis
    x = sentiment_df["date"]
    # create figure
    plt.figure()
    # plot the data
    plt.plot(x, smooth_sent, label="sentiment scores")
    # title of plot
    plt.title(f"{title}")
    # labelling x-axis
    plt.xlabel("date")
    # labelling y-axis
    plt.ylabel("sentiment")
    # rotate x-axis labels
    plt.xticks(rotation=40)
    # add legend
    plt.legend()
    # save figure 
    plt.savefig(os.path.join("output", f"{window_size}_sentiment.png"), bbox_inches='tight')    


# define main function
def main():
    #initialise spaCyTextBlob
    nlp = spacy.load("en_core_web_sm")
    # add it as a new component to our spaCy nlp pipeline
    spacy_text_blob = SpacyTextBlob()
    
    # make path to data
    in_file = os.path.join("data", "abcnews-date-text.csv")
    # load data
    data = pd.read_csv(in_file, nrows = 50000)
    
    # create list for storing polarity scores 
    sentiment_list = []
    mean_sent_list = []
    date_list = []
    group_list = []
    mean_sent_list = []

    # calculate sentiment scores 
    for doc in nlp.pipe(data["headline_text"], batch_size=500):
        sentiment_list.append(doc._.sentiment.polarity)
    # append scores to dataframe 
    data["sent_scores"] = sentiment_list
    # group data by dates 
    grouped = data.groupby("publish_date")
    # create mean for each date 
    for date, group in grouped:
        date_list.append(date)
        group_list.append(group)
    # make each group into a doc 
    for each_group in group_list:
        mean_sent_list.append(each_group["sent_scores"].mean())
    
    # make df
    df = pd.DataFrame(zip(date_list, mean_sent_list), 
                      columns =["date", "mean_sentiment"])
    print(df.head(5))
    #convert to date format
    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
    
    print(df.head(5))
    # make plots and save them
    plot_func(sentiment_df = df, window_size = 7, title = "Seven days rolling average sentiment scores")
    plot_func(sentiment_df = df, window_size = 30, title = "Thirty days rolling average sentiment scores")

    
# Define behaviour when script is called from command line
if __name__=="__main__":
    main()
          
          
