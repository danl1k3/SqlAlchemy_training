from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


engine = create_engine('sqlite:///localdb.db', echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    things = relationship('Thing', back_populates='person')

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates='things')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

'''
new_person = Person(name='Charlie', age=70)
session.add(new_person)

session.flush()

new_thing = Thing(description='Camera', value=500, owner=new_person.id)

session.add(new_thing)

session.commit()
'''

# Selecting
# results = session.query(Person.name, Person.age).filter(Person.age > 40).all()

# Deletion
# session.query(Thing).filter(Thing.value < 50).delete()

# Updating
# results = session.query(Person).filter(Person.name == 'Charlie').update({'name': 'Charles'})

# Joining
# results = session.query(Person.name, Thing.description).join(Thing).all()

# Aggregation
# results = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).having(func.sum(Thing.value) > 50).all()


# print(results)

session.close()
