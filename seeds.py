from models import User 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb
from faker import Faker

fake = Faker()

ipdb.set_trace()


engine = create_engine("sqlite:///main.db")

Session= sessionmaker(bind=engine)
session= Session()



# #Use faker to seed data for user table
# for _ in range(10):

#     user= User(firstname= fake.first_name(), lastname= fake.last_name(), email= fake.ascii_company_email())
#     print(user)