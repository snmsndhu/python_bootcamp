#Email SMTP and the datetime module

"""
Basically we will learn how to send email using the python.

Email SMTP is module that is pre bundle with the python and it helps us send
email using the python.

Datetime is another module, that helps us to figure out what's today date is,
and format that.
"""

#How does the email process works

"""
sender => first server => second server => reciever

This is the whole process behind the seen and all this is done by using the ,
SMTP
which stands for Simple Mail Transfer Protocal
This contains all of the rules that determines how email can be sent by the internet.
It is basically the postman.
"""

#Let have a look on some of the methods of Datetime module

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1234, month=22, day=33)
print(date_of_birth)