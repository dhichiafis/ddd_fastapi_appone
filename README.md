## Domain driven design
this is a project where we are implementing ddd in the desing of scalable software 
the first thing is to use explicit mapping where we map domain objects to database table 
the thing is highlevel objects should not depend on low level objects 
we have to create an orm file where we do our mapping with the following methd
mapper_registry=registy()
the database table and we then have map our domain to the database table
mapper_registry.map_imperatively(domain,database_table)
next we have to ensure that our tables are created with this line 
mapper_registry.metadata.create_all(engine)
next we define and abstraction to prevent the intreration with the database this will be resposible for handling crud
next we introduce the unit of work to our service layer here our endpoints acts as both the service laye making them thin
notice how we call the unitofwork and its dependency okay 
