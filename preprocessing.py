from re import sub
import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from typing import List

def preprocess_sentence(sentence: str) -> List[str]:
    """
    This method preprocess removing nonalphanumeric characters, lowers all characters, removes stop words, and punctuation
    """
    sentence = sub("[^A-Za-z0-9]+", " ", sentence)  # also removes special characters since they are not alphanumeric
    sentence = sentence.lower()
    tokens = word_tokenize(sentence)
    words = []
    for token in tokens:
        if token not in stopwords.words("english") and token not in punctuation:
            words.append(token)
    return words