from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    
    rooms = relationship("Room", back_populates="hotel")

    @property
    def total_rooms(self):
        return len(self.rooms)

    @classmethod
    def create(cls, session, name, location):
        if not name or not location:
            raise ValueError("Name and location are required")
        hotel = cls(name=name, location=location)
        session.add(hotel)
        session.commit()
        return hotel

    @classmethod
    def delete(cls, session, hotel_id):
        hotel = session.query(cls).filter_by(id=hotel_id).first()
        if hotel:
            session.delete(hotel)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, hotel_id):
        return session.query(cls).filter_by(id=hotel_id).first()

    def __repr__(self):
        return f"Hotel(id={self.id}, name={self.name}, location={self.location})"

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    room_number = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    is_available = Column(Integer, default=1)  # 1 for available, 0 for booked
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    
    hotel = relationship("Hotel", back_populates="rooms")
    user = relationship("User", back_populates="rooms", uselist=False)

    @property
    def status(self):
        return "Available" if self.is_available == 1 else "Booked"

    @classmethod
    def create(cls, session, hotel_id, room_number, price_per_night):
        hotel = session.query(Hotel).filter_by(id=hotel_id).first()
        if not hotel:
            raise ValueError("Hotel not found")
        if session.query(cls).filter_by(hotel_id=hotel_id, room_number=room_number).first():
            raise ValueError(f"Room {room_number} already exists in Hotel {hotel_id}")
        if price_per_night <= 0:
            raise ValueError("Price per night must be greater than 0")
        room = cls(hotel_id=hotel_id, room_number=room_number, price_per_night=price_per_night)
        session.add(room)
        session.commit()
        return room

    @classmethod
    def delete(cls, session, room_id):
        room = session.query(cls).filter_by(id=room_id).first()
        if room:
            session.delete(room)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, room_id):
        return session.query(cls).filter_by(id=room_id).first()

    def __repr__(self):
        return f"Room(id={self.id}, room_number={self.room_number}, hotel_id={self.hotel_id}, available={self.is_available})"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    rooms = relationship("Room", back_populates="user")

    @property
    def booked_rooms_count(self):
        return len(self.rooms)

    @classmethod
    def create(cls, session, name, email):
        if not name or not email:
            raise ValueError("Name and email are required")
        user = cls(name=name, email=email)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def delete(cls, session, user_id):
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, user_id):
        return session.query(cls).filter_by(id=user_id).first()

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"