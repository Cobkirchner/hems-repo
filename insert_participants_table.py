#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

#def read_from_cli(surname, name, email, password):
    surname = input("Please enter surname: ")
    name = input("Please enter name: ")
    email = input("Please enter email: ")
    password = input("Please enter password: ")

    print "You entered:", surname, name, email, password

def insert_participant(surname, name, email, password):
    query = "INSERT INTO participants(participants_surname,participants_name,participants_email,participants_password) " \
            "VALUES(%s,%s,%s,%s)"
    args = (surname, name, email, password)
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   insert_participant('surname','name','email','password')
 
if __name__ == '__main__':
    main()