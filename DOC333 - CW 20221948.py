# STEP 1: Initializing Variables

import random
print("WELCOME TO THE INKY, PINKY, POLLY")


Player_score = 0
Computer_score = 0
play_again = True

# STEP 2 : Getting input from the player and playing the game until the player chooses to stop the game.

# Computer choose = c1
# Player choose = p1


while play_again:
    c1 = random.choice(["Inky", "Pinky", "Polly"])
    p1 = input("Enter your choice (Inky or Pinky or Polly):")

    # STEP 3 : Deciding the winner and getting the score from every choose
    if p1 not in ["Inky", "Pinky", "Polly"]:
        print("Invalid Input")
        continue
        
    if p1 == c1:
        print("Ooooh it's tie! Let's Play again.")
        play_again_input = input("DO you wish to play again....? If you want Enter(yes) if you do not want Enter(no)")
    elif (p1 == "Inky" and c1 == "Polly") or (p1 == "Polly" and c1 == "Pinky") or (p1 == "Pinky" and c1 == "Inky"):
        print("Congratilations!!! You won.")
        Player_score += 1
        play_again_input = input("DO you wish to play again....? If you want Enter(yes) if you do notwant Enter(no)")
    else:
        print("So Sorry, you lost. Hope better luck next time!")
        Computer_score += 1
        play_again_input = input("DO you wish to play again....? If you want Enter(yes) if you do not want Enter(no)")

    # STEP 4 : Asking the player if he want to continue or want to end the game.

    if play_again_input.lower() == "no":
        play_again = False

# STEP 5 : Displaying the final scores and who's winner

print("Final Scores:")
print("Player.", Player_score)
print("Computer.", Computer_score)

if Player_score == Computer_score:
    print("Oooh it's tie.!")
elif Player_score > Computer_score:
    print("Congratulations..! You won the Game.")
else:
    print("Sorry man, you lost the game. Hope better luck next time.!")

# End Inky, Pinky, Polly Game
