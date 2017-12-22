#!/usr/bin/env python
# -*- coding: utf-8 -*-

#configuration Verwaltung
#Import section

import sys
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config




#Configuration read
def configuration_read():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM configuration")
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


#Configuration create
def configuration_create_insert_into_db(name, cpu, ram, space, type):
    query = "INSERT INTO configuration(name, cpu, ram, space, type) " \
            "VALUES(%s,%s,%s,%s.%s)"
    args = (name, cpu, ram, space, type)
 
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

def configuration_create():
    print ('Bitte füllen Sie die folgenden Felder aus:')
    name = raw_input('Name ')
    cpu = raw_input('CPU ')
    ram = raw_input('RAM: ')
    space = raw_input('Speicherplatz: ') 
    type = raw_input('Typ: ') 

    configuration_create_insert_into_db(name, cpu, ram, space, type)

#Configuration update
def configuration_update_insert_into_db(select_id, name, cpu, ram, space, type):
    # read database configuration
    db_config = read_db_config()
 
    # prepare query and data
    query = """ UPDATE configuration
                SET name = %s,cpu = %s,ram = %s,space = %s,type = %s
                WHERE id = %s """
 
    data = (name, cpu, ram, space, select_id)
 
    try:
        conn = MySQLConnection(**db_config)
 
        # update
        cursor = conn.cursor()
        cursor.execute(query, data)
 
        # accept the changes
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def configuration_update():
    configuration_read()
    print ('Welche Nutzerdaten wollen Sie ändern? Bitte füllen Sie die folgenden Felder aus:')
    select_id = raw_input('ID: ')
    name = raw_input('Name ')
    cpu = raw_input('CPU ')
    ram = raw_input('RAM: ')
    space = raw_input('Speicherplatz: ')
    type = raw_input('Typ: ') 
    # space = raw_input('You can enter a custom space: ')

    if not all ([name, cpu, ram, space]):
        print ('Bitte füllen Sie alle Felder aus')

    
    configuration_update_insert_into_db (select_id, name, cpu, ram, space, type)

#Configuration delete
def configuration_delete():
    configuration_read()

    print ('Bitte wählen Sie anhand der ID den configuration aus, welchen Sie löschen wollen:')
    select_id = raw_input('ID: ')

    delete_query = "DELETE FROM configuration WHERE ID = "+ select_id +";"    
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(delete_query)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


#Menu selection
menupoint_1 = "1. Konfiguration anzeigen"
menupoint_2 = "2. Konfiguration hinzufügen"
menupoint_3 = "3. Konfiguration ändern"
menupoint_4 = "4. Konfiguration löschen"
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
        configuration_read()
    elif choice==2:
        print menupoint_2
        configuration_create()
    elif choice==3:
        print menupoint_3
        configuration_update()
    elif choice==4:
        print menupoint_4
        configuration_delete()
    elif choice==5:
        print menupoint_5
        exit()    
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-7 we print an error message
        raw_input("Falsche Auswahl. Zum Fortfahren beliebige Taste drücken...")

#Main method
if __name__ == '__main__':
   print_menu()