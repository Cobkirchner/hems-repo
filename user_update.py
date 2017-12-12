#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

#from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config

def ask(surname, name, email)

    print ('Which user data do you want to change? Please enter the values you want to change: ')
    surname = raw_input('Please enter surname to update: ')
    name = raw_input('Please enter name: ')
    email = raw_input('Please enter email: ') # password = raw_input('You can enter a custom password: ')

    if not all ([surname, name, email]):
        print "Please enter valid details"
        ask()


def user_update(surname, name, email):
    # read database configuration
    db_config = read_db_config()
 
    # prepare query and data
    query = """ UPDATE user
                SET surname,name,email = %s
                WHERE email = %s """
 
    data = (surname, name, email)
 
    try:
        conn = MySQLConnection(**db_config)
 
        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)
 
        # accept the changes
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    ask(surname, name, email)
    user_update(surname, name, email)
