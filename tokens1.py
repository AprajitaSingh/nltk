#tokenizing- word tokenizer, sentence tokenizer
#corpora-body of text. e.g medical journal, anything in english language
#lexicon- word, meanings

from nltk.tokenize import sent_tokenize, word_tokenize
example_text="Hello Mr. Smith! How are you doing today? The weather is great and Python is awesome. The sky is blue. You should not eat cardboard.
print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
    
a=word_tokenize(example_text)
print(a[6])