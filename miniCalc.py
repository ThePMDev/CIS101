
# build a four function calculator

##first_number = input("Enter the first value -> ")
##operation = input("Enter the operation you want to perform -> ")
##second_number = input("Enter the second value -> ")
##
##if operation == "+":
##    print("The sum of " + first_number + " and " + second_number + " is ", float(first_number) + float(second_number))
##
##elif operation == "-":
##        print("The difference of " + first_number + " and " + second_number + " is ", float(first_number) - float(second_number))
##
##elif operation == "*" or operation == "x" or operation == "X":
##        print("The product of " + first_number + " and " + second_number + " is ", float(first_number) * float(second_number))
##
##elif operation == "/":
##        print("Dividing " + first_number + " by " + second_number + " is ", float(first_number) / float(second_number))


number = int(input("enter # -> "))

if number >= 100:
    print("your number is larger than double digits")
elif number >= 10:
    print("you have a double digit number")
else:
    print("Your number is single digits")
