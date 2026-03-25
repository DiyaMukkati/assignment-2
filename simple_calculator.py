try:
    # Input from user
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    # Performing calculations
    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number

    # Displaying results
    print("\nResults:")
    print(f"{first_number} + {second_number} = {addition}")
    print(f"{first_number} - {second_number} = {subtraction}")
    print(f"{first_number} * {second_number} = {multiplication}")

    # Division (checking division by zero)
    if second_number != 0:
        division = first_number / second_number
        modulus = first_number % second_number
        print(f"{first_number} / {second_number} = {division:.2f}")
        print(f"{first_number} % {second_number} = {modulus}")
    else:
        print("Division and modulus not possible (division by zero)")

    # Exponentiation
    power = first_number ** second_number
    print(f"{first_number} ^ {second_number} = {power}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")