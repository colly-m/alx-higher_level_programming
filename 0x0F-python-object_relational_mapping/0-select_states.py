#!/usr/bin/python3
"""Script to list states with names starting with 'N' from a database"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Accesses the database server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = db.cursor()

    query = 'SELECT * FROM states'
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)
