import re

phrase = "I was born in the year 1994"
phraseReform = "1994 was the year that I was born"

# match only looks at the first pattern in the entire sentence(doesn't look after space)
patternMatch = re.match(r"[a-zA-Z]", phrase)
print(patternMatch)

# the downfall of match is that it only applies to the first element of the entire text(non global)
patternMatchTwo = re.match(r"[a-zA-Z]+", phraseReform)
print(patternMatchTwo)

# search will skip over the characters that don't match the specified pattern and do to where the pettern begins
patternSearch = re.search(r"[a-zA-Z]+", phraseReform)
print(patternSearch)

# check whether text 'starts with' 1994 or not
if re.match(r"^1994", phraseReform):
    print("Match")
else:
    print("No match")

# check whether text 'ends with' born (can just use search also, because search does a global search of the text)
if re.search(r"born$", phraseReform):
    print("Match")
else:
    print("No match")