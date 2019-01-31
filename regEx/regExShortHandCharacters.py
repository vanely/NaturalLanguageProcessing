import re

phrase = "Welcome to earth where our popular calendar is the Christian calendar hence the 2018"
phraseTwo = "just ~% +++--- arrived at @Jack's place. #fun"
phraseThree = "I          love          clouds"

# will replace digits with empty string(remove them)
phraseModified = re.sub(r"\d", "", phrase)
print(phraseModified)

# grouping differen chracters inside of a pattern(brackets are used for grouping different characters)
# to change the meaning of symbols EX: the '.' means any character but if we want it to just be a regular
# '.' then we use the '\' as an escape character
phraseTwoModified = re.sub(r"[@%#~+\-\.\']", "", phraseTwo)
print(phraseTwoModified)

# the '\w' is the character that represents, all word characters(a-zA-Z0-9)
phraseTwoModifiedTwo = re.sub(r"\w", "", phraseTwo)
print(phraseTwoModifiedTwo)

# the '\W' is the character that represents, all the non word characters(!@#$%^&*-+/()[]{})
phraseTwoModifiedThree = re.sub(r"\W", " ", phraseTwo)
print(phraseTwoModifiedThree)

# the '\s' is the character that represents a space, and the '+' represents 1 or more
# so the '\s+' represents 1 or more spaces
phraseTwoModifiedFour = re.sub(r"\s+", " ", phraseTwoModifiedThree)
print(phraseTwoModifiedFour)

# to remove single characters(that are not 'a' or 'I' we use use a a sequesnce like so
eliminateSingles = re.sub(r"\s+[b-hj-z]\s+", " ", phraseTwoModifiedFour, flags=re.I)
print(eliminateSingles)

phraseThreeModified = re.sub(r"\s+", " ", phraseThree)
print(phraseThreeModified)