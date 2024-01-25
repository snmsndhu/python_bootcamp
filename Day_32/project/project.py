#Automated Birthday Wisher Project

import smtplib
import pandas
from datetime import datetime
import random

MY_EMAIL = "email_address"
MY_PASSWORD = "password"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,2)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()
        content.replace("[NAME]", birthday_person["name"])

with smtplib.SMTP("smt.email.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="rec@email.com",
        msg= "Subject: Hello \n\nThis is the body of my email.")

    connection.close()



