#BellP12 Supplemental
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To generate a database file in spec with the geopoint project

'''
db_Initializer.py
=================
Simple Database initialization script for the Geopoint distance calculator

This script:
    -Creates a SQLite database and populates it with data from a supplied CSV
    file matching the name 'Points.csv'
    
Tables Created:
    -Points: Stores location data (latitude, longitude, point descriptor)

Possible Manual Intervention Needed:
    -Towards the bottom of this script, under `if __name__ == "__main__":`
        There is a line beginning with `populate_points`:
        You may need to update this line such that `Points.csv` is replaced
        with the absolute path of your copy of `Points.csv`
'''

import sqlite3
import csv

def get_connection():
    '''
    Establish and return a connection to the SQLite database, create it if
    it does not exist
    '''
    return sqlite3.connect('Points.db')

def create_tables(cursor):
    '''
    Create required tables in the database if they do not already exist
    
    Args:
        -cursor (sqlite3.Cursor): The cursor with which we will execute our
            queries
    Tables Created:
        -Points
            (
                point_number TEXT,
                point_descriptor TEXT,
                point_latitude TEXT,
                point_longitude TEXT
                )
    '''
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Points(
                    point_number TEXT,
                    point_descriptor TEXT,
                    point_latitude TEXT,
                    point_longitude TEXT   
                   )
    """)
    
def populate_points(cursor, csv_file):
    '''
    Populate the `Points` table using data from a CSV file.
    
    Args:
        cursor (sqlite3.Cursor): The cursor with which we will execute our
            queries
        csv_file (str): Path to the CSV file containing course data.
        
    CSV Format:
        Description,Latitude,Longitude
        
    Notes:
        -Uses INSERT OR IGNORE queries to avoid duplication
        -Prints an error if the CSV is not found.
    '''
    try:
        n=0
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                n += 1
                cursor.execute("""
                INSERT OR IGNORE INTO Points (
                    point_number,
                    point_descriptor,
                    point_latitude,
                    point_longitude)
                VALUES (?, ?, ?, ?)
                """,
                (n,
                 row['Description'],
                 row['Latitude'],
                 row['Longitude']
                 )
                )
    except FileNotFoundError:
        print(f"CSV file `{csv_file}` not found.")
        
if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    create_tables(cursor)
    populate_points(cursor, 'ExpandedPoints.csv')
    conn.commit()
    conn.close()