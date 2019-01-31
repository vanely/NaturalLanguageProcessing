# FILE I/O
usrInput = input("Enter some text: ")
inputText = "\n" + usrInput
# with keyword will close the file automatically
# Explination in details file
# Opening a file in 'write' mode and storing the reference in 'f'
# if file does not exist it will be created, and 'w' will erase what is in the file and replace
# with ne content

with open("textFile.txt", "w") as f:
    f.write(usrInput)

# using 'a' will append to the file and not overwrite what's already inside'
with open("textFile.txt", "a") as f:
    f.write(inputText)

# using 'r' allows us to read the contents of a file
with open("textFile.txt", 'r') as f:
    print(f.read())
