#!/usr/bin/python3
import sys
import MySQLdb
"""Script that lists all states from the database hbtn_0e_0_usa"""


"""Main function"""


def states_list(username, password, database_name):
    """ Connection to the MySQL server """
    database = MySQLdb.connect(
        host='localhost',
        username=username,
        password=password,
        db=database_name,
        port=3306
    )

    cursor = database.cursor()

    try:
        rows = cursor.execute('SELECT * FROM states ORDER BY id ASC')
        for row in rows:
            print(row)

    except Exception as e:
        print('Error:', e)

    finally:
        cursor.close()
        database.close()
