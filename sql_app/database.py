###Import the necessary python libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

###Create the connection to the postgresql database
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<host/url>/<database-name>"
###Connect to the database utilizing sqlalchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
