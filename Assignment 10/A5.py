
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np

text = "Technology is evolving fast. New innovations emerge every year. Artificial Intelligence is growing rapidly. Machine learning helps systems improve."

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
seqs = tokenizer.texts_to_sequences([text])[0]
inp = []
for i in range(1, len(seqs)):
    inp.append(seqs[:i+1])

inp = np.array(pad_sequences(inp, padding='pre'))
X, y = inp[:, :-1], inp[:, -1]

model = Sequential()
model.add(Embedding(len(tokenizer.word_index)+1, 10, input_length=X.shape[1]))
model.add(LSTM(50))
model.add(Dense(len(tokenizer.word_index)+1, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(X, y, epochs=100, verbose=0)

seed = "Technology"
seq = tokenizer.texts_to_sequences([seed])[0]
for _ in range(3):
    pad_seq = pad_sequences([seq], maxlen=X.shape[1], padding='pre')
    pred = model.predict(pad_seq, verbose=0).argmax()
    seq.append(pred)
inv_map = {v: k for k, v in tokenizer.word_index.items()}
print(" ".join([inv_map.get(i, "") for i in seq]))
