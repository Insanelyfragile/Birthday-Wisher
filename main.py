import smtplib
import random
import datetime
import pandas
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("my_email")
password = os.getenv("my_pass")

df = pandas.read_csv("birthdays.csv")
year = (df["year"].tolist())
month = (df["month"].tolist())
day = (df["day"].tolist())


def send():
    num = random.randint(1, 3)

    with (open(f"letter_templates/letter_{num}.txt") as letter):
        id_value = df.loc[df['day'] == datetime.datetime.now().day, 'name'].iloc[0]
        lett = letter.read().replace("[NAME]", id_value)
        sender = df.loc[df['day'] == datetime.datetime.now().day, 'email'].iloc[0]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=sender,
            msg=f"Subject:Happy Birthday!!\n\n{lett}")


now = datetime.datetime.now()
if any(item == now.month for item in month):
    if any(itemm == now.day for itemm in day):
        send()
