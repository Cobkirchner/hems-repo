#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Event Verwaltung
#Import section
import sys
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def get_num_participants(): 
    
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("""SELECT num_participants FROM event WHERE state = "ready";""")
        result = cursor.fetchone()[0]
        print (result)
    
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

#Main method
if __name__ == '__main__':
   get_num_participants()       