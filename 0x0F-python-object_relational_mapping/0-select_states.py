#!/usr/bin/python3
"""
 a script that lists all states from the database hbtn_0e_0_usa
 parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            database=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM  states ORDER BY id ASC")
    for state in cursor:
        print(state)
    cursor.close()
    db.close()
