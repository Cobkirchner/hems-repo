#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Instance Handler
# Exectution every hour, stored in crontab: 0 * * * * /home/hems-repo/instance_handler.py
#Import section
import sys
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

from email.mime.text import MIMEText
import smtplib
import sys
from shutil import copyfile
import subprocess
import os


def get_num_participants(): 
    
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("""SELECT num_participants FROM event WHERE state = "ready";""")
        result = cursor.fetchone()[0]
        print (result)
        cursor.execute("""SELECT id FROM event WHERE state = "ready";""")
        result_id = cursor.fetchone()[0]
        print (result_id)
        #update_query = "UPDATE event SET state = "provisoned" WHERE id = "+ result_id +";"
        cursor.execute("""UPDATE event SET state = "provisoned" WHERE id = "+ result_id +";""")
        conn.commit()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
    copyfile ('/home/hems-repo/terraform/variables.tf', '/home/hems-repo/terraform/variables.old')
    copyfile ('/home/hems-repo/terraform/variables.template', '/home/hems-repo/terraform/variables.tf')
    
    fileHandle = open ( '/home/hems-repo/terraform/variables.tf', 'a' )
    fileHandle.write ( 'default = '+ str(result) + '}' )
    fileHandle.close()

    os.chdir("/home/hems-repo/terraform/")
    subprocess.call(["terraform", "apply"])

    mail (result)


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
def mail(result):

  # call sendmail() and generate a new mail with specified subject and content
  recipent = 'christian.obkirchner@outlook.com'
  subject = 'Neue Instanzen erstellt'
  message = 'Es wurden '+ str(result) + ' Instanzen erstellt.'
  sendmail(recipent,subject,message)

  # quit python script
  sys.exit(0)



#Main method
if __name__ == '__main__':
   get_num_participants()       