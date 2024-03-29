#!/usr/bin/python3

"""Script that lists all cities from
   the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities \
          JOIN states ON cities.state_id = states.id ORDER BY cities.id""")

    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    conn.close()
