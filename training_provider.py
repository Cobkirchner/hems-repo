#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Schulungsanbieter Verwaltung
#Import section

import sys
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


#Menu selection
menupoint_1 = "1. Schulungsanbieter anzeigen"
menupoint_2 = "2. Schulungsanbieter hinzufügen"
menupoint_3 = "3. Schulungsanbieter ändern"
menupoint_4 = "4. Schulungsanbieter löschen"
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
        Schulungsanbieter_read()
    elif choice==2:
        print menupoint_2
        ## You can add your code or functions here
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

#training_provider read
def training_provider_read():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM training_provider")
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


#training_provider create

#training_provider update

#training_provider delete


#Main method
if __name__ == '__main__':
   print_menu()