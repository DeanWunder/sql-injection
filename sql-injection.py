import sqlite3

connection = sqlite3.connect('sql-injection.py')
cursor = connection.cursor()

username = input('Username: ')
password = input('Password: ')

query = 'SELECT * FROM `users` WHERE `username` = %s AND `password` = %s'
query = query % (username, password)
print('The query being sent to the database is:')
print(query)

cursor.execute(query)
print('The query has successfully been executed.')
