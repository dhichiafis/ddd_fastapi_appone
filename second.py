from sqlalchemy import Table,Column,Integer,ForeignKey,String,create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy.orm import registry

db_url="sqlite:///second.db"

engine=create_engine(url=db_url)

SessionFactory=sessionmaker(bind=engine,autoflush=False)

def connect():
    db=SessionFactory()
    try:
        yield db 
    finally:
        db.close()

mapper_registry=registry()


users_table=Table(
    'user',
    mapper_registry.metadata,
    Column('id',Integer,primary_key=True),
    Column('username',String,unique=True),
    Column('password',String)

)

class User:

    def __init__(self,username,password):
        self.username=username
        self.password=password


    def change_password(self,new_password):
        self.password=new_password
    


mapper_registry.map_imperatively(User,users_table)#expilcitly mapping our user to the table


# create actual tables in sqlite
mapper_registry.metadata.create_all(engine)
def create_user(username,password):
    session=SessionFactory()
    try:
        user=User(username=username,password=password)
        session.add(user)
        session.commit()
        print(user)
        return user 
    finally:
        session.close()

def retrieve_user():
    pass

def retrieve_all_users():
    session=SessionFactory()
    try:
        users=session.query(User).all()
        for user in users:
            print(user.username)
        return [user for user in users]
    finally:
        session.close()

create_user("ochieng","ochiengp")
create_user("odhiambo","odhiambop")
retrieve_all_users()