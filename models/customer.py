# customer.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .review import Review
from . import Session

# Customer class definition
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship("Review", back_populates="customer")

    # Representation of Customer object
    def __repr__(self):
        return f"<Customer: {self.first_name} {self.last_name}>"

    # Concatenates the first and last name of the customer
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Returns the favourite restaurant of the customer
    def favorite_restaurant(self):
        rated_reviews = [review for review in self.user_reviews() if review.star_rating is not None]
        if rated_reviews:
            return max(rated_reviews, key=lambda review: review.star_rating).restaurant
        return None

    # Adds a new review for the customer
    def add_review(self, restaurant, rating, session):
        new_review = Review(customer_id=self.id, restaurant=restaurant, star_rating=rating)          
        session.add(new_review)   # Add the new review directly to the session
        session.commit()

    # Deletes all reviews for a specific restaurant belonging to the customer
    def delete_reviews(self, restaurant, session):
        session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).delete()
        session.commit()
        
    # Returns all reviews left by this Customer
    def user_reviews(self):
        return self.reviews 

    # Returns all reviews left by this Customer using a session
    def get_user_reviews(self, session):        
        return session.query(Review).filter_by(customer_id=self.id).all()

    # Returns all the restaurants reviewed by this Customer using a session
    def user_restaurants(self, session):        
        reviews = session.query(Review).filter_by(customer_id=self.id).all()
        return [review.restaurant for review in reviews]

    