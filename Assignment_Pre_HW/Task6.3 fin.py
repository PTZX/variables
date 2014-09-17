#Paul Njenje
#11-09-2014
#Task 6.3

#Tell the user about the program
print ("You have a Swimming pool that needs to be filled. Please give the dimensions, in metres, as follows:")

#Ask the user for the pools dimensions.
lenght = int(input("Please enter a lenght from 5 to 20: "))

width = int(input("Please enter a width from 1 to 5: "))

depth = int(input("Please enter a depth from 1 to 3: "))

#Display the users input for the pools dimensions
print("You chose a length of {0}, a width of {1} and a depth of {2}!".format(lenght, width, depth))

#Work out the volume of the pools
anwser = lenght * width * depth
print("The volume of water needed is {0}litres".format(anwser))
