import os
import smtplib

from email.message import EmailMessage


class NotificationManager:

    def __init__(self):

        self.email = os.environ["EMAIL_ADDRESS"]
        self.password = os.environ["EMAIL_PASSWORD"]

    def send_emails(self, emails, flight):

        subject = (
            f"Cheap flight alert: "
            f"{flight['origin']} → "
            f"{flight['destination']} "
            f"for £{flight['price']}"
        )

        body = (
            "✈️ Flight Club Alert!\n\n"
            f"Route: {flight['origin']} → {flight['destination']}\n"
            f"Price: £{flight['price']}\n"
            f"Departure: {flight['departure']}\n"
            f"Arrival: {flight['arrival']}\n"
            f"Stops: {flight['stops']}\n\n"
            "A cheap flight has been found!"
        )

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as connection:

            connection.login(
                self.email,
                self.password
            )

            for email in emails:

                message = EmailMessage()

                message["From"] = self.email
                message["To"] = email
                message["Subject"] = subject

                message.set_content(body)

                connection.send_message(message)

                print(f"Email sent to {email}")
