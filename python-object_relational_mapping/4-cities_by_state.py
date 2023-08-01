#!/usr/bin/python3

"""Script that lists all cities from
   the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        db=db,
        user=username,
        password=passwd
    )

    cur = conn.cursor()
    query = """SELECT * FROM cities
                ORDER BY id ASC""".format(argv[3])
    cur.execute(query, argv[3])

    cities = cur.fetchall()
    for city in cities:
        print(city)

        cur.close()
        conn.close()
