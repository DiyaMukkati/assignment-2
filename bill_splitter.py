try:
    bill = float(input("Enter total bill: "))
    people = int(input("Number of people: "))
    tax = float(input("Tax percentage: "))
    tip = float(input("Tip percentage: "))

    if people == 0:
        print("People cannot be zero")
    else:
        tax_amount = bill * tax / 100
        after_tax = bill + tax_amount
        tip_amount = after_tax * tip / 100
        total = after_tax + tip_amount
        per_person = total / people

        print("\n=== BILL BREAKDOWN ===")
        print("Subtotal: ₹", bill)
        print("Tax:", tax_amount)
        print("After tax:", after_tax)
        print("Tip:", tip_amount)
        print("Total:", total)
        print("Per person:", per_person)

except:
    print("Please enter numbers only")