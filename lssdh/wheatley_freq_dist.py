import numpy
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

allwords = []
officialstopwords = stopwords.words('english')
additionalstopwords = ["thou", "thine", "'", ".", ";", ":", "'s", ",", "thy",
                       "?", "th", "'d", "thus"]

allstopwords = officialstopwords + additionalstopwords

with open('texts/phillis-wheatley.txt') as input:
    book_lines = input.readlines()

for line in book_lines:
    words = word_tokenize(line)
    for w in words:
        w = w.lower()
        if w not in allstopwords:
            allwords.append(w)


freqdist = nltk.FreqDist(allwords)
plt.figure(figsize=(16,5))
freqdist.plot(50)
