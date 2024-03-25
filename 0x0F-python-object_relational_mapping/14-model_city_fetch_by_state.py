#!/usr/bin/python3
"""Next, write a script 14-model_city_fetch_by_state.py that
prints all City objects from the database hbtn_0e_14_usa:"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


def main():
    """Main function"""
    try:
        dburl = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
        engine = create_engine(dburl, pool_pre_ping=True)

        Session = sessionmaker(bind=engine)

        with Session() as session:
            for city_obj, state_obj in session.query(City, State). \
                    join(State).order_by(City.id):
                print(f"{state_obj.name}: {city_obj.id} {city_obj.name}")

    except Exception as e:
        print(f'An error occured: {e}')


if __name__ == "__main__":
    main()
