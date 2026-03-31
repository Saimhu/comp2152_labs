import sqlite3
from function import query_executor, query_responder

# connect to database
connection = sqlite3.connect("sqlite.db")

# create cursor
cursor = connection.cursor()

# Query 1
query_executor(cursor, "SELECT * FROM demo")
query_responder(cursor, "fetchall")

# Query 2
query_executor(cursor, "SELECT * FROM demo")
query_responder(cursor, "fetchone")

# Query 3
query_executor(cursor, "SELECT * FROM demo")
query_responder(cursor, "fetchmany", 2)

# close connection
connection.close()