import smtplib
host = 'https://web.whatsapp.com/'
port = 587
user = ''
password = ''
server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(user, password)
