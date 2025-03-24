# import smtplib

# my_email = "hadinaufal06@gmail.com"
# password = "wagt rwwt hsqf jjrr"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="naufalhd4@gmail.com",
#         msg="Subject: Hello\n\nThis is the body of my email"
#         )
    
    
# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)


import datetime as dt
import random
import smtplib

my_email = "hadinaufal06@gmail.com"
password = "wagt rwwt hsqf jjrr"

day_of_week = dt.datetime.today().weekday()

with open("Day32/Birthday+Wisher+(Day+32)+start/quotes.txt", "r") as file:
    list_of_quotes = [line for line in file]
    random_quote = random.choice(list_of_quotes)
    if day_of_week == 1:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="naufalhd4@gmail.com",
                msg=f"Subject: Monday Motivation\n\n{random_quote}"
                )