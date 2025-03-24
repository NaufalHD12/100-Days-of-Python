##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import datetime as dt
import random
import smtplib
import pandas as pd
import os

my_email = "hadinaufal06@gmail.com"
password = "wagt rwwt hsqf jjrr"

df = pd.read_csv("Day32/birthday-wisher-hard-start/birthdays.csv")

now = dt.datetime.now()
today_day = now.day
today_month = now.month

data_dict = {(row["month"], row["day"]): row.to_dict() for _, row in df.iterrows()}

folder_path = "Day32/birthday-wisher-hard-start/letter_templates"
templates = os.listdir(folder_path)
random_template = random.choice(templates)
template_path = os.path.join(folder_path, random_template)

if (today_month, today_day) in data_dict:
    birthday_person = data_dict[(today_month, today_day)]
    name = birthday_person["name"]
    email = birthday_person["email"]
    
    # Pilih template secara acak
    folder_path = "Day32/birthday-wisher-hard-start/letter_templates"
    templates = os.listdir(folder_path)
    random_template = random.choice(templates)
    template_path = os.path.join(folder_path, random_template)

    
    with open(template_path, "r") as template_letter:
        letter_content = template_letter.read()
        
    personalized_letter = letter_content.replace("[NAME]", name)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="naufalhd4@gmail.com",
                msg=f"Subject: Happy Birthday {name}!\n\n{personalized_letter}"
                )