

try:
    num = int(input("Enter number: "))
    end = int(input("Enter range (end): "))

    print("\nMultiplication Table of", num)
    
    for i in range(1, end + 1):
        print(num, "x", i, "=", num * i)

except:
    print("Invalid input")