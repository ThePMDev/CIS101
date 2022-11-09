# multiply two numbers

# numberOne = 5
# numberTwo = 2

numberOne = input("Enter your first number -> ")
numberTwo = input("Enter your second number -> ")

def timesTwo(num1, num2):
    product = int(num1) * int(num2)
    return product


print ("The first number is " + str(numberOne))
print ("The second number is " + str(numberTwo))
# product = int(numberOne) * int(numberTwo)

result = timesTwo(numberOne, numberTwo)
print ("The product of " + str(numberOne) + " times " + str(numberTwo) + " is " + str(result))

