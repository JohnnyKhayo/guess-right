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
            return attempts_used, level
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

    return None, level

def save_score(attempts, level):
    name = input("Enter your name: ").strip()
    if not name:
        name = "Anonymous"
    name = name.replace(",", "")

    with open("high_scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{level},{attempts}\n")
    print("Score saved!")


def main():
    print("=== Number Guessing Game ===")
    print("Welcome! Let's play.")

    result, level = play_round()

    if result is not None:
        save = input("\nSave this score? (y/n): ").strip().lower()
        if save == "y":
            save_score(result, level)

def show_leaderboard():
    try:
        with open("high_scores.txt", "r", encoding="utf-8") as file:
            scores = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, level, attempts = parts
                    try:
                        scores.append((name, level, int(attempts)))
                    except ValueError:
                        continue

        if not scores:
            print("No scores yet.")
            return

        scores.sort(key=lambda x: x[2])
        print("\n--- Top Scores ---")
        for i, (name, level, attempts) in enumerate(scores[:5], 1):
            print(f"{i}. {name} | {level} | {attempts} attempts")

    except FileNotFoundError:
        print("No scores yet.")

if __name__ == "__main__":
    main()