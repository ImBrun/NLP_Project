from re import sub
import pandas as pd
import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from typing import List
from gensim.utils import lemmatize
import csv

# slang_data = {}
# with open("./slang_dict.csv",'r') as exRtFile:
#     exchReader = csv.reader(exRtFile,delimiter='`',quoting=csv.QUOTE_NONE)
#     for row in exchReader:
#         if(len(row) > 1):
#             slang_data[row[0].lower()] = row[1].split('|')[0].lower()

# typos_list = {}
# with open("./typos.txt",'r') as exRtFile:
#     exchReader = csv.reader(exRtFile,delimiter='\t',quoting=csv.QUOTE_NONE)
#     for row in exchReader:
#         typos_list[row[0]] = row[1]

def preprocess_sentence(sentence: str) -> List[str]:
    """
    This method preprocess removing nonalphanumeric characters, lowers all characters, removes stop words, and punctuation
    """
    print("sentence: ", sentence)
    sentence = sub("[^A-Za-z0-9]+", " ", sentence)  # also removes special characters since they are not alphanumeric
    sentence = sentence.lower()
    tokens = word_tokenize(sentence)
    words = [lemmatize(token) for token in tokens if token not in stopwords.words("english") and token not in punctuation and token.isalpha()]
    lem_words = []
    for item in words:
        if(len(item)>0):
            lem_words.append(item[0].decode("utf-8-sig"))
    processed_words = separate_word_tag(lem_words)
    print(processed_words)
    return processed_words

def separate_word_tag(df_lem_test):
    words=[]
    for word in df_lem_test:
        sent = []
        split = word.split('/')
        sent.append(split[0])
        words.append(' '.join(word for word in sent))
    return words


