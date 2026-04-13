import random

print ("Welcome to the Rock Paper Scissors game\n\n\n")
rounds = int(input("How many rounds do you want to play"))
wins = (("rock","scissors"), ("scissors","paper"), ("paper","rock")) 

rock = '''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

art = {"rock": rock, "paper":paper, "scissors": scissors}

won_round = 0
lost_round = 0

game_over = True

while game_over:
    u_choice = input("What do you choose?: \nPick rock, paper, or scissors").lower()
    while u_choice not in ("rock", "paper", "scissors"):
        print('Please select either "rock", "paper", or "scissors"')
        u_choice = input("What do you choose?: \nPick rock, paper, or scissors").lower()
    c_choice= random.choice(["rock","scissors", "paper"]).lower()

    print(f"Computer chose: {art[c_choice]}")
    print(f"You chose:{art[u_choice]}")

    if u_choice == c_choice:
        print ("It's a draw")
        print(f"You have {rounds} rounds left")
    elif (u_choice, c_choice) in wins:
        print("You win")
        rounds -=1
        print(f"You have {rounds} rounds left")
        won_round +=1
    else:
        rounds -=1
        lost_round +=1
        print("You lose this round!")
    
    if rounds == 0:
        game_over=False
        print("No more rounds left")
        print(f"You won {won_round} and lost {lost_round}")
        if won_round > lost_round:
            print("You win")
        elif won_round < lost_round:
            print("You lost")
        else:
            print("It was a Draw")

