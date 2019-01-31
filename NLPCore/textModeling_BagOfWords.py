import nltk
from collections import Mapping, defaultdict

sentence1 = "It is going to rain today"
sentence2 = "Today I am not going outside"
sentence3 = "I am going to watch the season premiere"

# tokenize sentences
words1 = nltk.word_tokenize(sentence1)
words2 = nltk.word_tokenize(sentence2)
words3 = nltk.word_tokenize(sentence3)

# for histogram of frequency of tokenized words
# check how many different words are present in the text being used
# check how often each word appears in tge text
# the two previous steps result in a bag of words