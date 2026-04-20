import random

#-----------------Global variable-----------------#
WINS = {("rock","scissors"), ("scissors","paper"), ("paper","rock")}

ART = {"rock": '''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''', 

"paper": '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''',

"scissors": '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''}

CHOICES = tuple(ART.keys())


def get_choice() ->str:
    '''Prompts for user's guess until a valid choice is given and returns it as string.'''

    while True:
        choice = input(f'Pick {", ".join(CHOICES)}:  ').lower().strip()
        if choice in CHOICES:
            return  choice
        print (f'Invalid choice. Please pick from {", ".join(CHOICES)}')

def round_result(u_choice: str, c_choice: str) ->str:
    '''Returns win, loose or draw based on game conditions and user's choice'''
    if u_choice == c_choice:
        return "draw"
    return "win" if (u_choice, c_choice) in WINS else "lose"

def game_logic(rounds:int) ->dict:
    '''Main game logic, returns a dictionary with the number of wins, losses and draws.'''
    wins = lose = 0
    draw = 0
    while  rounds > 0:
        u_choice = get_choice()
        c_choice = random.choice(CHOICES)

        result = round_result(u_choice = u_choice, c_choice= c_choice)
        print (f"Computer chose {c_choice}")
        
        match result:
            case "draw":
                draw +=1
                print("It is a draw")
            case "win":
                wins +=1
                rounds -=1
                print("You win this round")
            case "lose":
                lose +=1
                rounds -=1
                print("You lost this round")
        print(f"You have {rounds} remaining")

    print("----Game Over----")
    return {"wins": wins, "lose": lose, "draw": draw}


def main() -> None:
    '''Main function to run the game.'''
    print ("Welcome to the Rock, Paper, Scissors game\n\n")
    rounds = int(input("How many rounds do you want to play?:  "))
    game_result = game_logic(rounds=rounds)

    print(f"Wins: {game_result['wins']} \nLosses: {game_result['lose']} \nTotal number of draws: {game_result['draw']}")

    if game_result["wins"] > game_result["lose"]:
        print("🎉 You won overall!")
    elif game_result["lose"] > game_result["wins"]:
        print("💀 You lost overall")
    else:
        print("🤝 It's an overall draw!")

if __name__ == "__main__":
    main()