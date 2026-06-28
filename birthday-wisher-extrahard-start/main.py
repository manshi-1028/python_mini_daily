

import smtplib
import csv
import datetime as dt
import random

today = dt.datetime.now()
password = "dhajkc"
my_email = "sample@gmail.com"
PLACEHOLDER_TEXT = "[NAME]"
choice=["letter_1","letter_2","letter_3"]

with open("birthdays.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["month"]) == today.month and int(row["day"]) == today.day:
            send_to=row["email"]
            name=row["name"]
            with open(f"./letter_templates/{random.choice(choice)}.txt", "r") as letter:
                letters = letter.read()
                new = letters.replace(PLACEHOLDER_TEXT, name.strip())
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=send_to,
                    msg=f"Subject:Happy Birthday\n\n {new}"
                )



