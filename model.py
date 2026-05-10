from dataclasses import dataclass
from datetime import datetime 

@dataclass
class OrderLine:
   # order_id:str 
    sku:str 
    qty:int 

class Batch:
    def __init__(self,ref:str,sku:str,qty:int,):
        self.sku=sku 
        self.reference=ref
        self.available_qty=qty
        self.allocations=set()

    def allocate(self,order):
        if self.can_allocate(order):
            self.allocations.add(order)

    def deallocate(self,orderline:OrderLine):
        if orderline.sku in self.allocations:
            self.allocations.remove(orderline)

        
    def can_allocate(self,line:OrderLine):
        return self.available_qty>line.qty and self.sku==line.sku