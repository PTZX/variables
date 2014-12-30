def main():
    print("Test Percentage")
    print()
    testScore = int(input("Please enter your test score: "))

    if testScore > 80 and testScore > 70:
        print("A grade")
    elif testScore > 70 and testScore > 60:
        print("B grade")
    elif testScore > 60 and testScore > 50:
        print("C grade")
    elif testScore > 50 and testScore > 40:
        print("D grade")
    elif testScore > 40:
        print("E grade")
    else:
        print("Fail")

