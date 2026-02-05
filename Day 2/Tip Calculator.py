def is_float(value):
    while True:
        try:
            value = float(value)
            return (value)
            break
        except ValueError:
            value = input(("Invalid input. Input digital values only: $"))

print("Welcome to the tip calculator")
bill = input("What was the total bill?: $")

bill = is_float(bill)

percentage_tip = input("What percentage tip are you willing to give: ")
percentage_tip = percentage_tip.replace("%", "")

percentage_tip = is_float(percentage_tip)

person = (input("How many people are paying the bill: "))
while not person.isdigit():
    person = input("Error. Please input an INTEGER: ")
person = int(person)

tip = (percentage_tip/100)*bill
print (f"Your tip is ${tip} ")

total = bill + tip
print (f"The total bill is :${total}")

each = total/person

print(f"Each person pays: ${each}")
