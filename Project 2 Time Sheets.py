import os

def main():
    choice_main =  'y'
    while choice_main == 'y' or choice_main == 'Y':
        print('Options: \n 1. Get employee times \n 2. Get individual costs ')
        print(' 3. Get week cost \n 4. Enter new employee \n 5. View employee \n 6. Exit program')
        selection = input('Pick something already (***Placeholder DONT SUBMIT): ')
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
            exit()
        else:
            print('Does this look like a game to you? (***Change this before submitting too)')
        choice_main = input('Do you want to do select anything else? [Y]es or [N]o: ')
        os.system('cls')

def get_times():
    os.system('cls')
    namesheet_read = open('names.txt', 'r')
    namesheet = namesheet_read.read()
    choice_main = 'y'
    while choice_main == 'y' or choice_main == 'Y':
        choice = input('Please enter the number for your choice:\n 1. List Employees\n 2. Select Employee\n')
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
        menu_choice = input('1. View Employee list.\n 2. Enter employee name.\n')
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