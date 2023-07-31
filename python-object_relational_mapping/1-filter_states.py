#!/usr/bin/python3

"""This modlists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usaule"""
import sys
import MySQLdb

"""Function Definition"""


def states_filter(username, password, database_name):
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

        query = "Select * FROOM states WHERE name LIKE 'N%' ORDER BY id ASC"
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
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    states_filter(username, password, database_name)
