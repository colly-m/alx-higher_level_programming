#!/usr/bin/python3
"""Script to display all values in 'state' table of 'hbtn_0e_0_usa'
where 'name' matches argument and is safe from injection
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connects to database server"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()

    query = 'SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY id ASC'
    cursor.execute(query, {'name': argv[4]})

    rows = cursor.fetchall()

    for row in rows:
        print(row)
