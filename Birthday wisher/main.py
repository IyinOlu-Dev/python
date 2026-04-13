import pandas as pd
import datetime as dt




##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv



# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day

data = pd.read_csv("birthdays.csv")
print(data)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




