#!/usr/bin/python3
"""Write a script that adds the State object “Louisiana” to
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
            session.add(State(name='Louisiana'))
            session.commit()

            inst = session.query(State).filter(
                State.name == 'Louisiana').first()
            print(f"{inst.id}")

    except Exception as e:
        print(f'An error occured: {e}')


if __name__ == "__main__":
    main()
