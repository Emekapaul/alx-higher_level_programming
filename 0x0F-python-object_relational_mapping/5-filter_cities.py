#!/usr/bin/python3
"""Write a script that takes in the name of a state as an
argument and lists all cities of that state, using the
database hbtn_0e_4_usa"""
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
        SELECT cities.name
        FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC""", (argv[4],))

    query_rows = cur.fetchall()

    cities = ', '.join(row[0] for row in query_rows)
    print(cities)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
