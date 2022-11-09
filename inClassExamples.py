"""
# Write an program that takes in a user’s name and appropriately outputs their name in the song ‘Happy Birthday’
# This will require variables, input and print statements

user_name = input("Please enter your name: ")


print("\nHappy Birthday to you")
print("Happy Birthday to you")
print("Happy Birthday dear " + user_name)
print("Happy Birthday to you")




# Using the first program, create a function that outputs the same song when the function is called
# This will require all of the above plus defining a function using the keyword def and then calling that function, you do not need to pass the function any parameters


user_name = input("\nPlease enter your name: ")

def birthday():
    print("\nHappy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear " + user_name)
    print("Happy Birthday to you")

birthday()
birthday()
birthday()




# Using the same program, modify it so you pass the user’s name to the function when called

name1 = input("\nPlease enter your name: ")
name2 = input("\nPlease enter another name: ")

def birthday(name):
    print("\nHappy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear " + name)
    print("Happy Birthday to you")

birthday(name1)
birthday(name2)



# Using the same program, modify it so you only write 'Happy Birthday to you' once

user_name = input("\nPlease enter your name: ")

def line():
    print("Happy Birthday to you")

def birthday(name):
    line()
    line()
    print("Happy Birthday dear " + name)
    line()



birthday(user_name)




# Write a program that uses a function that takes two parameters to calculate the area of a rectangle.
# This will require that you use variables, input and print along with defining and calling a function

side_1 = input("\nPlease enter the length of the long side: ")
side_2 = input("Please enter the length of the short side: ")

def area():
    print("\nThe area of a rectange with the long side of length " + str(side_1) + " and a short side of length " + str(side_2) + " is", float(side_1) * float(side_2))

area()



# Write a program that asks the user for a whole number greater than zero.
# If the number is less than 100 tell them that number is a small number, otherwise tell them that number is a large number.
# This will require using the keywords if and else

your_number = input("\nplease enter a whole number greater than zero: ")

if int(your_number) < 100:
    print(your_number + " is a small number")

else:
    print(your_number + " is a large number")



# Using that program, modify it so if the number is less than 10 tell them it is a single digit number,
# if it is less than 100 but at least 10 tell them that it is a double digit number,
# otherwise tell them that it is larger than a double digit number.
# This will require using the keywords if elif and else 


your_number = input("\nplease enter a whole number greater than zero: ")

if int(your_number) < 10:
    print(your_number + " is a single digit number")
    
elif int(your_number) >= 10 and int(your_number) < 100:
    print(your_number + " is a double digit number")

else:
    print(your_number + " is a larger that a double digit number")

"""

# Using a while loop, write a program that asks a user for a number.
# If the number is less than ten thousand, ask them to enter a larger number.
# Once they enter a number larger than ten thousand, end the loop and tell them the number is large enough.


number = input("\nPlease enter a number: ")

while int(number) < 10000:
    if int(number) < 10000:
        print("\nThat number is too small")
        number = input("Please enter a larger number: ")

print(number + " is large enough")



# Write a program that is a number guessing game that counts the number of attempts it takes for a user to guess a number between 1 and 100.
# After every guess, tell the user if the number is too high or two low and let them keep guessing until they guess the right number
# Then let them know both that they are correct and how many attempts it took.
# This will require that you assign a number between 1 and 100 to a variable first for the user to guess and a variable to count the number of attempts.

from random import randint

my_number = randint(1, 101)

guess = 0

counter = 1

print("Welcome to the guessing game where you enter numbers to guess my number between 1 and 100")
print("You will have seven attempts to guess correct number")

while guess != my_number and counter < 8:
    guess = int(input("\nPlease enter your guess: "))

    if guess > my_number:
        print("Your guess is too high")

    elif guess < my_number:
        print("Your guess is too low")

    else:
        print("\nSpot on!")

    counter = counter + 1

if counter == 6:
    print("you lose!" )

else:
    print("Your guessed my number", my_number, "and it only took", counter, "tries")



"""
