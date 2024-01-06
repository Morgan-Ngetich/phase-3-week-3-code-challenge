from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base
from .review import Review
from .customer import Customer
from . import Session

# Restaurant class definition
class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    
    reviews = relationship("Review", back_populates="restaurant")

    # Representaion of Restaurant object
    def __repr__(self):
      return f"<Restaurant: {self.name}>"
      
    # Returns all the customers who reviewed the Restaurant
    def customers(self):
      return [review.customer for review in self.reviews]   

    # Returns the fanciest Restaurant based on price
    @classmethod
    def fanciest(cls, session):
      session = Session()
      fanciest_restaurant = session.query(cls).order_by(cls.price.desc()).first()
      return fanciest_restaurant

    # Returns all the reviews for the Restaurant
    def all_reviews(self):
      return [f"Review for ({self.name}) by ({review.customer.full_name()}): [{review.star_rating}] stars." for review in self.reviews]

    # Returns a collection of all the reviews for the Restaurant
    def restaurant_reviews(self):
      return self.reviews  # Return a collection of all the reviews for the Restaurant


