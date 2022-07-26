# Web Scraping

This readme is to explain the process for scraping for contacts, more specifically, emails, phone numbers, names, and job titles.
There consist of 2 files; queryAssembler.ipynb, which requires CCIHE2021-PublicData.csv to get college names, and contactScrape.ipynb which requires blank web_urls.txt to write URLs queried, and queries_good.txt (can be renamed) which consist of the queries written to .txt by the query assembler.

## Methodology

The primary methodology that was attempted was using Stanford NLP Stanza in Python (https://stanfordnlp.github.io/stanza/) which the citation of the original paper can be found below:

Peng Qi, Yuhao Zhang, Yuhui Zhang, Jason Bolton and Christopher D. Manning. 2020. 

Stanza: A Python Natural Language Processing Toolkit for Many Human Languages. 

In Association for Computational Linguistics (ACL) System Demonstrations. 2020.

Code that is left commented out is for the old method and/or testing purposes, and is thoroughly documented as such to assist in reproducibility purposes.

As will be mentioned below, the "old" method refers to NER methods that attempt to find job titles in Stanza, which require more training data from perhaps O*NET (BLS.gov data), etc.
The "new" method is a WIP that refers to capturing contacts from the HTML data for each of the ~4000 colleges, and it uses the BeautifulSoup library to parse the HTML data for the college's webpage.  The BeautifulSoup library is a Python library that can be used to parse HTML data, which is useful for scraping data from websites, available at https://www.crummy.com/software/BeautifulSoup/bs4/doc/. The "new" method is currently being tested and is not yet ready for use. Both of these methods are used in the contactsScrape.ipynb notebook, which each can individually be implemented within what will be called the "giant 'while' loop" cell in order to convey the process of scraping the data.

## Libraries

The libraries that are used consist of the following (make sure you have the correct version of the library, and install them if they are not installed on your machine):

googlesearch: https://pypi.org/project/googlesearch/

requests: https://pypi.org/project/requests/

BeautifulSoup: https://pypi.org/project/beautifulsoup4/

    NavigableString: https://pypi.org/project/beautifulsoup4/

    Tag: https://pypi.org/project/beautifulsoup4/

re: https://pypi.org/project/re/

csv: https://pypi.org/project/csv/

json: https://pypi.org/project/json/

pandas: https://pypi.org/project/pandas/

bs4: https://pypi.org/project/bs4/

numpy: https://pypi.org/project/numpy/

time: https://pypi.org/project/time/

tld: https://pypi.org/project/tld/

stanza: https://stanfordnlp.github.io/stanza/

The libraries that were consulted along the way but were commented out were:

spacy: https://pypi.org/project/spacy/

nltk: https://pypi.org/project/nltk/


## Scraping

How to use "old" method:

1. Make sure the corenlp_server is running.
2. Create empty text file called "web_urls.txt" for storage.
3. Put the queries_good.txt in files folder.    (this is the queries that were written by the queryAssembler.ipynb notebook)
4. Run the giant "while" loop down below (right before the post-processing), type "y", then "n" in the prompt in order to begin scraping. The "while" loop will continue to run until the user types "n".
6. Run the final post-processing cells export to contacts.csv. This will take the scraped data and write it to a .csv file.

How to use "new" method:
1. Create empty text file called "web_urls.txt" for storage of the URLs that were scraped.
2. Put the queries_good.txt in files folder (this is the queries that were written by the queryAssembler.ipynb notebook).
3. Run defined methods that allows for scraping contact HTML data.      (WIP) 
4. Run the giant "while" loop down below (right before the post-processing), type "y", then "n" in the prompt in order to begin scraping the data. The "while" loop will continue to run until the user types "n".
5. Save output.csv to local computer or drive (if you have one). This will take the scraped data and write it to a .csv file.

## Reflections

The "old" method was put aside for working on the "new" method, and is not fully functional in terms of satisfactory information extraction. The main reason for this is that the NER methods that are used in Stanza are not fully trained on the data that we seek to extract from the HTML, therefore the model will sometimes not be able to extract the correct names and titles. However, it is almost always able to extract emails from the HTML.

The "new" method is also a work in progress, as well, because there are certain inconsistencies in the HTML data that we are unable to account for in the scraping process. For example, the HTML data for each college is not consistent in the way that it is structured, leading to some issues that are not easily resolved in the scraping process using the BeautifulSoup library.