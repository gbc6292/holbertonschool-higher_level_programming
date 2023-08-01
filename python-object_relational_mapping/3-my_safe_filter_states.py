#!/usr/bin/python3

"""This script takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=passwd,
        db=db
    )

    cur = conn.cursor()
    protected = (state_name,)
    query = """SELECT * FROM states
            WHERE name LIKE BINARY %s
            """.format(protected)

    cur.execute(query, protected)
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    conn.close()
