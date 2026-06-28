import smtplib
import datetime as dt
import random

password = "dhajkc"
my_email = "sample@gmail.com"

with open("quotes.txt", "r") as file:
    my_list = file.read().splitlines()

now = dt.datetime.now()
day_of_the_week = now.weekday()

# Monday is represented by 0
if day_of_the_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="appbrewerytesting@yahoo.com",
            msg=f"Subject:Quote of the Day\n\n{random.choice(my_list)}"
        )
