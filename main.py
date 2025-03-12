from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import click
from models import Hotel, Room, User, Base

# Database setup
engine = create_engine("sqlite:///hotel_reservation.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Pre-populate a default hotel
def initialize_default_hotel():
    session = Session()
    if not Hotel.find_by_id(session, 1):
        Hotel.create(session, "Default Hotel", "City Center")
    session.close()

initialize_default_hotel()

def print_menu():
    click.echo("\nHotel Reservation CLI System")
    click.echo("1. Add Room")
    click.echo("2. Add User")
    click.echo("3. Book Room")
    click.echo("4. Cancel Booking")
    click.echo("5. List Available Rooms")
    click.echo("6. Delete Room (Admin)")
    click.echo("7. Delete User (Admin)")
    click.echo("8. Add Hotel")
    click.echo("9. Exit")

def add_room():
    hotel_id = click.prompt("Hotel ID", type=int)
    room_number = click.prompt("Room Number")
    price = click.prompt("Price per Night", type=float)
    session = Session()
    try:
        room = Room.create(session, hotel_id, room_number, price)
        click.echo(f"Added room: {room.room_number} to Hotel ID {hotel_id}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def add_user():
    name = click.prompt("User Name")
    email = click.prompt("User Email")
    session = Session()
    try:
        user = User.create(session, name, email)
        click.echo(f"Added user: {user.name}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def book_room():
    user_id = click.prompt("User ID", type=int)
    room_id = click.prompt("Room ID", type=int)
    session = Session()
    try:
        user = User.find_by_id(session, user_id)
        room = Room.find_by_id(session, room_id)
        if not user:
            click.echo("User Not Found")
            return
        if not room:
            click.echo("Room Not Found")
            return
        if room.is_available == 0:
            click.echo("Room is already booked")
            return
        room.is_available = 0
        room.user_id = user_id
        session.commit()
        click.echo(f"Room {room.room_number} booked for {user.name}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def cancel_booking():
    room_id = click.prompt("Room ID", type=int)
    session = Session()
    try:
        room = Room.find_by_id(session, room_id)
        if not room:
            click.echo("Room Not Found")
            return
        if room.is_available == 1:
            click.echo("Room is not booked")
            return
        room.is_available = 1
        room.user_id = None
        session.commit()
        click.echo(f"Booking canceled for Room {room.room_number}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def list_available_rooms():
    session = Session()
    try:
        rooms = session.query(Room).filter_by(is_available=1).all()
        for room in rooms:
            hotel = Hotel.find_by_id(session, room.hotel_id)
            click.echo(f"ID: {room.id}, Room: {room.room_number}, Hotel: {hotel.name}, Price: ${room.price_per_night}, Status: {room.status}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def delete_room():
    room_id = click.prompt("Room ID", type=int)
    session = Session()
    try:
        if Room.delete(session, room_id):
            click.echo(f"Deleted room with ID: {room_id}")
        else:
            click.echo(f"Room with ID {room_id} not found")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def delete_user():
    user_id = click.prompt("User ID", type=int)
    session = Session()
    try:
        if User.delete(session, user_id):
            click.echo(f"Deleted user with ID: {user_id}")
        else:
            click.echo(f"User with ID {user_id} not found")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def add_hotel():
    name = click.prompt("Hotel Name")
    location = click.prompt("Hotel Location")
    session = Session()
    try:
        hotel = Hotel.create(session, name, location)
        click.echo(f"Added hotel: {hotel.name} in {hotel.location}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

def main():
    while True:
        print_menu()
        choice = click.prompt("Choose an option (1-9)", type=int)
        if choice == 1:
            add_room()
        elif choice == 2:
            add_user()
        elif choice == 3:
            book_room()
        elif choice == 4:
            cancel_booking()
        elif choice == 5:
            list_available_rooms()
        elif choice == 6:
            delete_room()
        elif choice == 7:
            delete_user()
        elif choice == 8:
            add_hotel()  # Now correctly calls add_hotel instead of exiting
        elif choice == 9:
            click.echo("Exiting...")
            break
            
        else:
            click.echo("Invalid option. Please choose between 1 and 9.")

if __name__ == '__main__':
    main()