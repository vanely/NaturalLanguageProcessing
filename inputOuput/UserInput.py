# CONSOLE I/O
name = str(input("Enter your name: "))
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Hi there {} ".format(name))
print("The answer to %d + %d is %d" % (num1, num2, num1 + num2))
