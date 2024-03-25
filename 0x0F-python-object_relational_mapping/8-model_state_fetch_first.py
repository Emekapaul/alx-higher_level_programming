#!/usr/bin/python3
"""Write a script that prints the first State object from
the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """Main function"""
    try:
        dburl = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
        engine = create_engine(dburl, pool_pre_ping=True)

        Session = sessionmaker(bind=engine)

        with Session() as session:
            inst = session.query(State).first()
            if inst is not None:
                print(f"{inst.id}: {inst.name}")
            else:
                print('Nothing')

    except Exception as e:
        print(f'An error occured: {e}')


if __name__ == "__main__":
    main()
