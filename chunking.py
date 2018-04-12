#Chunking is also called shallow parsing and it's basically the identification of parts of speech and short phrases (like noun phrases)
#An example of when chunking might be preferable is Named Entity Recognition. In NER, your goal is to find named entities, which tend to be noun phrases (though aren't always).

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
            
            chunkGram=r"""Chunk:{<RB.?>*<VB.?>*<NNP>+<NN>} """
            ChunkParser=nltk.RegexpParser(chunkGram)
            chunked=ChunkParser.parse(tagged)
            chunked.draw()
            
        except Exception as e:
            print(str(e))