import smtplib

my_email = "email_address"
password = "password"

connection = smtplib.SMTP("smt.email.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="rec@email.com"
    msg= "Subject: Hello \n\nThis is the body of my email."
)

connection.close()