import smtplib
import datetime as dt
import random

weekdays = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")

# get current day of week
current_day = dt.datetime.now()
current_day_of_week = current_day.weekday()

# check to see if it is monday (send modivational quote)
if weekdays[current_day_of_week] == "Monday":
    with open("./quotes.txt") as file:
        quotes = file.readlines()  # get quotes from file
        quote = random.choice(quotes)

    # modify security to allow less secure app access
    FROM_EMAIL = "x@gmail.com"
    PASSWORD = "x"
    TO_EMAIL = "x@gmail.com"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()  # secure encrypted connection
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
