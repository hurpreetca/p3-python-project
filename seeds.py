from models import User 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker

fake = Faker()

import ipdb;


engine = create_engine("sqlite:///main.db")

Session= sessionmaker(bind=engine)
session= Session()



#Use faker to seed data for user table
for _ in range(10):

    user= User(name= fake.name(), email= fake.ascii_company_email())
    print(user)



ipdb.set_trace()
