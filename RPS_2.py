import random

#Variables
winner_dict = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

score = 0
times_played = 0
question = input("Do you want to play? ")

#Update scores
def update_stats():
    global score
    global times_played
    if winner == 1:
        score += 1

    elif winner == 2:
        score = 0

    times_played += 1

#Game Loop/Checks
while question == "yes".lower():
    comp_answer = random.choice(list(winner_dict.keys()))
    human_input = input("Rock, Paper or Scissors? ").lower()

    if winner_dict[human_input] == comp_answer:
        winner = 1
        print("You Won")

    elif winner_dict[comp_answer] == human_input:
        winner = 2
        print("You Lost")

    elif human_input == comp_answer:
        winner = 3
        print("You Tied")

    print("Computer Chose: " + comp_answer)

    update_stats()
    print("Your Streak Is: " + str(score))
    print("You've Played: " + str(times_played) + " Times")

    question = input("Again? ")

    if question == "no".lower():
        quit()
