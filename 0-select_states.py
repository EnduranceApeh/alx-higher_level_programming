#!/usr/bin/python3
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="root", port=3306, passwd="", database="hbtn_0e_0_usa")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM  states")

    for state in cursor:
        print(state)
