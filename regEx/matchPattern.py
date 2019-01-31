# regEx uses sequences of characters to find, create, or require patterns in text(wild cards on steroids)
import re

phrase = "I was born in the year 1994"
phraseTwo = ""
phraseThree = "absent"

# match is used for matching specific patterns
# to declare a pattern we type 'r'(regular expression)

# the 'period' signifies any character, and the 'asterisk' means a presence of 0 or more
# so we are matching a sequence of length 0 or more of any character(will match anything)
patternAll = re.match(r".*", phrase)
print(patternAll)

# using the '+' will match only from length 1 or more(if pattern is of length 0 we get none)
patternOneOrMore = re.match(r".+", phraseTwo)
print(patternOneOrMore)

# will return pattern of anything that is a letter from a-z and A-Z, but no other characters(including spaces)
patternLetter = re.match(r"[a-zA-Z]+", phrase)
print(patternLetter)  # only outputs 'I' because we come acros a space

# will match an a and 0 or 1 b(in the sentence after 'a' there can be no 'b' or exactly one 'b')
patternSpecific = re.match(r"ab?", phraseThree)
print(patternSpecific)

