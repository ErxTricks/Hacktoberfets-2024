import random

def play_game():
    random_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 3
    
    print("Welcome to the Guessing Game!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between 1 and 10 (Attempt {attempts + 1}/{max_attempts}): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        attempts += 1
        
        if guess == random_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempt(s)!")
            break
        elif attempts < max_attempts:
            print("Incorrect guess. Try again!")
        else:
            print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {random_guess}.")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()