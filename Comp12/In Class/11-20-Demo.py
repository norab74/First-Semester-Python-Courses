#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect("NewDatabase.db") #This will create a database file if it does not already exist
curs = conn.cursor() #sqlite3 needs a cursor within the db to actually get anything done


#when we want to execute a SQL command, we must pass the SQL command to curs.execute() as a string
    #curs.execute('''
    #               SQL,
    #               COMMANDS,
    #               HERE''')
    
    
    