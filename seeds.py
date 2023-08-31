from models import User 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker

fake = Faker()

import ipdb;

if __name__ == "__main__":
    engine = create_engine("sqlite:///main.db")

    Session= sessionmaker(bind=engine)
    session= Session()



#Use faker to seed data for user table
for _ in range(10):

    user= User(name= fake.name(), email= fake.ascii_company_email())
    print(user)
    session.add(user)
    session.commit()

items= ["Keys",
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

ipdb.set_trace()
