from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    star_rating = Column(Integer)  # Add the star_rating column

    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    def __repr__(self):
      return f"<Review by Customer {self.customer_id}: {self.star_rating} stars>"

    def full_review(self):
      return f"Review for ({self.restaurant.name}) by ({self.customer.full_name()}): [{self.star_rating}] stars."