#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Event Verwaltung
#Import section
import sys
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

# Module components
#Event read
def event_read():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM event")
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


#Event create
def event_create_insert_into_db(name, type, num_participants, startdatetime, enddatetime, state):
    query = "INSERT INTO event(name,type,num_participants,startdatetime,enddatetime,state) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
    args = (name, type, num_participants, startdatetime, enddatetime, state)
    
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
        
        last_event_id = cursor.lastrowid
        sql_event_start = "CREATE EVENT " + name + "id" + str(last_event_id)+"start" + " ON SCHEDULE AT '" + startdatetime + "' DO UPDATE hems.event SET state = 'ready' WHERE id = " + str(last_event_id) + ";"
        sql_event_end = "CREATE EVENT " + name + "id" + str(last_event_id)+"end" + " ON SCHEDULE AT '" + enddatetime + "' DO UPDATE hems.event SET state = 'deprovison' WHERE id = " + str(last_event_id) + ";"
        
        cursor.execute(sql_event_start)
        cursor.execute(sql_event_end)
 
         
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()


def event_create():
    print ('Bitte füllen Sie die folgenden Felder aus:')
    name = raw_input('Eventname: ')
    type = raw_input('Typ: ')
    num_participants = raw_input('Anzahl Teilnehmer: ')
    startdate = raw_input('Startdatum (Format: 2017-01-01): ')
    startdatetime = startdate + " 01:00:00"
    enddate = raw_input('Enddatum (Format: 2017-01-01): ')
    enddatetime = enddate + " 20:00:00"
    state = "new"
    event_create_insert_into_db(name, type, num_participants, startdatetime, enddatetime, state)

#Event update
def event_update():
    event_read()

    print ('Bitte wählen Sie anhand der ID ein Event aus:')
    select_id = raw_input('ID: ')

    select_query = "SELECT * FROM event WHERE ID = "+select_id+";"    
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(select_query)
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

    print ('Bitte geben Sie die zu ändernden Daten ein:')
    name = raw_input('Eventname: ')
    type = raw_input('Typ: ')

    num_participants = raw_input('Anzahl Teilnehmer: ')

    startdate = raw_input('Startdatum (Format: 2017-01-01): ')
    startdatetime = startdate + " 01:00:00"

    enddate = raw_input('Enddatum (Format: 2017-01-01): ')
    enddatetime = enddate + " 20:00:00"
    state ="new"
    update_query = "UPDATE event SET name=%s, type=%s, num_participants=%s, startdatetime=%s, enddatetime=%s, state=%s WHERE id=%s"
    args = (name, type, num_participants, startdatetime, enddatetime, state, select_id)
    sql_event_start_drop = "DROP EVENT IF EXISTS "  + name + "id" + select_id +"start"+";"
    sql_event_end_drop = "DROP EVENT IF EXISTS "  + name + "id" + select_id +"end"+";"
    sql_event_start = "CREATE EVENT " + name + "id" + select_id +"start" + " ON SCHEDULE AT '" + startdatetime + "' DO UPDATE hems.event SET state = 'ready' WHERE id = " + select_id + ";"
    sql_event_end = "CREATE EVENT " + name + "id" + select_id +"end" + " ON SCHEDULE AT '" + enddatetime + "' DO UPDATE hems.event SET state = 'deprovison' WHERE id = " + select_id + ";"
            
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(update_query, args)
        cursor.execute(sql_event_start_drop)
        cursor.execute(sql_event_end_drop)
        cursor.execute(sql_event_start)
        cursor.execute(sql_event_end)
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


#Event delete
def event_delete():
    event_read()

    print ('Bitte wählen Sie anhand der ID das Event aus, welches Sie löschen wollen:')
    select_id = raw_input('ID: ')

    select_query = "DELETE * FROM event WHERE ID = "+select_id+";"    
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(select_query)
        conn.commit()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

#Instances read
def instances_read():

    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute()
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


#Menu selection
menupoint_1 = "1. Events anzeigen"
menupoint_2 = "2. Event hinzufügen"
menupoint_3 = "3. Event löschen"
menupoint_4 = "4. Event ändern"
menupoint_5 = "6. Zurück"
menupoint_6 = "7. Ende"

def print_menu():
    print 30 * "-" , "MENU" , 30 * "-"
    print menupoint_1
    print menupoint_2
    print menupoint_3
    print menupoint_4
    print menupoint_5
    print menupoint_6
    print 67 * "-"
  
loop=True      
  
while loop:
    print_menu() 
    choice = input("Ihre Auswahl [1-6]: ")
     
    if choice==1:     
        print menupoint_1
        event_read()
    elif choice==2:
        print menupoint_2
        event_create()
    elif choice==3:
        print menupoint_3
        ## You can add your code or functions here
    elif choice==4:
        print menupoint_4
        event_update()
    elif choice==5:
        print menupoint_6
        execfile('startmenu.py')   
    elif choice==6:
        print menupoint_7
        exit()    
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-7 we print an error message
        raw_input("Falsche Auswahl. Zum Fortfahren beliebige Taste drücken...")



#Main method
if __name__ == '__main__':
   print_menu()