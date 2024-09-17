import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = None # EMAIL
MY_PASSWORD = None # PASSWORD

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)
# print(today)


birthdays_df = pandas.read_csv("Automated Birthday Wisher/birthdays.csv")
# print(birthdays_df)


birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays_df.iterrows()}
# print(birthdays_dict)


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"Automated Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()

        contents = contents.replace("[NAME]", birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user = MY_EMAIL, password = MY_PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs = birthday_person["email"], 
                            msg = f"Subject: Happy Birthday\n\n{contents}")



