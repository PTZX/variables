#Paul Njenje
#22-09-2014
#Class Exercise Dev_2

#ask for a temperature in dergees fahrenheit
degrees_fehr = int(input("Enter a temperature in degrees fahrenheit: "))

#calculate the equivalent for degrees cent.
degrees_cent = (degrees_fehr - 32) * (5/9)

#display the temerature in degrees cent.
print ("This is the temperature in dergrees centegrade: {0}".format(degrees_cent))
