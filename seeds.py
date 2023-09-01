from models import User, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

from faker import Faker

fake = Faker()

import ipdb;

if __name__ == "__main__":
    engine = create_engine("sqlite:///main.db")

    Session= sessionmaker(bind=engine)
    session= Session()

    #Deleting the existing data before seeding again
    session.query(User).delete()
    session.query(Item).delete()

###########################################################################################################

#Use faker to seed data for User table
for _ in range(20):

    user= User(name= fake.name(), email= fake.ascii_company_email())
    print(user)
    session.add(user)
    session.commit()

###########################################################################################################


ITEMS= ["Keys",
        "Wallets",
        "Phones",
        "Sunglasses",
        "Umbrellas",
        "Headphones",
        "Jewelry",
        "Documents",
        "Chargers",
        "Gloves",
        "Scarves",
        "Hats",
        "Books",
        "Pens",
        "Water Bottles",
        "Lunch Boxes",
        "Laptops/Tablets",
        "Cameras",
        "Chapsticks",
        "Flash Drives",
        "Medication"
        ]

STATUS= ["Claimed", "Unclaimed"]
item = Item(item_name= random.choice(ITEMS),status= random.choice(STATUS) )
print(item)
ipdb.set_trace()
