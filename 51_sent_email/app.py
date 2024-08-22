from email.message import EmailMessage
import smtplib

my_email = EmailMessage()

my_email['from'] = "Artuom"
my_email['to'] = "veronika198603@gmail.com"
my_email['subject'] = "Hello from Python"
my_email.set_content("Hey! How are you doing?")

with  smtplib.SMTP(host='localhost', port=2525 ) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(my_email)
    print('Email was sent!!!')

