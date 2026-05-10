from orm.orm import *
from repository.repository import *
#the unitofwork is to remove the coupling from the endpoints and make our endpoints lighter
class BatchUnitOfWork:
    def __init__(self,):
        self.session=None

    def __enter__(self):
        self.session=SessionFactory()
        self.batchrepo=BatchRepository(session=self.session)
        return self#we have to return this otherwise we reun into an error
    
    def __exit__(self,exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()