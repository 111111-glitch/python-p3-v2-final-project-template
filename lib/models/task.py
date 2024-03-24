import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

#Define Database Models
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String) 

#Configure Database Connection
engine = create_engine('sqlite:///task.db')

#Create Session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a new task
def add_task(title, description):
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()

# Function to delete a task by ID
def delete_task(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
    else:
        print("Task not found!")

# Function to retrieve all tasks
def get_all_tasks():
    return session.query(Task).all()

# Function to find a task by ID
def find_task_by_id(task_id):
    return session.query(Task).filter_by(id=task_id).first()

# Function to update the status of a task
def update_task_status(task_id, new_status):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.status = new_status
        session.commit()
    else:
        print("Task not found!")
