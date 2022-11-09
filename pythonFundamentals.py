# python fundamentals

# Lets build some python statements

# Here are the variables we'll be using
alpha = 5
beta = 7
maybeTrueMaybeFalse = False
itemPrice = 14.99
quantity = 10


# calculate total cost
totalCost = itemPrice * quantity
print(totalCost)

# using equality operators
if alpha == alpha:
	print(alpha, " equals ", alpha)
else:
	print(str(alpha) + " does not equal " + str(alpha))
	
if alpha == beta:
	print("alpha equals beta")
else:
	print("alpha does not equal beta")

if alpha != beta:
	print(str(alpha) + " does not equal " + str(beta))
else:
	print("alpha does equal beta")
	
if not maybeTrueMaybeFalse:
        print ("True")
else:
        print("False")

if alpha > beta or beta > alpha:
        print("True")
else:
        print("False")


print(10%7)
print(alpha>beta or maybeTrueMaybeFalse)
