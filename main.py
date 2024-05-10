from customer_add import add_customer
from customer_fetch import fetch_customer, fetch_all_customers

def user_menu():

    while True:
        action = input('''
    1.) Add Customer
    2.) View Customer Details
    3.) Display All Customers
    4.) Main Menu
    > ''')
        
        if action == '1':
            add_customer()
        elif action == '2':
            fetch_customer()
        elif action == '3':
            fetch_all_customers()
        elif action == '4':
            break
        else:
            print('Invalid Input, please try again!')

while True:
    action = input('''
    1.) Customer Actions
    2.) Book Actions
    3.) Quit
    > ''')

    if action == '1':
        user_menu()
    elif action == '2':
        pass
        #send to book menu
    elif action == '3':
        break
    else:
        'Invalid Response, please try again'


