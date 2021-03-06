#Chinking is a lot like chunking, it is basically a way for you to remove a chunk from a chunk. The chunk that you remove from your chunk is your chink

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text=state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")
print(train_text)
print(sample_text)

custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
tokenized=custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram=r"""Chunk:{<.*>+} 
                                }<VB.?|IN|DT>+{"""
                                
            ChunkParser=nltk.RegexpParser(chunkGram)
            chunked=ChunkParser.parse(tagged)
            chunked.draw()
            
        except Exception as e:
            print(str(e))