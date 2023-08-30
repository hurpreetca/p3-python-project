from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id= Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String(55), nullable=False)

    item= relationship("Item", backref= "user")

    def __repr__(self):
        return (
            f"<User: id= {self.id}, \n"
            f"name= '{self.name}', \n"
            f"email= '{self.email}>\n\n"
        )

class Item(Base):
    __tablename__ = 'items'

    id= Column(Integer, primary_key=True)
    item_name= Column(String, nullable=False)
    status= Column(String(10))
    found_by= Column(String)
    claimed_by= Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"\n<Item " \
            + f"id={self.id}, " \
            + f"item_name={self.item_name}, " \
            + f"status={self.status}, " \
            + f"found_by={self.found_by}, " \
            + f"claimed_by={self.claimed_by}, " \
            + ">"
    

