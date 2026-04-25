# if it smaller comes after the bigger -> add e.g vi
# if bigger comes after the smaller -> subtract e.g iv
#  if they are equal -> add e.g xx

#-------- Validator------#
# if sum of consecutive values equal next numeral -> send an error( suggest to use the next numeral instead of adding the same numeral multiple times) e.g iii = 3 but iv = 4
# ------------------CODE------------------#  

# class Solution:
roman_dict = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} 
def get_roman_numeral():
    
    s = str(input("Type the roman numeral:  ")).upper()
    while not all(chars in roman_dict for chars in s):
        print("Error. Value is not a roman integer")
        s = str(input("Type the roman numeral:  ")).upper()
    return s

def romanToInt(s:str) -> int:
    roman_dict = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} 
    result = 0

    for i, chars in enumerate(s):
        current_val = roman_dict[chars]
        if i+1 < len(s):
            next_val = roman_dict[s[i+1]]
            if current_val < next_val:
                current_val = -current_val
        result += current_val
    return result    

# val = get_roman_numeral()
value = romanToInt(s= "xcv")
print(value)