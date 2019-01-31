import re

x = ["This is a wolf #scary",
     "Welcome to the jungle #missing",
     "11322 the number to know",
     "Remember the name s - John",
     "I        have        you",]

for i in range(len(x)):
    # remove non word characters
    x[i] = re.sub(r"\W", " ", x[i])
    # remove digits
    x[i] = re.sub(r"\d", "", x[i])
    # remove single letters that are not 'a' or 'i'
    x[i] = re.sub(r"\s+[b-hj-z]\s+", " ", x[i], flags=re.I)
    # remove extra spaces
    x[i] = re.sub(r"\s+", " ", x[i])
    # remove space at beginning of sentence
    x[i] = re.sub(r"^\s", "", x[i])
    # remove space at the end of sentence
    x[i] = re.sub(r"\s$", "", x[i])
    print(x[i])