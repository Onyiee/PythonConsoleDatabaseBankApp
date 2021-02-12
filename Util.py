from Db_Connection import *


def initialize():
    connection = initialize_connection()
    create_tables()
    return connection


def new_account_creation():
    firstname = input("Enter your firstname ")
    lastname = input("Enter your lastname ")
    mobile_number = input("Enter your mobileNumber ")
    date_of_birth = input("Enter your date of birth in YYYY-MM-DD format ")
    if firstname == "":
        raise ValueError("firstname must be entered ")
    if mobile_number == "":
        raise ValueError("mobile number must be entered")
    if lastname == "":
        raise ValueError("lastname must be entered")

    sql = 'insert into bankapp.customer(firstname, lastname, mobilenumber, date_of_birth) ' \
          'values (%s, %s, %s, %s)'
    values = [(firstname, lastname, mobile_number, date_of_birth)]

    connection = initialize()
    connection.cursor().executemany(sql, values)
    connection.commit()
    query = f'select customerId from bankapp.customer where mobilenumber = {mobile_number}'
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()  # fetchone returns a tuple based on how our columns are arranged
    print(result)
    customer_id = result[0]
    query = 'insert into bankapp.account(customerId, accountType, accountStatus) ' \
            'values (%s, %s, %s)'

    account_type = int(input("Enter 1 for a savings account, 2 for a current account"))
    if account_type == 1:
        account_type = 'savings'
    else:
        account_type = 'current'

    values = [(customer_id, account_type, 'active')]
    cursor.executemany(query, values)
    connection.commit()
    close_connection()


def perform_transactions():
    account_number = int(input("Enter your account_number"))
    transactiontype = int(input("Enter 1 for withdrawal, 2 for a tranfer, 3 for deposit"))
    if transactiontype == 1:
        transactiontype = "withdrawal"
    if transactiontype == 2:
        transactiontype = "transfer"
    if transactiontype == 3:
        transactiontype = "deposit"

    transactionamount = int(input("Enter an amount "))
    transactionmedium = input("Select 1 for mobile transfer, 2 for ATM ")
    if transactionmedium == 1:
        transactionmedium = "mobile_transfer"
    if transactionmedium == 2:
        transactionmedium = "ATM"

    sql = 'insert into bankapp.transactions(accountnumber, transactiontype, \
     transactionamount, transactionmedium) ' \
          'values(%s, %s, %s, %s)'
    values = (account_number, transactiontype, transactionamount, transactionmedium)
    connection = initialize()
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()
    connection.close()


def view_accountdetails():
    account_number = int(input("Enter your account number "))
    sql = f'''select  *  from account join customer
    on customer.customerId  = account.customerId 
    where accountnumber = {account_number}'''
    connection = initialize()
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    connection.close()
    print(result)


def update_accountdetails():
    account_number = int(input("Enter your account number "))
    user_choice = int(input("Enter 1 to update firstname, Enter 2 to update lastname, Enter 3 to update occupation"))
    column_name = ''
    new_value = ''
    if user_choice == 1:
        column_name = 'firstname'
        new_value = input("Enter your new firstname")
    elif user_choice == 2:
        column_name = 'lastname'
        new_value = input("Enter your new lastname")
    else:
        column_name = 'occupation'
        new_value = input("Enter new occupation")
    customer_id_query = f'select customerId from account where accountnumber = {account_number}'
    connection = initialize()
    cursor = connection.cursor()
    cursor.execute(customer_id_query)
    result = cursor.fetchone()
    customer_id = result[0]
    sql = f'update customer set {column_name} = %s where customerid = {customer_id}'
    value = (new_value,)
    cursor.execute(sql, value)
    connection.commit()
    connection.close()


def delete_account():
    account_number = int(input("Enter your account number "))
    customer_id_query = f'select customerId from account where accountnumber = {account_number}'
    connection = initialize()
    cursor = connection.cursor()
    cursor.execute(customer_id_query)
    result = cursor.fetchone()
    customer_id = result[0]
    delete_account_query = 'Delete from account where accountnumber = %s'
    delete_customer_query = 'Delete from customer where customerId = %s'
    cursor.execute(delete_account_query, (account_number,))
    cursor.execute(delete_customer_query, (customer_id,))
    connection.commit()
    connection.close()
