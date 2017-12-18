#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import required modules
#
from email.mime.text import MIMEText
import smtplib
import sys


#
# declaration of the default mail settings
#

# mail address of the sender
sender = 'mitsmhems@gmail.com'

# fully qualified domain name of the mail server
smtpserver = 'smtp.gmail.com'

# username for the SMTP authentication
smtpusername = 'mitsmhems@gmail.com'

# password for the SMTP authentication
smtppassword = 'hems@2017'

# use TLS encryption for the connection
usetls = True


#
# function to send a mail
#
def sendmail(recipient,subject,content):

  # generate a RFC 2822 message
  msg = MIMEText(content)
  msg['From'] = sender
  msg['To'] = recipient
  msg['Subject'] = subject

  # open SMTP connection
  server = smtplib.SMTP(smtpserver)

  # start TLS encryption
  if usetls:
    server.starttls()

  # login with specified account
  if smtpusername and smtppassword:
    server.login(smtpusername,smtppassword)

  # send generated message
  server.sendmail(sender,recipient,msg.as_string())

  # close SMTP connection
  server.quit()


#
# main function
#
def main():

  # call sendmail() and generate a new mail with specified subject and content
  recipent = 'christian.obkirchner@outlook.com'
  subject = 'Test'
  message = 'Testnachricht'
  sendmail(recipent,subject,message)

  # quit python script
  sys.exit(0)


if __name__ == '__main__':
  main()