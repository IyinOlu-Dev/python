import smtplib

my_email = "unprotectedtest@gmail.com"
my_password = "mzby maso bvcc sdxy"


import datetime as dt
now =  dt.datetime.now()
week= dt.datetime.now().isocalendar().week
print(now)
year = now.year

count = 0

day = now.weekday()

if day == 0:
    with open ("quotes.txt",) as file:
        all_quotes = file.readlines()
        day_quote = (all_quotes[count])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= my_password )
        connection.sendmail(from_addr=my_email, to_addrs= f"tomiwaoyegbola9@gmail.com", 
                            msg=f"Subject: Morning Quotes\n\n{day_quote}")
        connection.close




# print(type(day))
