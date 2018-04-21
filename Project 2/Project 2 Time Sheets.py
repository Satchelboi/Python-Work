import os
import sqlite3
from time import sleep
from crazy_intro import intro

db = sqlite3.connect('employees.db')
ex = db.cursor()

def main(): # Fully functional
    intro()
    sleep(2)
    os.system('cls')
    choice_main =  'y'
    while choice_main == 'y':
        selection = input("""
    Options: 
    
1. Get employee times 
2. Get individual costs 
3. Get week cost 
4. Enter new employee 
5. View employee 
6. Exit program
> """)
        if selection == '1':
            get_times()
            print()
        elif selection == '2':
            indv_cost()
        elif selection == '3':
            week_cost()
        elif selection == '4':
            emp_entry()
        elif selection == '5':
            emp_view()
        elif selection == '6':
            db.close()
            exit()
        else:
            print('Does this look like a game to you? (***Change this before submitting too)')

def get_times():
    os.system('cls')
    namesheet_read = open('names.txt', 'r')
    namesheet = namesheet_read.read()
    choice_main = 'y'
    while choice_main == 'y' or choice_main == 'Y':
        choice = input('Options:\n1. List Employees \n2. Select Employee\n>')
        if choice == '1':
            emp_list()
            print()
        if choice == '2': # Still pseudocode-ish, re-visit and iron out functionality
            employee = input('Enter employee name: ')
            for line in namesheet: # Statement not currently functional
                if employee in line:
                    print(line)
        choice_main = input('Do you want to do select anything else? [Y]es or [N]o: ')
    namesheet_read.close()
    return False

def indv_cost():
    os.system('cls')
    choice_main = 'y'
    namesheet = open('pay_rate.txt', 'r') # Juggling too many files, try to condense and sort into fewer
    while choice_main == 'y' or choice_main == 'Y':
        menu_choice = input('Options:\n1. View Employee list.\n2. Enter employee name.\n>')
        if menu_choice == '1':
            emp_list()
            print()
        if menu_choice == '2':
            emp_fetch = input('Enter the name of the employee you wish to see the weekly cost of: ')
#           Find employee name in file and print out name with set pay rate
#           Pseudocode now, revise once files are condensed and organized
        choice_main = input('Would you like to perform anything else? [Y]es [N]o: ')
    return False

def week_cost(): # Function written in pseudocode right now, fix once files are properly condensed
    os.system('cls')
    return False

def emp_entry():
    os.system('cls')
    choice_main = 'y'
    while choice_main == 'y' or choice_main == 'Y':
        menu_choice = input('Options:\n1. Add new employee.\n2. Edit existing employee.\n3. Remove employee.\n>')
        if menu_choice == '1':
            emp_name = input('Enter new employee name: ')
            emp_pos = input('Enter new employee position: ')
            emp_pay = input('Enter new employee pay: ')
            # ex.execute( <ADD emp_name to TABLE name, emp_pos to TABLE position, emp_pay to TABLE payroll> )
        if menu_choice == '2':
            emp_name = input('Enter employee name: ')
            emp_type = input('Options: 1. Edit employee name\n 2. Edit employee position\n 3. Edit employee pay\n >')
            # ex.execute(search TABLE names for emp_edit)

    return False

def emp_view():
    os.system('cls')
    return False

def emp_list(): # Added to reduce redundant code between other functions
    os.system('cls')
    name_list = open('names.txt', 'r')
    name_read = name_list.read()
    name_list.close()
    return name_read

main()