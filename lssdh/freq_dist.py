import numpy
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

allwords = []
officialstopwords = stopwords.words(english)
