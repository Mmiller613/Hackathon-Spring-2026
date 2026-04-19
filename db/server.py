"""server.py: connect to Postgre database and create tables"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env
load_dotenv()

Base = declarative_base()

# database values
# defaults to localhost for local dev
db_host = os.getenv('db_host','localhost')
# defaults to local port where postgres svr running
db_port = os.getenv('db_port','5432')
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url)

PostgresSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_session():
    """Get database session"""
    return PostgresSession()

def init_database():
    """Initialize database tables"""
    try:
        # Import all of the tables
        from db.schema.advisor import Advisor
        from db.schema.advisorcourse import Advisorcourse
        from db.schema.course import Course
        from db.schema.degree import Degree
        from db.schema.minor import Minor
        from db.schema.student import Student
        from db.schema.studentadvisor import Studentadvisor
        from db.schema.studentcourse import Studentcourse
        from db.schema.studentdegree import Studentdegree
        from db.schema.studentminor import Studentminor

        # Create all of the tables
        Base.metadata.create_all(bind=engine)
        print(f"\n\n----------- Connection successful!")
        print(f" * Connected to {db_name}")
        print(f" * Successfully created DB tables!")
        return True
    except Exception as error:
        print(f"\n\n----------- Connection failed!")
        print(f" * Unable to connect to {db_name}")
        print(f" * ERROR: {error}")
        return False