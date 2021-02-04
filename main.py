from Util import *

userchoice_str = input(
    '''
    Welcome to Bank_De_La_Cruz
    Enter 1 to Create a new account
    Enter 2 to perform new transactions
    Enter 3 for an update on your account
    Enter 4 to view account status
    Enter 5 to check transaction history
    Enter 6 to Exit
    '''
)

userchoice_int = int(userchoice_str)

if userchoice_int == 1:
    create_new_account()
if userchoice_int == 2:
    accountnumber = int(input("Enter your account number"))
    # perform_new_transaction(accountnumber)
if userchoice_int == 3:
    accountnumber = int(input("Enter your account number"))
    # update_your_account(accountnumber)
