#!/usr/bin/python3
"""Script to list all 'cities' from database 'hbtn_0e_4_usa'"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Accesses database server"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()

    query = 'SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id \
                = states.id ORDER BY cities.id ASC'
    cursor.execute(query)

    rows = cursor.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
