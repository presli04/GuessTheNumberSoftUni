import random

pc_number=random.randint(1,100)
difficulty=input("Choose difficulty (eg. easy, medium, hard): ")
tries=0
counter_of_failed_attemptss=0
while True:
    players_input=input("Guess the number between 1 and 100: ")
    if difficulty=="easy":
        tries=5
    elif difficulty=="medium":
        tries=3
    elif difficulty=="hard":
        tries=1
    if not players_input.isdigit():
        print("Invalid input,retry!")
        continue
    player_number=int(players_input)
    if player_number!=pc_number:
        counter_of_failed_attemptss+=1
    if counter_of_failed_attemptss>=tries:
        print("Failed to guess the number.")
        print("Do you want to play again?")
        player_answer=input()
        if player_answer=="yes":
            tries+=1
        else:
            break
    if player_number==pc_number:
        print("Correct!")
        break
    elif player_number>pc_number:
        print("Guess lower!")
    else:
        print("Guess higher!")


