import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('index.html').read_text())
email = EmailMessage()
email['from']='Taruna'
email['to']= 'rt.tarunarawat@gmail.com'
email['subject']= 'won a lottery'
email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()		#initiate request
	smtp.starttls()		#secure connection
	smtp.login('rt.tarunarawat@gmail.com','rt112233')
	smtp.send_message(email)
	print('all done')