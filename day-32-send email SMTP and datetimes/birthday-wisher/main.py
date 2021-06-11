import pandas
import random
import datetime as dt
import smtplib

# extract birthday list
birthdays_df = pandas.read_csv("./birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")

# get current date information
current_datetime = dt.datetime.now()
current_month = current_datetime.month
current_day = current_datetime.day

# check all birthdays in list against todays date
for person in birthdays_dict:
    month = person['month']
    day = person['day']
    if (current_month, current_day) == (month, day):
        # chose a random letter template
        template_num = random.randint(1, 3)
        with open(f"./letter_templates/letter_{template_num}.txt") as file:
            template_text = file.read()
            msg_text = template_text.replace("[NAME]", person['name'])

        # modify security to allow less secure app access
        FROM_EMAIL = "x@gmail.com"
        PASSWORD = "x"
        to_email = person['email']

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()  # secure encrypted connection
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=FROM_EMAIL, to_addrs=to_email,
                                msg=f"Subject:Happy Birthday!\n\n{msg_text}")
