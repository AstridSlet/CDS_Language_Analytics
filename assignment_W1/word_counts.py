# ! /usr/bin/python

##### LANGUAGE ANALYTICS ASSIGNMENT 1 #####

# load packages
import os 
from pathlib import Path # for filepaths 
import string # for removing punctuations
import pandas as pd # for creating df 

# create pathname to use in the loop 
filepath = os.path.join("data", "100_english_novels", "corpus")

# check if you reach the files you want in the filepath 
for filename in Path(filepath).glob("*.txt"):
    print(filename)

# create empty list to fill in with the loaded texts 
text_list = []

# create empty list to store file names
fileneame_list = []

# create loop that loads all files into a list - and save the file name of each file in another list
for each_file in Path(filepath).glob("*.txt"):
    with open(each_file, "r", encoding="utf-8") as file:
        file_name = Path(each_file).stem # save just the file name, using the .stem and Path function
        fileneame_list.append(file_name) # append filename to list
        loaded_text = file.read() # load text file
        text_list.append(loaded_text) # append file
        

# create empty list to store word count and unique words count
word_count_list = []
unique_count_list = []

# cleaning the text files and counting words and unique words 
for text in text_list:
    words = text.split() # split text 
    words[0] = '' # removing the first word in each list 
    # remove punctuations
    table = str.maketrans('', '', string.punctuation) 
    stripped = [w.translate(table) for w in words]
    # convert to lower case
    words_clean = [word.lower() for word in stripped]
    word_count_list.append(len(words_clean)) # count words and append the word count to  word_count_list
    unique_count_list.append(len(set(words_clean))) # count unique words (using set() function) and append the word count to unique_count_list

# Save result as a CSV file with three columns: filename, total_words, unique_words

# First gathering the three lists created above in a pandas dataframe
df = pd.DataFrame(zip(fileneame_list, word_count_list, unique_count_list), 
               columns =["filename", "word_count", "unique_words"]) 

# define output path name + output file name  
outpath = os.path.join("output","outputfile.csv")

# save the dataframe in the output folder (using the output path)
df.to_csv(outpath, index=False)


