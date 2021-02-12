import getpass
import mysql.connector
from mysql.connector import Error
import os

username_str = input("Enter your db username: ")
password_str = getpass.win_getpass()
db_name = input("Enter db name ")

conn = None


def initialize_connection():
    try:
        global conn
        conn = mysql.connector.connect(
            host='localhost',
            user=username_str,
            password=password_str
        )
        print('connection successful')
        if conn.is_connected():
            sql = f'CREATE DATABASE IF NOT EXISTS {db_name}'
            conn.cursor().execute(sql)
            print(f"{db_name} created successfully")
            return conn
    except Error as connection_error:
        print("Connection failed due to ", connection_error)


def close_connection():
    if conn is not None and conn.is_connected:
        conn.close()

        print("Connection closed ...")


def create_tables():
    queries = [
        '''
        CREATE TABLE IF NOT EXISTS Customer(
        customerId integer not null AUTO_INCREMENT,
        firstname varchar(200) not null,
        lastname varchar(200) not null,
        middlename varchar(200),
        mobilenumber varchar (40) unique,
        occupation varchar (40),
        date_of_birth date,
        constraint customer_pk primary key (customerId)
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS Account (
        accountnumber integer not null AUTO_INCREMENT,
        customerId integer not null,
        accounttype varchar(50),
        accountstatus varchar(50),
        account_opening_date Date default(current_date),
        constraint  account_pk primary key(accountnumber),
        constraint account_fk foreign key(customerId) references customer(customerId) on delete cascade 
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS Transactions (
        transactionId integer not null AUTO_INCREMENT,
        accountnumber integer not null,
        transactiondate date default(current_date),
        transactiontype varchar(50) not null,
        transactionamount integer not null,
        transactionmedium varchar (50) not null,
        constraint transactions_pk primary key(transactionId),
        constraint transactions_fk foreign key(accountnumber) references account(accountnumber) on delete cascade 
        )
        '''
    ]
    for query in queries:
        conn.cursor().execute(query)

# initialize_connection()
# use_database()
# create_tables()
# close_connection()
