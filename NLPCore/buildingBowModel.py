import nltk
import re
import heapq
import numpy as np
# nltk.download()
paragraph = """Thank you all so very much. Thank you to the Academy. 
              Thank you to all of you in this room. I have to congratulate 
              the other incredible nominees this year. The Revenant was the product of 
              the tireless efforts of an unbelievable cast and crew. First off, to my 
              brother in this endeavor, Mr. Tom Hardy. Tom, your talent on screen can only 
              be surpassed by your friendship off screen … thank you for creating a 
              transcendent cinematic experience. Thank you to everybody at Fox and New 
              Regency … my entire team. I have to thank everyone from the very onset of my 
              career … To my parents; none of this would be possible without you. And to my 
              friends, I love you dearly; you know who you are.
              And lastly, I just want to say this: Making The Revenant was about man's 
              relationship to the natural world. A world that we collectively felt in 2015 
              as the hottest year in recorded history. Our production needed to move to the 
              southern tip of this planet just to be able to find snow. Climate change 
              is real, it is happening right now. It is the most urgent threat facing our 
              entire species, and we need to work collectively together and stop 
              procrastinating. We need to support leaders around the world who do not speak 
              for the big polluters, but who speak for all of humanity, for the indigenous 
              people of the world, for the billions and billions of underprivileged people 
              out there who would be most affected by this. For our children’s children, 
              and for those people out there whose voices have been drowned out by the 
              politics of greed. I thank you all for this amazing award tonight. Let us not 
              take this planet for granted. I do not take tonight for granted. 
              Thank you so very much.
              """

sentences = nltk.sent_tokenize(paragraph)

# wordsArr = []
for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub(r"\W", " ", sentences[i])
    sentences[i] = re.sub(r"\s+", " ", sentences[i])
    # wordsArr.append(words)

# Histogram(frequency of each word)
wordToCount = {}
for sent in sentences:
    words = nltk.word_tokenize(sent)
    for word in words:
        # if the word that was just come across has not been encountered before
        if word not in wordToCount.keys():
            # word is appended to wordToCount as a key with a value of 1
            wordToCount[word] = 1
        else:
            wordToCount[word] += 1

# used to create an array of the 100 most frequent of the wordToCount
freq_words = heapq.nlargest(100, wordToCount, key=wordToCount.get)

#will contain bag of words model
# documents will be represented as vectors of length 100(our top frequent words)
# if word appears, it is a 1, if not it is a 0
X = []

for sent in sentences:
    # for each iteration vector will contain all day pre sentence
    vector = []
    for word in freq_words:
        # if frequent word is in one of the sentences we add 1 to the vector else we add a 0
        if word in nltk.word_tokenize(sent):
            vector.append(1)
        else:
            vector.append(0)
    # append the vector for every sentence into X making it a multidimensional list of word appearences
    X.append(vector)

# use numpy to covert X into a 2Darray
X = np.array(X)
# print(wordToCount)
# print(freq_words)
print(X)