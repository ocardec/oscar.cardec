#!/usr/bin/env python
# coding: utf-8

# ## Assignment 12.1

# In[7]:


# The code asumes the following modules have been imported: 
import string
nltk.download('stopwords')
import nltk
from nltk.corpus import stopwords


# In[12]:


# DATA 620 Assignment 12.1
# Writen by: Oscar Cardec
# Semester: SUMMER 2020
# Professor: DR. CARRIE BEAM

# Starter Code -
# Based on Toby Donaldson's Python: Visual QuickStart Guide
# function print_file_stats (location 5347)
#
# Modified by Oscar Cardec
# Last updated: 7 Jul 2020
# Program to open a text file named 'nss2017.txt'
# This program will give a word count of all the words in the file
# and give the top 30 words.

# The code asumes the following modules have been imported: 
# import string
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords

# open file to be analyzed
fhand = open('nss2017.txt', 'r').read()

# count characters 
num_chars = len(fhand)

# count lines 
num_lines = fhand.count('\n')

d = dict()

# split lines and lowercase all words
words = fhand.split()
words = [word.lower() for word in words]

# extra junky or particular words to exclude
words = [word.replace('united','') for word in words]
words = [word.replace('states','') for word in words]
words = [word.replace('also','') for word in words]
words = [word.replace('use','') for word in words]

# filter out punctuation 
words = [word for word in words if word.isalpha()]

# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

# capture word or add count if word is known
for w in words:
    if w in d:    
       d[w] += 1
    else:
       d[w] = 1

num_words = sum(d[w] for w in d)

lst = [(d[w], w) for w in d]
lst.sort()
lst.reverse()

print('Total number of characters = ' + str(num_chars))
print('Total number of lines = ' + str(num_lines))
print('Total number of words = ' + str(num_words))

print('\n The 30 most frequent words are: \n')

i = 1
for count, word in lst[:30]:   
    print('%2s.  %4s %s' % (i, count, word))
    i += 1


# In[ ]:




