#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Text menu in Python


menupoint_1 = "1. Cloud Accountverwaltung"
menupoint_2 = "2. Eventverwaltung"
menupoint_3 = "3. Nutzerverwaltung"
menupoint_4 = "4. Konfigurationsverwaltung"
menupoint_5 = "5. Templateverwaltung"
menupoint_6 = "6. Schulungsanbieterverwaltung"
menupoint_7 = "7. Ende"

      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print menupoint_1
    print menupoint_2
    print menupoint_3
    print menupoint_4
    print menupoint_5
    print menupoint_6
    print menupoint_7
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-7]: ")
     
    if choice==1:     
        print menupoint_1
        execfile('sendmail.py')
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
        ## You can add your code or functions here
    elif choice==6:
        print menupoint_6
        ## You can add your code or functions here
    elif choice==7:
        print menupoint_7
        exit()    
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-7 we print an error message
        raw_input("Falsche Auswahl. Zum Fortfahren beliebige Taste drücken...")