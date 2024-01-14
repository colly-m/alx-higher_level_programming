#!/usr/bin/python3
"""
Script to get name of states as argument and list all cities
of the statefrom database 'hbtn_0e_4_usa'
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

    query = """
            SELECT cities.id, cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %(state_name)s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, {'state_name': argv[4]})

    rows = cursor.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
