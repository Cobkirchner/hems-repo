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

for (participants_name, participants_email, participants_password) in cursor:
      print("{}, {}, {}".format(participants_name, participants_email, participants_password))

db.close()