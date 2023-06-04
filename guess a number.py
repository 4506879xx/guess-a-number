import random

def get_valid_input(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Please enter a valid number!")

def play_game():
    secret_num = random.randint(1, 100)
    guess = None
    guess_count = 0
    guess_limit = 3
    out_of_limit = False

    while secret_num != guess and not out_of_limit:
        guess_count += 1
        if guess_count <= guess_limit:
            guess = get_valid_input("Please guess a number (between 1 and 100): ")
            if guess > secret_num:
                print("Go lower")
            elif guess < secret_num:
                print("Go higher")
            else:
                out_of_limit = True
        else:
            out_of_limit = True

    if out_of_limit:
        print("Sorry, you lost. The correct answer was:", secret_num)
    else:
        print("Congratulations, you won!")

def play_again():
    choice = input("Do you want to play again? (Enter 'yes' or 'no'): ")
    return choice.lower() == 'yes'

def main():
    print("Welcome to the Guess the Number game!")
    play_game()

    while play_again():
        play_game()

    print("Game over. Thank you for playing!")

main()
