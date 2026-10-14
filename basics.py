from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert

# --- Tables Definition ---

people = Table(
        "people",
        meta, 
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('age', Integer)
)


# --- Tables END ---

engine = create_engine(sqlite:///mydatabase.db, echo=True)
meta = MetaData()

meta.create_all(engine)
conn = engine.connect()

def print_db(db_name: str):
    select_statement = db_name.select()
    result = conn.execute(select_statement)
    for row in result.fetchall():
        print(row)
'''
# inserting 1 | needed import insert
insert_statement = insert(people).values(name='Jane', age=40)

# insert 2 
insert_state = people.insert().values(name='Mike', age=30)

result = conn.execute(insert_statement)
'''

'''
SELECTIONS
select_statement = people.select().where(people.c.age > 20)
result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)
'''

'''
UPDATE
update_statement = people.update().where(people.c.name == 'Jane', people.c.id == 2).values(age=50)
result = conn.execute(update_statement)
'''

'''
DELETING
delete_statement = people.delete().where(people.c.name == 'Jane', people.c.id == 2)
result = conn.execute(delete_statement)
'''

conn.commit()



