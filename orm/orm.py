from sqlalchemy.orm import registry ,Session,sessionmaker 
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,ForeignKey
from model import *
db_url="sqlite:///fouth1.db"
engine=create_engine(url=db_url)


mapper_registry=registry()
SessionFactory=sessionmaker(bind=engine)


batch_table=Table(
    'batch',mapper_registry.metadata,
    Column('id',Integer,primary_key=True),
    Column('sku',String,unique=True),
    Column('reference',String),
    Column('available_qty',Integer)
)
mapper_registry.map_imperatively(Batch,batch_table)

orderline_table=Table(
    'orderline',
    mapper_registry.metadata,
    Column('id',Integer,primary_key=True),
    Column('sku',String,unique=True),
    Column('qty',Integer,)
)

mapper_registry.map_imperatively(
    OrderLine,orderline_table
)

mapper_registry.metadata.create_all(engine)