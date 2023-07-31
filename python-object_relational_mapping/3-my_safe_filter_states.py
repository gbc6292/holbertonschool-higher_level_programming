#!/usr/bin/python3

"""This script takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""

import sys
import MySQLdb

"""Function Definition"""


def my_states_filter(state_name):
    """ Setting connection to the MySQL server """
    try:
        conn = MySQLdb.connect(
            user='username',
            passwd='password',
            db='database_name',
            host='localhost',
            port=3306
        )

        cur = conn.cursor()

        query = """SELECT *
                FROM states
                WHERE BINARY name = '{}'
                ORDER BY id ASC
            """.format(state_name)
        cur.execute(query, (state_name,))

        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print('Error', e)

    finally:
        if 'cur' in locals():
            cur.close()

        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python_script.py <state_name>")
        sys.exit(1)

    state_name = sys.argv[1]

    my_states_filter(state_name)
