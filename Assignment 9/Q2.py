import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer

words = ['technology', 'evolving', 'rapidly', 'artificial', 'intelligence', 'fascinating', 'area', 'companies', 'invest', 'changes', 'interact', 'machines', 'machine', 'learning', 'key', 'part']

porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

porter_stemmed = [porter.stem(w) for w in words]
lancaster_stemmed = [lancaster.stem(w) for w in words]
lemmatized = [lemmatizer.lemmatize(w) for w in words]

print(porter_stemmed)
print(lancaster_stemmed)
print(lemmatized)