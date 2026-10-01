# Exercise 4.18 - Analyze a different text using NLTK
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

sentence = '''
Ada Lovelace wrote notes about Charles Babbage's Analytical Engine in London.
Her work described how a machine could follow a sequence of instructions.
'''
tokens = nltk.word_tokenize(sentence)
print('Tokens:', tokens)
tagged = nltk.pos_tag(tokens)
print('Part-of-speech tags:', tagged)
entities = nltk.chunk.ne_chunk(tagged)
print('Named entities:', entities)
