import nltk
from nltk.corpus import treebank
nltk.download('punkt')
sentence = """ Dread it, run from it Destiny still arrives
... Or I am Destiny."""
tokens=nltk.word_tokenize(sentence)
print(tokens)
tagged=nltk.pos_tag(tokens)
print(tagged[0:6])
entities=nltk.chunk.ne_chunk(tagged)
print(entities)
t=treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
