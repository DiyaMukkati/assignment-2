try:
    year = int(input("Enter a year: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a Leap Year")
        print("Reason: Divisible by 4 and not by 100, or divisible by 400")
    else:
        print(year, "is NOT a Leap Year")
        print("Reason: Does not satisfy leap year rules")

except:
    print("Invalid input")