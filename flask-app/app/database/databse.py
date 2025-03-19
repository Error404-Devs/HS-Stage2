from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define SQLite database file
DATABASE_URL = "sqlite:///raspberry_pi.db"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Define base class for ORM models
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session factory
SessionLocal = sessionmaker(bind=engine)
