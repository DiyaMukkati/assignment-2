def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

try:
    # Part 1: Single number check
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a PRIME number")

    # Part 2: Range check
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    print("Prime numbers:", end=" ")

    for i in range(start, end + 1):
        if is_prime(i):
            print(i, end=" ")

except:
    print("Invalid input")