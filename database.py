#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="hems_user",         # your username
                     passwd="nF4mTRDT69RySz",  # your password
                     db="hems")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = db.cursor()

# Use all the SQL you like
cursor.execute("SELECT participants_id, participants_email, participants_password FROM participants")

# print all the first cell of all the rows
for row in cursor.fetchall():
    print row[0]
db.close()