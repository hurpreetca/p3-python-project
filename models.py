from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


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

    @classmethod
    def find_user_by_email(cls, email):
        user = session.query(cls).filter(cls.email == email).first()
        return user

    @classmethod
    def create_user(cls, name, email):
        user = cls(name=name, email=email)

        session.add(user)
        session.commit()
        return user


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
            + f"final_status={self.final_status} "
            + ">"
        )

    @classmethod
    def add_item(cls, item_name, status, final_status, user_id):
        item = cls(
            item_name=item_name,
            status=status,
            final_status=final_status,
            user_id=user_id,
        )
        session.add(item)
        session.commit()

        return item
