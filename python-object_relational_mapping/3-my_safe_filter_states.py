#!/usr/bin/python3

"""This script takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""

import sys
import MySQLdb

"""Function Definition"""


def states_by_name(username, password, database, state_name):
    """ Setting connection to the MySQL server """
    try:
        conn = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            host='localhost',
            port=3306
        )

        cur = conn.cursor()
        query = """SELECT *
                FROM states
                WHERE BINARY name = %s
                ORDER BY id ASC
            """.format(state_name)

        cur.execute(query, (state_name,))
        results = cur.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print('Error', e)

        cur.close()
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("""Usage: python_script.py <mysql_username>
              <mysql_password> <database_name> <state_name>""")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = [4]

    states_by_name(username, password, database, state_name)
