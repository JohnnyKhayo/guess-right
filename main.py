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



def main():
    print("=== Number Guessing Game ===")
    print("Welcome! Let's play.")
    max_attempts, level = choose_difficulty()
    print(f"You selected {level} mode with {max_attempts} attempts.")


if __name__ == "__main__":
    main()