from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:password@localhost:3306/AddressBookORM')
Base = declarative_base()
