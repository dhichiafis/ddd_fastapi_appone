from fastapi import FastAPI,Depends,HTTPException
import uvicorn 
from fastapi.middleware.cors import CORSMiddleware
from db_connection import *
from sqlalchemy.orm import relationship,Session
from pydantic import BaseModel,ConfigDict
from typing import List,Optional
from orm.orm import *
from model import *
from repository.repository import *
from service.batchunitofwork import *
from pydantic import BaseModel,ConfigDict

class BatchBase(BaseModel):
    id:int 
    sku:str 
    reference:str 
    available_qty:int 
    model_config=ConfigDict(from_attributes=True)
app=FastAPI()

@app.get('/')
async def home():
    return {"message":'introduction to abstraction'}


@app.post('/new/batch')
async def create_batch(
    sku:str,ref:str,qty:int,
    batchuow:BatchUnitOfWork=Depends(BatchUnitOfWork)
):
    with batchuow as uow:
        uow.batchrepo.add(Batch(ref=ref,sku=sku,qty=qty))
        uow.commit()
    return {'message':'successfully created a batch'}
     

@app.get("/all/batches",response_model=list[BatchBase])
async def get_all_batches(
    batchuow:BatchUnitOfWork=Depends(BatchUnitOfWork)
):
    #with batchuow as uow:
    batches=batchuow.batchrepo.list()
    #    return [BatchBase.model_validate(b) for b in batches]
    return batches
@app.post('/new/order/line')
async def create_orderline(
    sku:str,qty:int
):
    session=SessionFactory()
    repo=OrderLineRepository(session=session)
    try:
        batch=OrderLine(sku=sku,qty=qty)
        repo.add(batch)
        session.commit()
        return batch 
    finally:
        session.close 

@app.get("/all/order/lines")
async def get_all_lines():
    session=SessionFactory()
    repo=OrderLineRepository(session=session)
    try:
        lines=session.query(OrderLine).all()
        return lines
    finally:
        session.close()


@app.get('/allocations')
async def allocate():
    session=SessionFactory()
    batchrepo=BatchRepository(session=session)
    orderrepo=OrderLineRepository(session=session)
    try:
        pass 
    finally:
        session.close()