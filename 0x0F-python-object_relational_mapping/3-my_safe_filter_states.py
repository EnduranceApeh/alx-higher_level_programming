#!/usr/bin/python3
"""
a script that list all state with a name startinmg with N
paThis script recieve three paarameterer: udername, passd and database name
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
    sql_cmd = """SELECT *
    FROM states
    WHERE name=%s ORDER BY id ASC"""

    cursor.execute(sql_cmd, (argv[4],))
    states = cursor

    for state in states:
        print(state)

    cursor.close()
    db.close()
