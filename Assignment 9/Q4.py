import re

text = "Contact us at example@example.com or visit https://example.com. For support, call +91 9876543210. This is a state-of-the-art technology. It isn't just hype. The value is 3.14."

def custom_tokenize(text):
    text = re.sub(r'[^\w\s\.-]', '', text)
    tokens = re.findall(r"\b\d+\.\d+\b|\b\w+(?:-\w+)*\b", text)
    return tokens

text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '<EMAIL>', text)
text = re.sub(r'https?://\S+|www\.\S+', '<URL>', text)
text = re.sub(r'\+\d{1,3} \d{10}|\d{3}-\d{3}-\d{4}', '<PHONE>', text)

tokens = custom_tokenize(text)
print(tokens)
print(text)