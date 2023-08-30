from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id= Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    contact = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f"<User: id= {self.id}, \n"
            f"firstname= '{self.firstname}', \n"
            f"lastname= '{self.lastname}, \n"
            f"contact= '{self.contact}>\n\n"
        )


    

