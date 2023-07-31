#!/usr/bin/python3

"""This script takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""

import sys
import MySQLdb

"""Function Definition"""


def my_states_filter(username, password, database_name, state_name_searched):
    """ Setting connection to the MySQL server """
    try:
        conn = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database_name,
            host='localhost',
            port=3306
        )

        cur = conn.cursor()

        query = """SELECT *
                FROM states
                WHERE name = '{}'
                ORDER BY id ASC
            """.format(state_name_searched)
        cur.execute(query)

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
    if len(sys.argv) != 5:
        print("""Usage: python my_filter_states.py <username>
              <password> <db_name> <state_name_searched>""")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    my_states_filter(username, password, database_name, state_name_searched)
