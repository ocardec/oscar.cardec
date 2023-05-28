## Text Analysis with NLTK and Tableau Visualizations

As a Data Analyst, BI Analyst, Data Miner, ML Engineer, etc. text analysis could result in one of the handiest tools of your toolbox. In simple words, text analysis is about parsing a string or text file with the objective of extracting key characteristics, facts, or trends from within the context.
 
>"Using Text Analysis is one of the first steps in many data-driven approaches, as the process extracts machine-readable facts from large bodies of texts and allows these facts to be further entered automatically into a database or a spreadsheet. The database or the spreadsheet are then used to analyze the data for trends, to give a natural language summary, or may be used for indexing purposes in Information Retrieval applications" - ontotext.com

**Example:**
*Given unstructured text data, process the data, and create valuable business analytics. Create a managerial report identifying the patterns and recommendations uncovered in the data.*

You want to choose readily available text which recurred over at least three time periods, spaced some distance apart. You want to make sure you have at least several thousand words of text for each time period, and you want something which will change noticeably over that time period.
For this example, I've selected the U.S. National Security Strategy for the years of 1996, 2002, and 2017.

>Text analysis is about parsing a string or text file with the objective of extracting characteristics, facts, or trends from the context.
    
**1st Step:** Open the text file (ie., nss1996.txt), create basic counters, and dictionary, split the lines as words, and lowercase all contained words. 

**Note:** Starter Code - Based on Toby Donaldson's Python: Visual QuickStart Guide function print_file_stats (location 5347). Modified by OC on 7 Jul 2020
Program to open a text file named 'nss1996.txt' give a word count of all the words in the file and give the top 30 words. Note: This code assumes the following have been imported:

- import string
- import nltk
- nltk.download('stopwords')
- from nltk.corpus import stopwords

      fhand = open('nss1996.txt', 'r').read()   #open the file
      num_chars = len(fhand)                    #count characters 
      num_lines = fhand.count('\n')             #count lines
      d = dict()                                #create a list
      words = fhand.split()                     #split lines
      words = [word.lower() for word in words]  #lowercase words
      

#### Click [HERE](https://nbviewer.org/github/ocardec/oscar.cardec/blob/main/text_analysis/text_analysis_w_NLTK.ipynb) to read the rest. 
