import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
rounds_played = 0
max_rounds = 5

while rounds_played < max_rounds and player_score < 3 and computer_score < 3:

    while True:
        player_choice = input("Choose rock, paper, scissors (or 'quit'): ").lower()

        if player_choice == "quit":
            print(f"Final score — You: {player_score}, Computer: {computer_score}")
            break

        if player_choice not in choices:
            print("Invalid choice, try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score — You: {player_score}, Computer: {computer_score}\n")