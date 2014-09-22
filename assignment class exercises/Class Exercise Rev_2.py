#Paul Njenje
#11-09-2014
#class_exercises rev_2

#Ask the user for three integers and display the total.
integer1 = int(input("Please enter a number from 2 to 10: "))
integer2 = int(input("Please enter a number from 5 to 20: "))
integer3 = int(input("Please another number from 5 to 20: "))

#Display the users input for 3 integers
print("You chose {0}, {1} and {2}!".format(integer1, integer2, integer3))

#multiply int1 by int2
answer = integer1 * integer2
answer2 = answer / integer3

#display answer
print("{0}".format(answer2))


