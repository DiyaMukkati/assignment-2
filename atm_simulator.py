balance = 10000

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Current Balance: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance = balance + amount
                print("Deposit successful")
                print("New Balance: ₹", balance)
            else:
                print("Enter valid amount")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Enter valid amount")
            elif balance - amount < 500:
                print("Minimum balance of ₹500 must be maintained")
            else:
                balance = balance - amount
                print("Withdrawal successful")
                print("New Balance: ₹", balance)

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

    except:
        print("Invalid input")