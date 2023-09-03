from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database connection
DATABASE_URI = 'sqlite:///restaurant.db'
engine = create_engine(DATABASE_URI, echo=True)

# Define the base class for all the classes
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, Sequence('restaurant_id_seq'), primary_key=True)
    name = Column(String(255))
    price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))  


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, Sequence('review_id_seq'), primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rating = Column(Integer)
    comment = Column(Text)

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")      

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Make the restaurant instances
restaurant1 = Restaurant(name="Kempinsky", price=2)
restaurant2 = Restaurant(name="Hilton", price=3)
session.add(restaurant1)
session.add(restaurant2)

# Create some customers
customer1 = Customer(first_name="Ibrahim", last_name="Moh")
customer2 = Customer(first_name="Zlatan", last_name="Adm")
session.add(customer1)
session.add(customer2)

session.commit()
