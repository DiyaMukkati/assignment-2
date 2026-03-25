# Sum and Average Calculator

try:
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Enter a valid count")
    else:
        total = 0
        maximum = None
        minimum = None

        for i in range(1, n + 1):
            num = int(input("Enter number " + str(i) + ": "))
            total = total + num

            if maximum is None or num > maximum:
                maximum = num
            if minimum is None or num < minimum:
                minimum = num

        average = total / n

        print("\nSum:", total)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)

except:
    print("Invalid input")