import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

text = "Technology is evolving rapidly. Artificial Intelligence is a fascinating area of technology. Many companies invest in AI. It changes how we interact with machines. Machine learning is a key part of AI."

text = text.lower().translate(str.maketrans('', '', string.punctuation))
words = word_tokenize(text)
sentences = sent_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]
freq_dist = Counter(filtered_words)
print(freq_dist)