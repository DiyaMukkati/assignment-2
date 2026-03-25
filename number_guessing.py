import random

while True:
    secret = random.randint(1, 100)
    attempts = 7
    guessed = False

    print("\nGuess a number between 1 and 100")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret:
                print("Correct! You guessed it.")
                guessed = True
                break
            elif guess < secret:
                print("Too low")
            else:
                print("Too high")

            attempts -= 1
            print("Attempts left:", attempts)

        except:
            print("Invalid input")

    if not guessed:
        print("You lost. The number was:", secret)

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break