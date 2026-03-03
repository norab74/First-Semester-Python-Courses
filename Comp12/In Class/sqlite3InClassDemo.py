#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect("NewDatabase.db") #This will create a database file if it does not already exist
curs = conn.cursor() #sqlite3 needs a cursor within the db to actually get anything done

#Do stuff using curs.execute('''stuff
#                               To Do
#                               Here''')
curs.execute('''
             CREATE TABLE IF NOT EXISTS students(
             id   INT,
             name   TEXT,
             age    INT)
             '''
             
             ) #Just a note, this could all be done on one line, using spaces instead of tabs. SQL doesn't give two shits about whitespace... usually.
#Lets make a simple list as a demo
dataToInsert = [(1, 'Alice', 19),
                (2, 'Bobert', 20),
                (3, 'Calcifer', 999),
                (4, 'Darmok', 10)]

#Let's insert that data into our table
curs.executemany('''
             INSERT INTO students
             VALUES (?,?,?)''',dataToInsert
             )



#Let's create a second table, if there was only one, a Database wouldn't make sense
curs.execute('''
             CREATE TABLE IF NOT EXISTS cowabunga(
             name   TEXT,
             color  TEXT,
             age    TEXT,
             species    TEXT)
             ''')
tmnt = [('Donatello', 'Purple', 'Teen', 'Turtle'),
        ('Leonardo', 'Red', 'Teen', 'Turtle'),
        ('Michaelangelo', 'Orange', 'Teen', 'Turtle'),
        ('Raphael', 'Red', 'Teen', 'Turtle')]
#Fill our table
curs.executemany('''
                 INSERT INTO cowabunga
                 VALUES (?,?,?,?)''',tmnt)

#Delete an entry
curs.execute('''
             DELETE FROM cowabunga
             WHERE name = 'Raphael'
             ''')


conn.commit() #commit changes to the database

#Great, now that we've added data, let's print it
curs.execute("SELECT * FROM Students")
rows = curs.fetchall()
print ("Students: ")
for row in rows:
    print(row)
    
curs.execute("SELECT * FROM cowabunga")
rowtmnt = curs.fetchall()
print ("Remaining Ninjas: ")
for row in rowtmnt:
    print(row)

conn.close() #This should automatically happen, but calling it explicitly mitigates potential security issues related to SQL injection, the unauthorized and usually malicious use of SQL patterns in unsanitized inputs. For example, in the instance that the server application is killed in a non-graceful fashion, a potential bad actor may still have their local instance open, with bidirectional sockets still active. In this situation, there is no middle man to sanitize inputs, therefore a properly formatted escape sequence within a text box could allow for SQL injection which could drop tables, or other potential problems.

