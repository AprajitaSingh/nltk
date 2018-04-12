#Lemmatizing-A very similar operation to stemming is called lemmatizing. The major difference between these is stemming can often create non-existent words, whereas lemmas are actual words.

from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))

print(lemmatizer.lemmatize("ride",pos="v"))
print(lemmatizer.lemmatize("riding",pos="v"))
print(lemmatizer.lemmatize("better",pos="a"))