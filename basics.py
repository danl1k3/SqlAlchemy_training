from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, func

meta = MetaData()

# --- Tables Definition ---

people = Table(
        "people",
        meta, 
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('age', Integer)
)
things = Table(
        "things",
        meta,
        Column('id', Integer, primary_key=True),
        Column('description', String, nullable=False),
        Column('value', Float),
        Column('owner', Integer, ForeignKey('people.id'))
)

# --- Tables END ---

conn_string = 'sqlite:///mydatabase.db'
engine = create_engine(conn_string, echo=True)
conn = engine.connect()
meta.create_all(engine)

def print_selection(select_statement: str) -> None:
    result = conn.execute(select_statement)
    for row in result.fetchall():
        print(row)

'''
# inserting 1 | needed import insert
insert_statement = insert(people).values(name='Jane', age=40)

# insert 2 
insert_state = people.insert().values(name='Mike', age=30)

result = conn.execute(insert_statement)


SELECTIONS
select_statement = people.select().where(people.c.age > 20)
result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)


UPDATE
update_statement = people.update().where(people.c.name == 'Jane', people.c.id == 2).values(age=50)
result = conn.execute(update_statement)

# DELETING
delete_statement = people.delete().where(people.c.id > 9)
result = conn.execute(delete_statement)
conn.commit()

# Adding data
insert_people = people.insert().values([
    {'name': 'Mike', 'age': 30},
    {'name': 'Katya', 'age': 20},
    {'name': 'Nina', 'age': 40},
    {'name': 'Denis', 'age': 42},
    {'name': 'John', 'age': 33}
])

insert_things = things.insert().values([
    {'owner': 2, 'description': 'Laptop', 'value': 800.50},
    {'owner': 2, 'description': 'Mouse', 'value': 50.50},
    {'owner': 2, 'description': 'KeyBoard', 'value': 100.50},
    {'owner': 3, 'description': 'Book', 'value': 30},
    {'owner': 4, 'description': 'Bottle', 'value': 10.50},
    {'owner': 5, 'description': 'Speakers', 'value': 80.50},
])

conn.execute(insert_people)

conn.commit()

conn.execute(insert_things)

conn.commit()

# JOINS
join_statement = people.join(things, people.c.id == things.c.owner)
select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)
conn.execute(select_statement)
conn.commit()

print_selection(select_statement)
'''

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner).having(func.sum(things.c.value) > 50)
result = conn.execute(group_by_statement)

print_selection(group_by_statement)
