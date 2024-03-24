import sqlite3

CONN = sqlite3.connect('task.db')
CURSOR = CONN.cursor()
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .task import Task
