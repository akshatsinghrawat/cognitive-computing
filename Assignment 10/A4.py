
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reviews = ["This product is amazing and works flawlessly", "It is not what I expected", "Average quality, nothing special"]
polarities = []
for r in reviews:
    b = TextBlob(r)
    polarities.append(b.sentiment.polarity)

labels = []
for p in polarities:
    if p > 0:
        labels.append("Positive")
    elif p < 0:
        labels.append("Negative")
    else:
        labels.append("Neutral")

pos_text = " ".join([reviews[i] for i in range(len(reviews)) if labels[i] == "Positive"])
wc = WordCloud().generate(pos_text)
plt.imshow(wc)
plt.axis("off")
plt.show()
