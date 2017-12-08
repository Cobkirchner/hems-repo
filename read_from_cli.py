#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def read_from_cli(surname, name, email, password):
    surname = input('Please enter surname: ')
    name = input('Please enter name: ')
    email = input('Please enter email: ')
    password = input('Please enter password: ')
    print "You entered:", surname, name, email, password

def main():
   read_from_cli(surname, name, email, password)
 
if __name__ == '__main__':
    main()