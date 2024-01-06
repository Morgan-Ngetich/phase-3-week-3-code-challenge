from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Restaurant, Review, engine

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create some customers
john = Customer(first_name='John', last_name='Doe')
alice = Customer(first_name='Alice', last_name='Smith')
session.add_all([john, alice])
session.commit()

# Create some restaurants
restaurant_1 = Restaurant(name='Restaurant One')
restaurant_2 = Restaurant(name='Restaurant Two')
session.add_all([restaurant_1, restaurant_2])
session.commit()

# Add reviews for customers and restaurants
review1 = Review(customer=john, restaurant=restaurant_1, star_rating=4)
review2 = Review(customer=john, restaurant=restaurant_2, star_rating=3)
review3 = Review(customer=alice, restaurant=restaurant_1, star_rating=5)
session.add_all([review1, review2, review3])
session.commit()

# Fetch the first customer
first_customer = session.query(Customer).first()

# Test the new methods
# Test the full_name method
print("Full name of the first customer:")
print(first_customer.full_name())

# Test the favorite_restaurant method
print("\nFavorite restaurant for the first customer:")
fav_restaurant = first_customer.favorite_restaurant()
if fav_restaurant:
    print(fav_restaurant.name)
else:
    print("No reviews found for this customer.")

# Test the add_review method
new_restaurant = Restaurant(name='New Restaurant')
session.add(new_restaurant)
session.commit()
first_customer.add_review(new_restaurant, 5, session)
print("\nReviews for the first customer after adding a new review:")
print([review.star_rating for review in first_customer.reviews])

# Test the delete_reviews method
first_customer.delete_reviews(restaurant_1, session)
print("\nReviews for the first customer after deleting all reviews for Restaurant One:")
print([review.star_rating for review in first_customer.reviews])

# Fetch the first restaurant
first_restaurant = session.query(Restaurant).first()

# Test the all_reviews method
print("\nAll reviews for the first restaurant:")
print(first_restaurant.all_reviews())

# Test the fanciest method
fanciest_restaurant = Restaurant.fanciest(session)
if fanciest_restaurant:
    print(f"\nThe fanciest restaurant is: {fanciest_restaurant.name}")
else:
    print("No restaurants found.")

# Test the full_review method for the first review of the first restaurant
first_review = first_restaurant.reviews[0]
print("\nFull review for the first review of the first restaurant:")
print(first_review.full_review())
