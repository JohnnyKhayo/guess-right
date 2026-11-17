import random

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy   (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard   (5 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 10, "Easy"
        elif choice == "2":
            return 7, "Medium"
        elif choice == "3":
            return 5, "Hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")



def play_round():
    lowest_num = 1
    highest_num = 100
    secret_number = random.randint(lowest_num, highest_num)
    max_attempts, level = choose_difficulty()
    attempts_used = 0
    wrong_guesses = 0

    print(f"\n{level} mode. I'm thinking of a number between {lowest_num} and {highest_num}.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts_used < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts_used + 1}/{max_attempts} - Your guess: "))
            if guess < lowest_num or guess > highest_num:
                print(f"Please enter a number between {lowest_num} and {highest_num}.\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        attempts_used += 1

        if guess == secret_number:
            print(f"\nCorrect! You got it in {attempts_used} attempts.")
            return
        else:
            wrong_guesses += 1
            if guess < secret_number:
                print("Too Low!")
            else:
                print("Too High!")

                    # Hint after 3 wrong guesses
            if wrong_guesses == 3:
                if secret_number % 2 == 0:
                    print("Hint: The number is even.")
                else:
                    print("Hint: The number is odd.")
                if secret_number % 5 == 0:
                    print("Hint: The number is divisible by 5.")


        remaining = max_attempts - attempts_used
        if remaining > 0:
            print(f"Attempts left: {remaining}\n")
        else:
            print(f"\nOut of attempts! The number was {secret_number}.")


def main():
    print("=== Number Guessing Game ===")
    print("Welcome! Let's play.")
    play_round()


if __name__ == "__main__":
    main()