from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String(55), nullable=False)

    item = relationship("Item", backref="users")

    def __repr__(self):
        return (
            f"<User: id= {self.id}, \n"
            f"name= '{self.name}', \n"
            f"email= '{self.email}>\n\n"
        )


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    status = Column(String(10))
    final_status = Column(String(20))

    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return (
            f"\n<Item "
            + f"id={self.id}, "
            + f"item_name={self.item_name}, "
            + f"item_status={self.status}, "
            + f"final_status={self.final_status}, "
            + ">"
        )
