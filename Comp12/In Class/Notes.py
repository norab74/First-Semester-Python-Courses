'''What is a database?
        A database is a data agnostic file in which we store data in tables.
        
        A database has a Schema, a file which defines how data is formatted in the database

SQLite3: Included with python installation
    SQLite3 is serverless, this doesn't mean it can't be used in a server environment.
    SQLite3 will store all data in a single file. Consider your Jellyfin library,
        it uses 8 separate SQLite3 databases because the datatypes it hosts need more than just one

The textbook was written with SQLite in mind, all references to it should be changed to SQLite3

SQL = Structured Query Language
Remember CRUD
        Create rows of data in a table
        Read data from tables
        Update data in tables
        Delete data from tables
        
        
Databases may be managed with code, as done in our demos, or Databases may be manually managed with a SQL Database Browser
'''