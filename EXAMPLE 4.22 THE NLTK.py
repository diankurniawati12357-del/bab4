# Example 4.22 - NLTK text analysis
# Requires NLTK and its maxent_ne_chunker and words data packages.
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

sentence = '''
Artificial intelligence uses computer systems to perform tasks that often
require human intelligence, including learning and problem solving.
'''
tokens = nltk.word_tokenize(sentence)
print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged)

entities = nltk.chunk.ne_chunk(tagged)
print(entities)
