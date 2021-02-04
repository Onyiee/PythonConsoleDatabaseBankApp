from Connection import *


def initialize():
    connection = initialize_connection()
    use_database()
    create_tables()
    return connection


def create_new_account():
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
    values = [(firstname, lastname, int(mobile_number), date_of_birth)]

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
