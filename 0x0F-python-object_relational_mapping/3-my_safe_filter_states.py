#!/usr/bin/python3
"""Write a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    cur.execute("""
        SELECT *
        FROM states
        WHERE states.name LIKE BINARY %s
        ORDER BY states.id ASC""", (argv[4],))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
