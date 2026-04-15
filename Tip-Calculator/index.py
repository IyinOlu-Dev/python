print ("Welcome to the tip calculator")

price = float(input("How much was the bill?: "))

tip_type = input('Do you want to give "percentage" or "set amout"').lower()

''' ------------ Confirm tip type--------------------------'''

while tip_type not in ("set amount", "percentage"):
    tip_type = input('Please enter "percentage" or "set amout"').lower()
tip = float(input("How much is the tip?: "))

people = int(input("how many people are splitting the bill?: "))

if tip_type == "set amount":
    split = (price + tip)/people
elif tip_type == "percentage":
    total = (price + (tip/100)*price)
    split = total/people

'''------------------------Print Result-----------------------'''
print(f"Each person pays: ${split:.2f}")