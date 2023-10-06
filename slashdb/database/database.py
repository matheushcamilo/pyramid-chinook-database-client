from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///development.db")
DBSession = sessionmaker(bind=engine)
