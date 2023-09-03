from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import yellow
from models import User, Item


engine = create_engine("sqlite:///db/habittracker.db")
Session = sessionmaker(bind=engine)
session = Session()


def new_user(name, email):
    new_user_instance = User(name=name, email=email)
    session.add(new_user_instance)
    session.commit()
    return new_user_instance


def check_email(email):
    return session.query(User).filter_by(email=email).first() == None


def find_by_email(email):
    return session.query(User).filter_by(email=email).first()


def handle_lost_item(item_name, user_id, status, final_status):
    new_lost_item = Item(
        item_name=item_name, user_id=user_id, status="Lost", final_status="Unresolved"
    )
    session.add(new_lost_item)
    session.commit()
    print(yellow("Item Reported Successfully!"))


def find_by_item_name(self, text):
    query = session.query(Item).filter(Item.item_name.like(f"%{text}"))
    return query.all()


def lost_item_list(status="Lost"):
    query = session.query(Item).filter_by(status=status).all()


def found_item_list(status="Found"):
    query = session.query(Item).filter_by(status=status).all()


def claimed_item_list(final_status="Resolved"):
    query = session.query(Item).filter_by(final_status=final_status).all()
