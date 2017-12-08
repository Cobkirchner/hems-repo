#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config

print ('Which user data do you want to change? Please enter the values you want to change: ')
surname = raw_input('Please enter surname: ')
for val in surname:
    if val == "":
        continue
    print ("Please enter a value")

print("The end")



#name = raw_input('Please enter name: ')
#email = raw_input('Please enter email: ')
#password = raw_input('Please enter password: ')