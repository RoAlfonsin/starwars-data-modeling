import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    password = Column(String(30), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    birth_year = Column(Integer)
    gender = Column(String(32))
    height = Column(Float)
    skin_color = Column(String(64))
    eye_color = Column(String(64))
    imageUrl = Column(String(256))


class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    climate = Column(String(32))
    terrain = Column(String(128))
    gravity = Column(String(64))
    imageUrl = Column(String(256))

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    model = Column(String(64))
    crew = Column(Integer)
    passengers = Column(Integer)
    vehicle_class = Column(String(128))
    cargo_capacity = Column(Integer)
    imageUrl = Column(String(256))

class Favorites_Names(Base):
    __tablename__ = 'favorites_ids'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), default=-1)
    character_id = Column(Integer, ForeignKey('characters.id'), default=-1)
    planet_id = Column(Integer, ForeignKey('planets.id'), default=-1)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    favorites_id = Column(Integer, ForeignKey('favorites_ids.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
