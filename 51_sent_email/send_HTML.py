from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()
html_template = Template(Path("templates/index.html").read_text())
html_content= html_template.substitute({'name':'Artuom','date': 'tomorrow'})

my_email['from'] = "Artuom"
my_email['to'] = "Artuom198603@gmail.com"
my_email['subject'] = "Let's go out2"
my_email.set_content(html_content, 'html')

with  smtplib.SMTP(host='localhost', port=2525 ) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(my_email)
    print('Email was sent!!!')

