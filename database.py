#!/usr/bin/python
# -*- coding: utf-8 -*-

import Mysqldb;

# Verbindung erstellen
try:
    connection = Mysqldb.connect(host="localhost",    # your host, usually localhost
                     user="hems_user",         # your username
                     passwd="nF4mTRDT69RySz",  # your password
                     db="hems")        # name of the data base
except:
    print("Keine Verbindung zum Server")
    exit(0)

# Datensätze auslesen
cursor = connection.cursor()
cursor.execute("SELECT * from participants")
result = cursor.fetchall()
cursor.close()

for data in result:
    print(str(data[0]) + data[1] + data[2])