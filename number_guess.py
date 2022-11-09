
# Write a program that is a number guessing game that counts the number of attempts it takes for a user to guess a number between 1 and 100.
# After every guess, tell the user if the number is too high or two low and let them keep guessing until they guess the right number
# Then let them know both that they are correct and how many attempts it took.
# This will require that you assign a variable first for the user to guess and a variable to count the number of attempts.

from random import randint

total = 100000
my_number = randint(1, total)

guess = 0

counter = 0
limit = 50

print("Welcome to the guessing game where you enter numbers to guess my number between 1 and " + str(total))
print("You will have " + str(limit) + " attempts to guess correct number")

while guess != my_number and counter < limit:
    guess = int(input("\nPlease enter your guess: "))

    if guess > my_number:
        print("Your guess is too high")

    elif guess < my_number:
        print("Your guess is too low")

    else:
        print("\nSpot on!")

    counter = counter + 1

if counter == limit:
    print("you lose!" )

else:
    print("Your guessed my number", my_number, "and it only took", counter, "tries")

