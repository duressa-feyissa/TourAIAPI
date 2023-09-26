from sqlalchemy import Column, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    firstname = Column(String(255))
    lastname = Column(String(255))
    email = Column(String(255))
    role = Column(String(100))
    password = Column(String(255))
    accommodations = relationship('Accommodation', back_populates='user')
    events = relationship('Event', back_populates='user')
    
    def toJson(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'role': self.role,
            'email': self.email
        }

class Accommodation(Base):
    __tablename__ = 'accommodations'

    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey('users.id'))
    tour_place_id = Column(String(36), ForeignKey('tour_places.id'))
    name = Column(String(255))
    type = Column(JSON)
    description = Column(Text)
    location = Column(JSON) 
    contact = Column(String(255))
    website = Column(String(255))
    images = Column(JSON)  
    service = Column(JSON)
    user = relationship('User', back_populates='accommodations')
    tour_place = relationship('TourPlace', back_populates='accommodations')
    
    def toJson(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tour_place_id': self.tour_place_id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'location': self.location,
            'contact': self.contact,
            'website': self.website,
            'images': self.images,
            'service': self.service
        }

class TourPlace(Base):
    __tablename__ = 'tour_places'

    id = Column(String(36), primary_key=True)
    name = Column(String(255))
    description = Column(JSON)  
    location = Column(JSON) 
    category = Column(JSON)  
    highlights = Column(JSON)  
    images = Column(JSON) 
    activities = Column(JSON)  
    weather = Column(JSON)  
    accommodations = relationship('Accommodation', back_populates='tour_place')
    
    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'category': self.category,
            'highlights': self.highlights,
            'images': self.images,
            'activities': self.activities,
            'Weather': self.weather
        }
    

class Event(Base):
    __tablename__ = 'events'

    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey('users.id'))
    title = Column(String(255))
    description = Column(Text)
    location = Column(String(255))
    date = Column(String(20)) 
    category = Column(JSON)  
    organizer = Column(String(255))
    contact = Column(String(255))
    website = Column(String(255))
    highlights = Column(JSON)
    images = Column(JSON)
    tickets = Column(JSON)
    user = relationship('User', back_populates='events')


    def toJson(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'date': self.date,
            'category': self.category,
            'organizer': self.organizer,
            'contact': self.contact,
            'website': self.website,
            'highlights': self.highlights,
            'images': self.images,
            'tickets': self.tickets
        }