import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("Student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()


# Create the Student table
table_info="""
CREATE TABLE Student (
    Id INTEGER NOT NULL PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    age INTEGER
);

"""

# create database
cursor.execute(table_info)

## Insert all records

cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (1, 'Jim', 'Pierre', 'Jim@gmail.com', 10)''')
cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (2, 'Harry', 'Kravchuck', 'Harry@gmail.com', 9)''')
cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (3, 'Anthony', 'Cruz', 'Anthony@gmail.com', 8)''')
cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (4, 'Raymond', 'Carr', 'Raymond@gmail.com', 10)''')
cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (5, 'Gardinson', 'Jean', 'Gardinson@gmail.com', 9)''')

cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (6, 'Oscar D', 'Martinez JR.', 'Oscar D@gmail.com', 8)''')
cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (7, 'Kane', 'Williams', 'Kane@gmail.com', 10)''')
cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (8, 'Christian', 'Posada', 'Christian@gmail.com', 9);''')
cursor.execute('''INSERT INTO Student (Id, firstName, lastName, email, age) VALUES (9, 'Terry', 'Kemp', 'Terry@gmail.com', 8)''')


## Display all the records

print("The records are :")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()

## close your connection
connection.close()