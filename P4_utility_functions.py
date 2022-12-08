""" File:  P4_utility_functions.py  

    Description:  Utility functions to perform NER

"""

#Import the necessary packages
import os.path
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk import Tree
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet

def createCorpusTextFileFromData(data, fileName):
    """ Create a text file from data and save it as fileName. """
    corpusFile = open(fileName, 'w')
    for line in data['Transcript']:
        corpusFile.write(line + " ")
    corpusFile.close()

def perform_NER(corpus):
    """ Perform Named Entity Recognition (NER) on a corpus of text. """
    #Tokenize the corpus of text
    tokenized_corpus = word_tokenize(corpus)
    #Tag the tokenized corpus of text
    tagged_corpus = pos_tag(tokenized_corpus)
    #Perform NER on the tagged corpus of text
    named_entities = ne_chunk(tagged_corpus)
    #Return the named entities
    return named_entities