import re

phrase = "I love horror movies"
phraseTwo = "I love love love horror movies"

# substitutes a part of a text with an other, very much like a replace function
print(re.sub(r"horror movies", "stand up comedies", phrase))

# NOTE: sub will substitute every occurrence of the text being replaced(global search/ global replace)
print(re.sub(r"love", "adore", phraseTwo))

# will replace all characters that from lowercase a-z for 0s
# setting a flag with 'flags' param, gives us more control over sequence of characters, EX: re.I == ignorecase
# we can also use a number param as a range of characters to apply the sequence to
print(re.sub(r"[a-z]", "0", phrase, flags=re.I))
print(re.sub(r"[a-z]", '#', phrase, 5, flags=re.I))

