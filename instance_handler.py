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
        result = cursor.fetchone()[0]()

        widths = []
        columns = []
        tavnit = '|'
        separator = '+' 

        for cd in cursor.description:
            widths.append(max(cd[2], len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-"+"%ss |" % (w,)
            separator += '-'*w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in result:
            print(tavnit % row)
        print(separator)
    
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

#Main method
if __name__ == '__main__':
   get_num_participants()       