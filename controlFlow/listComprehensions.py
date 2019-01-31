numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list comprehensions can be used to iterate over and display list items
Sum = [num for num in numbers]
print(Sum)

# can also be used to filter out list items with conditionals
newNums = [nums for nums in numbers if nums <= 6]
print(newNums)

numbersTwo = [1, 3, 5, 7, 9]

# can also filter using other arrays
newNumsTwo = [nums for nums in numbers if nums not in numbersTwo]
print(newNumsTwo)

multByTwo = [nums * 2 for nums in numbers]
print(multByTwo)

odds = [nums for nums in numbers if nums % 2 == 1]
print(odds)

# generator comprehension
squareGen = (nums**2 for nums in numbers)
print(squareGen)

myDict = {"apple": 1, "orange": 4, "banana": 10}

# dictionary comprehension
          #key: value
newDict = {key: myDict[key] for key in myDict.keys()}
print(newDict)

# filtering dictionary values
newDictTwo = {key: myDict[key] for key in myDict.keys() if myDict[key] >= 5}
print(newDictTwo)

# jpin() to concat strings with specific delimiters
words = ["I", "love", "python"]
sentence1 = ' '.join(words)
print(sentence1)

sentence2 = '.'.join(words)
print(sentence2)

sentence3 = '$'.join(words)
print(sentence3)