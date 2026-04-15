import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bid() -> tuple[str, int]:
    name = input("Please enter your name: ").strip()

    while True:
        try:
            bid = float(input("How much do you want to bid?: "))
            break
        except ValueError:
            bid = print("Invalid please enter a number")
    return name, bid

def find_winner(bids:dict[str, int]) -> tuple[str, int]:
    return max(bids, key = bids.get), max(bids.values())


def main():
    clear_screen()
    print ("Welcome to the secret auction")
    while True:
        try:
            number = int(input("How many people are bidding?: "))
            break
        except ValueError:
            amount = print("Invalid please enter a number")
    
    bids ={}
    for _ in range (number):
        name, amount = get_bid()
        bids[name] = amount
        clear_screen()

    winner, winning_bid = find_winner(bids)

    print(f"{winner} won the auction witha final_bid of {winning_bid} ")

if __name__ == "__main__":
    main()