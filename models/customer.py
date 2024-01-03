# customer.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .review import Review
from . import Session

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return f"<Customer: {self.first_name} {self.last_name}>"

    def add_review(self, restaurant, rating, session):        
        new_review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant, session):        
        reviews_to_delete = session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).all()
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

    def get_reviews(self, session):        
        return session.query(Review).filter_by(customer_id=self.id).all()

    def restaurants(self, session):        
        reviews = session.query(Review).filter_by(customer_id=self.id).all()
        return [review.restaurant for review in reviews]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, session):        
      rated_reviews = session.query(Review).filter(Review.customer_id == self.id, Review.star_rating != None).all()
      if not rated_reviews:
        return None
      return max(rated_reviews, key=lambda review: review.star_rating).restaurant