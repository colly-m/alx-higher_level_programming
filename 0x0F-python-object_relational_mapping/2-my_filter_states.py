#!/usr/bin/python3
"""Script to display all values in 'states' table of 'hbtn_0e_0_usa'
where name matches argument
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Accesses the batabase server"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()

    query = 'SELECT * FROM states WHERE name LIKE BINARY "{}" ORDER BY \
                    states.id ASC'.format(argv[4])
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
