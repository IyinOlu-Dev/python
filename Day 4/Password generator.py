import random
import string

def password_length(min_char_length):

    valid_password_length = False
    while not valid_password_length:
        length = (input("How many characters do you want in your password: ")).strip()
        if not length.isdigit():
            print("InvalidInput.\nPlease input INTEGERS only ") 
            continue
        else:
            length = int(length)
        if length < min_char_length:
            print(f"InvalidInput\nYour password must be at least {min_char_length} characters long: ")
            continue
        else:
            valid_password_length = True
    return (length)


# print(char_pool)
def password_generator ():
    #accepts an integer representing the length of password characters(no less than 4) and prints a
    #string of passwords characters with at least one lower case, upper case, symbol and digit)
    digits = string.digits
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    symbols = string.punctuation
    space = " "
    space_allowed = input("Answer 'Y' or y for yes and 'N' or 'n' for no" \
    "\nDoes your password allow for the use of space? ").lower().strip()
    valid_response = ["n","no","y","yes"]
    while space_allowed not in  valid_response:
        space_allowed = input("Answer 'y' or 'yes' for yes and 'n' or 'no' for no").lower().strip()
    if space_allowed in ("n","no"):
        char_pool = digits+lower_case+upper_case+symbols
    if space_allowed in ("yes", "y"):
        char_pool = digits+lower_case+upper_case+symbols+space

    min_possible_length = 4
    length = password_length(min_possible_length)
    required = [random.choice(digits),random.choice(lower_case), random.choice(upper_case), random.choice(symbols)]
    remainder = random.choices(char_pool,k = length - 4)
    
    final_password = (required + remainder)
    random.shuffle(final_password)
    final_password = "".join(final_password)
    return(f"{final_password}")


bov = password_length(5)
print(bov)