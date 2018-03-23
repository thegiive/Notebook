from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('postgresql://user:password@localhost:5432/postgres'.format(**locals()))

class Deliver(Base):
    __tablename__='deliver'
    #column fields
    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    mode = Column(Integer)
    quantity = Column(Integer)
    number = Column(Float)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    deliver_locations = relationship('location')
    def __unicode__(self):
        return "[%s(%s)]" % (self.__class__.__name__, ', '.join('%s=%s' % (k, self.__dict__[k]) for k in sorted(self.__dict__) if '_sa_' != k[:4]))


class Location(Base):
    __tablename__='location'
    #column fields
    id = Column(Integer , primary_key=True)
    lat = Column(Float)
    lng = Column(Float)
    located_at = Column(DateTime)
    deliver_id = Column(Integer , ForeignKey('deliver.id'))
    def __unicode__(self):
        return "[%s(%s)]" % (self.__class__.__name__, ', '.join('%s=%s' % (k, self.__dict__[k]) for k in sorted(self.__dict__) if '_sa_' != k[:4]))

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()

for deliver in s.query(Deliver).all():
    print(ship.__unicode__())

deliver=Deliver(id=id,\
                status=randint(1,4) , mode =randint(1,4), quantity =randint(1,1000),\
                number=1.3,\
                start_time=target_time, end_time =end_time, asn_number ="asn"+str(randint(1,10000)) 
            )
s.add(deliver)
s.commit()

s.rollback()


