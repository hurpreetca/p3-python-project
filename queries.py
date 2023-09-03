from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import yellow
from models import User, Item


engine = create_engine("sqlite:///db/habittracker.db")
Session = sessionmaker(bind=engine)
session = Session()


def find_by_item_name(text):
    query = session.query(Item).filter(Item.item_name.like(f"%{text}"))
