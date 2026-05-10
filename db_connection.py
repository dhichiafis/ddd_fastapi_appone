from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from dataclasses import dataclass
from datetime import datetime 
from dataclasses import dataclass
from datetime import datetime 

from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


Base=declarative_base()


db_url="sqlite:///first1.db"


engine=create_engine(url=db_url)

SessionFactory=sessionmaker(bind=engine,autoflush=False,)

def connect():
    db=SessionFactory()
    try:
        yield db 
    finally:
        db.close()






