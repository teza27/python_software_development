import random
def guessing_game():
    guess = random.randint(1, 100)
    max_attempts = 5
    print(guess)
    while max_attempts > 0: # and max_attempts != 1:
        take_a_guess = int(input("Guess a number between 1 and 100\n"))
        #if take_a_guess is not numeric:
        max_attempts -= 1
        if take_a_guess < guess:
            print(f"Your guess is too low, you have {max_attempts} attempts(s) left")
        elif take_a_guess > guess:
            print(f"Your guess is too high, you have {max_attempts} attempts(s) left")
        else:
            print("You guessed right!")
            break
    retry = input("Would you like to play the game again? Yes or No: \n").title()
    if retry == "Yes":
        guessing_game()
    else:
        print("Thank you for your attempt, the game is now exiting!")

guessing_game()