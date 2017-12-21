#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Text menu in Python


menupoint_1 = "1. Administrator"
menupoint_2 = "2. Schulungsanbieter"
menupoint_3 = "3. Administrator Schulungsanbieter" 
menupoint_4 = "4. Ende"
      
def print_menu():       ## Your menu design here
    print 28 * "-" , "Startmenue" , 28 * "-"
    print menupoint_1
    print menupoint_2
    print menupoint_3
    print menupoint_4
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Ihre Auswahl [1-4]: ")
     
    if choice==1:     
        print menupoint_1
        execfile('menu_admin.py')
    elif choice==2:
        print menupoint_2
        execfile('menu_training_provider.py')
    elif choice==3:
        print menupoint_2
        execfile('menu_training_provider_admin.py')
    elif choice==4:
        print menupoint_3
        exit()    
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-7 we print an error message
        raw_input("Falsche Auswahl. Zum Fortfahren beliebige Taste drücken...")