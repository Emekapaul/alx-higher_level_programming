#!/usr/bin/python3
"""Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:"""
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
        WHERE states.name LIKE BINARY 'N%'
        ORDER BY states.id ASC
        """)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
