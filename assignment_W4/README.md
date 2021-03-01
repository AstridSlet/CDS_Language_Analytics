## Repository description 

The files found at this repo relates to the assignment of W4 (see below). To run the script you need to set up the virtual environment made for this project. To do this you need to download the folder. 

Then in bash you move to the folder and run the command: 

bash create_lang_venv.sh

You should then be able to run the script __sentiment.py__ with the data (a csv file called "abcnews-date-text.csv" placed in the 'data' folder). 
If you are unable to download the data from this repo, the data can also be found at this link: https://www.kaggle.com/therohk/million-headlines

When the script has been run it should produce two plots (which will be placed in the 'output' folder) which shows plots of mean sentiment for the different dates found in the data with a rolling average with a window size of either 7 or 30 days.

NB: the scripts have only been run with a sample of 50.000 headlines as I was a little preassured on time and was unsure of whether I had the time to run the code with all the data. 

## Assignment description 
__Dictionary-based sentiment analysis with Python__

This is a dataset of over a million headlines taken from the Australian news source ABC (Start Date: 2003-02-19 ; End Date: 2020-12-31).


Calculate the sentiment score for every headline in the data. You can do this using the spaCyTextBlob approach that we covered in class or any other dictionary-based approach in Python.
Create and save a plot of sentiment over time with a 1-week rolling average
Create and save a plot of sentiment over time with a 1-month rolling average
Make sure that you have clear values on the x-axis and that you include the following: a plot title; labels for the x and y axes; and a legend for the plot
Write a short summary (no more than a paragraph) describing what the two plots show. You should mention the following points: 1) What (if any) are the general trends? 2) What (if any) inferences might you draw from them?


HINT: You'll probably want to calculate an average score for each day first, before calculating the rolling averages for weeks and months.


__General instructions__

- For this assignment, you should upload a standalone .py script which can be executed from the command line or a Jupyter Notebook
- Save your script as sentiment.py or sentiment.ipynb
- Make sure to include a requirements.txt file and details about where to find the data
- You can either upload the scripts here or push to GitHub and include a link - or both!
- Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line


__Purpose__

This assignment is designed to test that you have a understanding of:
- how to perform dictionary-based sentiment analysis in Python;
- how to effectively use pandas and spaCy in a simple NLP workflow;
- how to present results visually, working with datetime formats to show trends over time




## Summary paragraph 


It is hard to say anything about the 'big' tendencies when simply computing the rolling average over 7 days. In this plot you see a lot of changes in the graph. In the plot with the 30-day rolling average it seems that there are two 'peaks' in sentiment in april 2003 and october 2003. 

