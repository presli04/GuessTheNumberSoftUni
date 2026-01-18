import random

pc_number=random.randint(1,100)
while True:
    players_input=input("Guess the number between 1 and 100: ")
    if not players_input.isdigit():
        print("Invalid input,retry!")
        continue
    player_number=int(players_input)
    if player_number==pc_number:
        print("Correct!")
        break
    elif player_number>pc_number:
        print("Guess lower!")
    else:
        print("Guess higher!")
