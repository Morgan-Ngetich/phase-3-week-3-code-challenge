from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base
from .review import Review
from . import Session

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    
    reviews = relationship("Review", back_populates="restaurant")

    def __repr__(self):
      return f"<Restaurant: {self.name}>"
      
    def customers(self):
      return [review.customer for review in self.reviews]   

    @classmethod
    def fanciest(cls, session):
      session = Session()
      fanciest_restaurant = session.query(cls).order_by(cls.price.desc()).first()
      return fanciest_restaurant

    def all_reviews(self):
      return [f"Review for ({self.name}) by ({review.customer.full_name()}): [{review.star_rating}] stars." for review in self.reviews]
