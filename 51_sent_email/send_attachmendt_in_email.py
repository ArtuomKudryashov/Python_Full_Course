from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()
html_template = Template(Path("templates/index.html").read_text())
html_content= html_template.substitute({'name':'Artuom','date': 'tomorrow'})

my_email['from'] = "Artuom <accademic198405@gmail.com>"
my_email['to'] = "Artuom198603@gmail.com"
my_email['subject'] = "Email with  image"
my_email.set_content(html_content, 'html')

with open('images/test3.jpg','rb') as img:
    image_date = img.read()
    my_email.add_attachment(image_date, maintype = 'image', subtype = 'jpg',filename='test3.jpg')

with  smtplib.SMTP(host='localhost', port=2525 ) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(my_email)
    print('Email was sent!!!')

