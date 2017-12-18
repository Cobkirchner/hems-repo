#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
#notes           :
#python_version  :2.7.6  
#=======================================================================

# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}  

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print "Willkommen,\n"
    print "Bitte wählen Sie eine Rolle aus:"
    print "(1) Administrator"
    print "(2) Schulungsanbieter"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Ungültige Eingabe.\n"
            menu_actions['main_menu']()
    return

# =======================
#    MENU Administrator
# =======================
def menu1():
    print "Administratormenü !\n"
    print "(1) Cloud Accountverwaltung"
    print "(2) Eventverwaltung"
    print "(3) Nutzerverwaltung"
    print "(4) Konfigurationsverwaltung"
    print "(5) Templateverwaltung"
    print "(6) Schulungsanbieterverwaltung"
    print "(0) Ende"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# =======================
#    MENU Schulungsanbieter
# =======================
def menu2():
    print "Schulungsanbieter Menü !\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()