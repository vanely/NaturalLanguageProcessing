import nltk
# extracting names of things and people for the given text

paragraph = "The Taj Mahal was built by Emperor Shah Jahan"

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

# extracting named entity through ne_chunk() method NOTE: type == tree
namedEnt = nltk.ne_chunk(tagged_words)

# ne_chunk produces a tree, which we can visualize using the draw function
# draw() method output directives
# |S: simple entities of a sentence
# |ORGANIZATION: buildings, names of places, monuments, and companies all get translated to organizations
# |PERSON: people names, and titles
namedEnt.draw()
