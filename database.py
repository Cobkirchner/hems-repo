#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="hems_user",         # your username
                     passwd="nF4mTRDT69RySz",  # your password
                     db="hems")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# Use all the SQL you like
cursor.execute("SELECT * FROM participants")

# print all the first cell of all the rows
#for row in cursor.fetchall():
#    print "%s, %s" % (row["participants_id"], row["participants_email"], row["participants_password"])

rows = cursor.fetchall()
for row in rows:
    for col in row:
        print "%s," % col
    print "\n"

db.close()