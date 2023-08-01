#!/usr/bin/python3

"""script that takes in the name of
a state as an argument and lists all
cities of that state, using the
database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state = argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        password=passwd,
        db=db
    )

    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities \
          JOIN states ON cities.state_id = states.id WHERE \
                states.name LIKE %s ORDER BY cities.id""", (state,))

    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))

    cur.close()
    conn.close()
