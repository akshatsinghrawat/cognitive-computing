import re

text = "Technology is evolving rapidly. Artificial Intelligence is a fascinating area of technology. Many companies invest in AI. It changes how we interact with machines. Machine learning is a key part of AI."

words_more_than_5 = re.findall(r'\b\w{6,}\b', text)
numbers = re.findall(r'\b\d+\b', text)
capitalized = re.findall(r'\b[A-Z][a-z]*\b', text)

alphabetic_words = re.findall(r'\b[a-zA-Z]+\b', text)
vowel_words = [w for w in alphabetic_words if w[0].lower() in 'aeiou']

print(words_more_than_5)
print(numbers)
print(capitalized)
print(alphabetic_words)
print(vowel_words)