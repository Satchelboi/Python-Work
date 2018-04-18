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
            print(namesheet)
        if choice == '2':
            employee = input('Enter employee name: ')
            for line in namesheet:
                if employee in line:
                    print(line)
        choice_main = input('Do you want to do select anything else? [Y]es or [N]o: ')
    namesheet_read.close()
    return False

def indv_cost():
    os.system('cls')
    return False

def week_cost():
    os.system('cls')
    return False

def emp_entry():
    os.system('cls')
    return False

def emp_view():
    os.system('cls')
    return False

main()