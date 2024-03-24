from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.task import Task

# Create an engine to connect to the database
engine = create_engine('sqlite:///task.db')

# Define a session
Session = sessionmaker(bind=engine)
session = Session()

# Use the `columns` attribute of the `Task` class to inspect the schema
print("Task Table Schema:")
for column in Task.__table__.columns:
    print(f"{column.name}: {column.type}")

# Close the session
session.close()
