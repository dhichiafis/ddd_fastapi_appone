from sqlalchemy.orm import Session 

from model import *

#the repository is providing and abstraction of the database
class BatchRepository:
    def __init__(self,session):
        self.session=session

    def add(self,batch):
        self.session.add(batch)
    def get(self,reference):
        return self.session.query(Batch).filter(Batch.reference==reference).one()
    
    def list(self):
        return self.session.query(Batch).all()
    
class OrderLineRepository:
    def __init__(self,session):
        self.session=session

    def add(self,orderline):
        self.session.add(orderline)
    def get(self,sku):
        return self.session.query(OrderLine).filter(OrderLine.sku==sku).one()
    
    def list(self):
        return self.session.query(OrderLine).all()
