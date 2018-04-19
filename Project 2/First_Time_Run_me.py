# Run before main program to build database table if it is not already included.

import sqlite3

db = sqlite3.connect('employees.db')
db.execute("""create table Employee (
           name text,
           position text,
           hours real,
           payrate real
           )""")

db.commit()

db.close()