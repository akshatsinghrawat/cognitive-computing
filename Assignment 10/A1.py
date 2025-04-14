
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

text = "Books open up new worlds. Reading improves vocabulary and knowledge. Many people enjoy fiction. Non-fiction is also popular. Libraries offer free access to books."

t = re.sub(r'[^a-zA-Z\s]', '', text.lower())
words = re.findall(r'\b[a-zA-Z]+\b', t)
stop_words = set(stopwords.words('english'))
filtered = [w for w in words if w not in stop_words]

ps = PorterStemmer()
lem = WordNetLemmatizer()
stemmed = [ps.stem(w) for w in filtered]
lemmatized = [lem.lemmatize(w) for w in filtered]
print(stemmed)
print(lemmatized)
