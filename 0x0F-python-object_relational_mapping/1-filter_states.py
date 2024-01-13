#!/usr/bin/python3
"""Script lists all states names starting with 'N' from
'hbtn_0e_0_usa' database
"""


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

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
