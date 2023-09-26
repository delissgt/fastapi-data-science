# Instantiate several objects, to setup the connection between our FastAPI app and the database engine.
import sqlalchemy
from databases import Database


DATABASE_URL = "sqlite:///chapter6_sqlalchemy.db"  # set connection string.
# Generally is database engine followed by authentication information and the hostname of database server.

database = Database(DATABASE_URL)  # we instantiate a Database instance
# connection layer provided by databases that will allow us to perform asynchronous queries

sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)  # standard synchronous connection object provided by SQLAlchemy
# that it constitutes an overlap with database.

# function that simply return the database instance
# use this function as a dependency to retrieve this instance in our path operation functions
def get_database() -> Database:
    return database
