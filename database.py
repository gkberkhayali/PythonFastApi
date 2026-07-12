from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:TestDbPw@localhost:5432/postgres"
engine = create_engine(db_url, connect_args={"options": "-c search_path=PythonFastApi"}) 
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)