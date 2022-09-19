import sqlalchemy
from .base import metadata
from datetime import datetime


contacts = sqlalchemy.Table(
    'contacts', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('first_name', sqlalchemy.String),
    sqlalchemy.Column('last_name', sqlalchemy.String),
    sqlalchemy.Column('patronymic', sqlalchemy.String),
    sqlalchemy.Column('phone', sqlalchemy.String),
    sqlalchemy.Column('email', sqlalchemy.String),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.utcnow),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.utcnow)
)
