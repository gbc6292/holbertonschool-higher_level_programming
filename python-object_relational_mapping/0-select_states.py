#!/usr/bin/python3

import sys
import MySQLdb
"""Script that lists all states from the database hbtn_0e_0_usa"""


"""Main function"""


def states_list(username, password, database_name):
    try:
        """ Setting connection to the MySQL server """
        conn = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database_name,
            host='localhost',
            port=3306
        )
        """Creating cursor to execute queries"""
        cur = conn.cursor()

        """Execute query"""
        query = 'SELECT * FROM states ORDER BY id ASC'
        cur.execute(query)

        """Fetch all the rows returned by the query"""

        rows = cur.fetchall()

        """Process and print the data"""

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print('Error:', e)

    finally:

        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    states_list(username, password, database_name)
