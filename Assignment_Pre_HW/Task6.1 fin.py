#Paul Njenje
#11-09-2014
#Task 6.1

#Ask the user for three integers.
integer1 = int(input("Please enter a number from 1 to 10: "))

integer2 = int(input("Please enter a number from 5 to 20: "))

integer3 = int(input("Please enter a number from 1 to 5: "))

#Display the users input for three integers
print("You chose {0}, {1} and {2}!".format(integer1, integer2, integer3))

anwser = integer1 + integer2 + integer3
print("The sum of your numbers is {0}".format(anwser))


