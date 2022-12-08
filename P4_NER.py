""" File:  P3_NER.py  

    Description: Function to perform Named Entity Recognition (NER) on a corpus of text.
"""

from P4_utility_functions import *
import pandas as pd

def main():
    data = pd.read_csv("data.csv") #TO-DO:  Change this to the name of your data file
    corpus = createCorpusTextFileFromData(data, "corpus.txt") #keep the text file out of the repository!!!!!!!!!!!!!!!!!

    #Perform NER on the corpus of text
    named_entities = perform_NER(corpus)

    #Print the named entities
    print(named_entities)

if __name__ == '__main__':
    main()