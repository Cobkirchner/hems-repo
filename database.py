#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
 
def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM participants")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchall()



# Datensätze auslesen
#cursor = connection.cursor()
#cursor.execute("SELECT * from participants")
#result = cursor.fetchall()
#cursor.close()

#for data in result:
#    print(str(data[0]) + data[1] + data[2])