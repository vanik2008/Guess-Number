import random

def guess_number():
    secret_number = random.randint(1, 100)  # Generating a random number between 1 and 100
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it.")

    while True:
        user_guess = int(input("Enter your guess: "))

        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try a higher number.")
        elif user_guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number()
