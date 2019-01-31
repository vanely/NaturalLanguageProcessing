import nltk
import re

filteredStory = []
with open("shortStory", "r") as f:
    sentences = nltk.sent_tokenize(f.read())
    for sent in range(len(sentences)):
        sentences[sent] = re.sub(r"[\d]", "", sentences[sent])
        filteredStory.append(sentences[sent])


with open("shortStoryEdit.txt", "w") as f:
    for sent in range(len(filteredStory)):
        f.write(filteredStory[sent] + "\n")
