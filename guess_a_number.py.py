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
    if difficulty=="easy" and player_number==pc_number:
        for _ in range(1,tries):
            if tries==1:
                print(f"You guessed the number from the {tries} time.Bravo!You win 100 points ")
                break
            elif tries==2:
                print(f"You guess the number from the {tries} time.Bravo!You win 90 points ")
                break
            elif tries == 3:
                print(f"You guess the number from the {tries} time.Bravo!You win 80 points ")
                break
            elif tries==4:
                print(f"You guess the number from the {tries} time.Bravo!You win 70 points ")
                break
            elif tries==5:
                print(f"You guess the number from the {tries} time.Bravo!You win 60 points ")
                break
    elif difficulty=="medium" and player_number==pc_number:
        for _ in range(1,tries):
            if tries == 1:
                print(f"You guessed the number from the {tries} time.Bravo!You win 150 points ")
                break
            elif tries == 2:
                print(f"You guess the number from the {tries} time.Bravo!You win 140 points ")
                break
            elif tries == 3:
                print(f"You guess the number from the {tries} time.Bravo!You win 130 points ")
                break
    elif difficulty=="hard" and player_number==pc_number:
        for _ in range(1, tries):
            if tries == 1:
                print(f"You guessed the number from the {tries} time.Bravo!You win 500 points ")
                break
    if player_number!=pc_number:
        counter_of_failed_attemptss+=1
    if counter_of_failed_attemptss>=tries:
        print("Failed to guess the number.")
        print("Do you want to play again?")
        player_answer=input()
        if not players_input.isdigit():
            print("Invalid input,retry!")
            continue
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


