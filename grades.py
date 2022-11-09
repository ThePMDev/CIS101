# create a program that calculates a student's letter grade and outputs the grade and if they passed or not

# set the exam's point value
# set the default letter grade
# set the default for passing
# input the user's score
# convert the user's input into an integer
# calculate the percentage
# determine the student's grade based on their score
# output the grade results
# output if the student passed or not

# Sample output
# What was the student's score? 88
# The exam was worth 100  points
# You earned a score of 88 or 88.0 %
# Your grade is: B
# You earned credit for this course

########################################

# set the exam's point value
total = 100

# set the default letter grade
grade = "F"

# set the default for passing
credit = False

# input the user's score
earned = input("What was the student's score? ")

# the value in 'earned' is "88" and I want 88 as an integer without the quote marks

# convert the user's input into an integer
earned = int(earned)

# calculate the percentage
score = earned / total

# test your progress so far
# print("the score is ", score)

# determine the student's grade based on their score and if they received credit
if score >= 0.90:
        grade = "A"
        credit = True

elif score >= 0.80:
        grade = "B"
        credit = True

elif score >= 0.70:
        grade = "C"
        credit = True

elif score >= 0.60:
        grade = "D"

else:
        grade = "F"

# output the grade results
print("The exam was worth", total, "points")
print("You earned a score of", earned, "or", score * 100, "%")
print("your grade is: " + grade)

# output if the student passed or not
if credit:
        print("You earned credit for this course")
else:
        print("You failed to earn credit for this course")


# Sample output
# What was the student's score? 88
# The exam was worth 100  points
# You earned a score of 88 or 88.0 %
# Your grade is: B
# You earned credit for this course
