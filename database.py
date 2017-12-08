#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='hems',
                                       user='hems_user',
                                       password='nF4mTRDT69RySz')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()



# Datensätze auslesen
#cursor = connection.cursor()
#cursor.execute("SELECT * from participants")
#result = cursor.fetchall()
#cursor.close()

#for data in result:
#    print(str(data[0]) + data[1] + data[2])