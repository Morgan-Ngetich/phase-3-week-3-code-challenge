from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an engine
engine = create_engine('sqlite:///mydatabase.db') 

# Bind the engine to a sessionmaker
Session = sessionmaker(bind=engine)

# Create a Base class for declarative models
Base = declarative_base()

from .base import Base
from .customer import Customer
from .restaurant import Restaurant
from .review import Review
