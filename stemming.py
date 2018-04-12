#stemming-taking the root stem of the word. example: riding-ride

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

example_words=["Python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))
    
example_words=["ride","riding","ridden","rode","rid"]
for w in example_words:
    print(ps.stem(w))

example_text="It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words=word_tokenize(example_text)
for w in words:
    print(ps.stem(w))
   
