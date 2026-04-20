import string
import random

caps = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
digits = list(string.digits)
special = list(string.punctuation)


def choose():
    '''Prompts for password requirements and returns a list of characters based on the user's choices.'''
    length = int(input("How long do you want the password to be?: "))
    while length < 8:
        print("\n\n⚠️Password must be at least 8 characters long")
        length = int(input("How long do you want the password to be?: "))
    caps_size = int(input("How many upper case letters do you want in your password?: "))
    lower_size = int(input("How many lower case characcters do you want in your password?: "))
    digit_size = int(input("How many numbers do you want in your passwords?: "))
    special_size = int(input("How many punctuation characters do you want in your password?: "))
    
    while length != caps_size + lower_size + digit_size + special_size :
        print("\n\n⚠️ The character count must add up to the total length of the password")
        return choose()
    
    password_choice = (
        random.choices(caps, k=caps_size)+
        random.choices(lower, k=lower_size)+
        random.choices(digits, k=digit_size)+
        random.choices(special, k=special_size)
    )
    return password_choice

def randomized():
    '''Prompts for password length and returns a list of characters based on the user's choice.'''
    length = int(input("How long do you want the password to be?: "))
    while length < 8:
        print("\n\n⚠️Password must be at least 8 characters long")
        length = int(input("How long do you want the password to be?: "))
    password_chars = random.choices(
        random.choices(caps, k=1) +
        random.choices(lower, k=1) +
        random.choices(digits, k=1) +
        random.choices(special, k=1) +
        random.choices(caps + lower + digits + special, k=length - 4)
    )
    return(password_chars)

def display_password(password):
    '''Shuffles the password characters and prints the final password.'''
    random.shuffle(password)
    print ("Your password is "+"".join(password))

print("====Password Generator======\n"
    "Choose a mode\n"
    "• random - Generate a fully randomized password with a minimum of eight characters\n"
    "• ordered - Select password length and number of each character type\n")

while True:
    mode = input("Enter your choice (random/ordered: )").lower().strip()
    if mode in ("ordered", "random"):
        break
    else:
        print("\n\n⚠️ Entry not valid\nPlease enter 'random' or 'ordered'")

if mode == "ordered": 
    display_password(choose())
else:
    display_password(randomized())
