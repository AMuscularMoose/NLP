from textblob import TextBlob
import nltk

#nltk.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

print(blob.word_counts["juliet"])
print(blob.word_counts["romeo"])
print(blob.word_counts["thou"])
print(blob.word_counts["joy"])
print(blob.noun_phrases.count("lady capulet"))

stops = stopwords.words("english")


items = blob.word_counts.items()


items = [item for item in items if item not in stops]


print(items[:10])



from operator import itemgetter

sorted_items = sorted(items)


sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

import matplotlib






from pathlib import Path
from wordcloud import WordCloud
import imageio

text = Path("RomeoAndJuliet.txt").read_text()
#print(text)

mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

plt.imshow(wordcloud)
print("Done")