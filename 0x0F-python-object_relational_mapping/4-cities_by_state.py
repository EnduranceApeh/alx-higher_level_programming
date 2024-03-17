#!/usr/bin/python3
"""
a script that list all cities frm database
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
    sql_cmd = """SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(sql_cmd)
    cities = cursor

    for city in cities:
        print(city)

    cursor.close()
    db.close()
