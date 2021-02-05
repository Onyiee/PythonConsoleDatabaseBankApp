from Util import *

checker = 1
while checker != -1:

    userchoice_str = input(
        '''
        Hi there! Welcome to Bank_De_La_Cruz
        To Create a new account, enter 1
        To perform new transactions, enter 2
        For an update on your account, enter 3
        To view your account details, enter 4
        To delete your account, enter 5
        Enter 6 to Exit
        '''
    )
    userchoice_int = int(userchoice_str)

    if userchoice_int == 1:
        new_account_creation()
    if userchoice_int == 2:
        perform_transactions()
    if userchoice_int == 3:
        update_accountdetails()
    if userchoice_int == 4:
        view_accountdetails()
    if userchoice_int == 5:
        delete_account()
    if userchoice_int == 6:
        checker = -1
