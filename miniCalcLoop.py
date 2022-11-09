# mini calculator

# set the calculator to execute at least once
doAnotherCalculation = 1

while doAnotherCalculation == 1:
    # prompt the user for the first number
    num1 = int(input("Enter your first number -->  "))

    # prompt the user for the operation they would like to perform
    operator = input("Enter the operation you would like to perform -->  ")

    # prompt the user for the second number
    num2 = int(input("Enter your second number -->  "))

    # use if, elif, else statements to perform the proper calculation
    if operator == "+":
        print("The result of ", num1, operator, num2, " is: ", num1 + num2)
    elif operator == "-":
        print("The result of ", num1, operator, num2, " is: ", num1 - num2)
    elif operator == "*":
        print("The result of ", num1, operator, num2, " is: ", num1 * num2)
    elif operator == "/":
        print("The result of ", num1, operator, num2, " is: ", num1 / num2)
    else:
        print("The operation can't be performed")
    
    # ask the user if they want to perform another calculation
    doAnotherCalculation = int(input("Enter 1 to perform another calculation or 0 to stop -->  "))

# let the user know they have quit the program
print("Thank you for using the WC2019 Super Calculator")
