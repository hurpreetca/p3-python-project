from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import yellow, blue, red
from models import User, Item


engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


def lost_item_list(status):
    query = session.query(Item).filter_by(status=status).all()
    return query


def found_item_list(status):
    query = session.query(Item).filter_by(status=status).all()
    return query


def claimed_item_list(final_status):
    query = session.query(Item).filter_by(final_status=final_status).all()
    return query
