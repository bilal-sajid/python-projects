import smtplib
import datetime as dt
import random


my_email = "example@email.com"
my_password = "deffault"

now = dt.datetime.now()

day_of_week = now.weekday()

if day_of_week == 4:

    with open("Quotes Through Email Project/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls() # Makes the Connection Secure

        connection.login(user = my_email, password = my_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs = "example@email", 
                            msg = f"Subject: Testing\n\n{quote}")

