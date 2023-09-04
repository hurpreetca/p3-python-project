from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import yellow, blue, red
from models import User, Item


engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


def lost_item_list(status):
    query = session.query(Item).filter_by(status=status).all()
    print(red("All lost Items: \n"))
    return query


def found_item_list(status):
    query = session.query(Item).filter_by(status=status).all()
    print(yellow("All found Items: \n"))
    return query


def claimed_item_list(final_status):
    query = session.query(Item).filter_by(final_status=final_status).all()
    print(blue("All claimed Items: \n"))
    return query


def handle_item_claim(item_name):
    query = session.query(Item).filter_by(item_name=item_name).limit(2).all()
    user_id = query[0].user_id
    query[0].final_status = "Resolved"
    if query[1].user_id != user_id:
        query[1].final_status = "Resolved"

    session.commit()

    # flag = 0
    # for i in range(2):
    #     if user_id == query[i].user_id:
    #
    #         flag = 1
    #     if flag == 0:

    #         break
    #     else:
    #         continue
