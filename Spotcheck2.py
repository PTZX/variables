#Paul Njenje
#29/09/2014
#Spot Check q2 - second try

weight = int(input("Enter a weight: "))

hundred = weight // 100
remainder = weight % 100

fifty = remainder // 50
remainder = remainder % 50

ten = remainder // 10
remainder = remainder % 10

five = remainder // 5
remainder = remainder % 5

two = remainder // 2
remainder = remainder % 2

one = remainder // 1
remainder = remainder % 1


print ("{0} one gram(s)|{1} two gram(s)|{2} five gram(s)|{3} ten(s)|{4} fifty(s)|{5} hundred(s)".format (one, two, five, ten, fifty, hundred))



