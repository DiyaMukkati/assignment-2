try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").lower()
    tickets = int(input("Enter number of tickets: "))

    # Base price by age
    if age < 3:
        price = 0
        category = "Free"
    elif age <= 12:
        price = 150
        category = "Child"
    elif age <= 59:
        price = 300
        category = "Adult"
    else:
        price = 200
        category = "Senior"

    base_amount = price * tickets

    # Discount check
    if day in ["friday", "saturday", "sunday"]:
        discount = base_amount * 0.20
    else:
        discount = 0

    final_amount = base_amount - discount

    print("\n--- TICKET DETAILS ---")
    print("Category:", category)
    print("Base price per ticket:", price)
    print("Base amount:", base_amount)
    print("Discount:", discount)
    print("Total amount:", final_amount)

except:
    print("Invalid input")