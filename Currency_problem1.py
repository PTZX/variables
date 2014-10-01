print("Give me an amount of money in whole ponds and I will tell you how many notes and/or coins it would convert to:")

cash = int(input("Enter an amount of money in whole ponuds: £"))

twenty = cash // 20
remainder = cash % 20

ten = remainder // 10
remainder = remainder % 10

five = remainder // 5
remainder = remainder % 5

two = remainder // 2
remainder = remainder % 2

one = remainder

print("|x{0} £20 note(s)|x{1} £10 note(s)|x{2} £5 note(s)|x{3} £2 coin(s)|x{4} £1 coin(s)".format(twenty, ten, five, two, one))
