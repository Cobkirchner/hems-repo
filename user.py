#!/usr/bin/env python
# -*- coding: utf-8 -*-

#user Verwaltung
#Import section

import sys
import random
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


#Menu selection
menupoint_1 = "1. Nutzer anzeigen"
menupoint_2 = "2. Nutzer hinzufügen"
menupoint_3 = "3. Nutzer löschen"
menupoint_4 = "4. Nutzer ändern"
menupoint_5 = "5. Ende"

def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print menupoint_1
    print menupoint_2
    print menupoint_3
    print menupoint_4
    print menupoint_5
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Ihre Auswahl [1-5]: ")
     
    if choice==1:     
        print menupoint_1
        user_read()
    elif choice==2:
        print menupoint_2
        user_create()
    elif choice==3:
        print menupoint_3
        ## You can add your code or functions here
    elif choice==4:
        print menupoint_4
        ## You can add your code or functions here
    elif choice==5:
        print menupoint_5
        exit()    
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-7 we print an error message
        raw_input("Falsche Auswahl. Zum Fortfahren beliebige Taste drücken...")

#user read
def user_read():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        results = cursor.fetchall()
 
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
        for row in results:
            print(tavnit % row)
        print(separator)



    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()


#user create
def user_create_insert_into_db(surname, name, email, password):
    query = "INSERT INTO user(surname,name,email,password) " \
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

def user_create():
print "Bitte füllen Sie die folgenden Felder aus:"
surname = raw_input('Vorname: ')
name = raw_input('Nachname: ')
email = raw_input('E-Mail: ')
#password = raw_input('Please enter password: ')
#print "You entered:", surname, name, email, password



alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pw_length = 8
mypw = ""

for i in range(pw_length):
    next_index = random.randrange(len(alphabet))
    mypw = mypw + alphabet[next_index]

password = mypw

user_create_insert_into_db(surname, name, email, password)


#user update

def user_update_insert_into_db(surname, name, email):
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
 
def user_update(surname, name, email):
    
    print ('Welche Nutzerdaten wollen Sie ändern? Bitte füllen Sie die folgenden Felder aus:')
    surname = raw_input('Vorname ')
    name = raw_input('Nachname ')
    email = raw_input('E-Mailadresse: ') 
    # password = raw_input('You can enter a custom password: ')

    if not all ([surname, name, email]):
        print "Bitte füllen Sie alle Felder aus"
        ask() 
    
    user_update_insert_into_db

#user delete


#Main method
if __name__ == '__main__':
   print_menu()