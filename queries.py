from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import yellow
from models import User, Item


engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


# def new_user(name, email):
#     new_user_instance = User(name=name, email=email)
#     session.add(new_user_instance)
#     session.commit()
#     return new_user_instance


@classmethod
def handle_report_item(cls, name, email, item_name, status, final_status):
    # Create a new User instance
    new_user = cls(name=name, email=email)

    # Create a new Item instance associated with the user
    new_item = Item(
        item_name=item_name, status=status, final_status=final_status, user=new_user
    )

    # Add both the User and Item instances to the session and commit the changes
    session.add(new_user)
    session.add(new_item)
    session.commit()


def check_email(email):
    return session.query(User).filter_by(email=email).first() == None


def find_by_email(email):
    return session.query(User).filter_by(email=email).first()


def handle_lost_item(item_name, user_id, status, final_status):
    new_lost_item = Item(
        item_name=item_name, user_id=user_id, status=status, final_status=final_status
    )
    session.add(new_lost_item)
    session.commit()
    print(yellow("Item Reported Successfully!"))


def find_by_item_name(self, text):
    query = session.query(Item).filter(Item.item_name.like(f"%{text}"))
    return query.all()


def lost_item_list(status):
    query = session.query(Item).filter_by(status="Lost").all()


def found_item_list(status):
    query = session.query(Item).filter_by(status="Found").all()


def claimed_item_list(final_status):
    query = session.query(Item).filter_by(final_status="Resolved").all()
