from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import environ


# Database
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

engine = create_engine('mysql+pymysql://Super_User:SuperX1234'
                       '@mysql-13101-0.cloudclusters.net:13101/SuperX',
                       echo=False)
SessionLocal = sessionmaker(autocommit=False,bind=engine)

db_session = scoped_session(sessionmaker(autocommit=False,  bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()