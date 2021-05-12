import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud


text = open('texts/phillis-wheatley.txt').read()

# Stopwords file
officialstopwords = stopwords.words('english')
additionalstopwords = ["thy", "thou", "ye"]

allstopwords = officialstopwords + additionalstopwords

# Word Cloud attributes
wc = WordCloud(
         width=600, height=300,
         background_color="white",
         max_words=5000,
         stopwords=allstopwords,
         max_font_size=60,
         min_font_size=6,
         random_state=80
         )

# Generate Word Cloud
wc.generate(text)

# Show Word Cloud
plt.figure(figsize=(20,10))
plt.imshow(wc)
plt.axis("off")
plt.show()


