### Hotel Reservation CLI System 🏨

A command-line interface (CLI) application built in Python for managing hotel reservations. Users interact via a menu to add hotels, rooms, and users, book and cancel rooms, list available rooms, and perform admin tasks, with data stored in an SQLite database.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
     git@github.com:MaryMachuma/hotel_reservation.git
   ```
  ```bash
     cd hotel-system
  ```
Initialize a local Git repository:
```⁠bash
   git init
```
⁠  2.Navigate to the Project Directory:
``` ⁠bash
   cd hotel_system
```

⁠ 3.Create and Activate a Virtual Environment:
Create the virtual environment:
 
 ``` ⁠bash
    python -m venv env
 ```

⁠ Activate the virtual environment:
``` ⁠bash
    source env/bin/activate
 ```


⁠ 4.Install Dependencies:
Install the required libraries:
``` ⁠bash
   pip install sqlalchemy alembic click
```

⁠ 5.Apply Database Migrations:
Initialize the database with Alembic:
 
 ``` bash
     alembic upgrade head
  ```

⁠ 6.Run the CLI Application:
Start the application:
``` ⁠bash
   python main.py 
```

### CLI Usage 🖥️
The CLI provides the following  to manage the application. 

Guest IDs and Room IDs are sequential (i.e., the first guest has ID 1, the second guest has ID 2, etc.).
Hotel IDs are displayed under the Rooms section to help users reference them when making bookings.

Main Menu
Hotel Reservation CLI System  
1. Add Room  
2. Add User  
3. Book Room  
4. Cancel Booking  
5. List Available Rooms  
6. Delete Room (Admin)  
7. Delete User (Admin)  
8. Add Hotel  
9. Exit  
Choose an option (1-9):  

## Add User
- **Command** Add a new user.
- **Steps**:
1. Choose an option (1-9): 2
2. User Name: Jane Smith
3. User Email: jane.smith@example.com

- **Output**:
Added user: Jane Smith

## Add Hotel
- **Command** Add a new hotel.
- **Steps**:
1. Choose an option (1-9): 8
2. Hotel Name: Nairobi Serena Hotel
3. Hotel Location: Nairobi, Kenya

 - **Output**:
  Added hotel: Nairobi Serena Hotel in Nairobi, Kenya
 
## Add Room
-**Command**: Add a room to a hotel (e.g., Hotel ID 2 is Ocean Breeze Hotel).
- **Steps**:
1. Choose an option (1-9): 1
2. Hotel ID: 2
3. Room Number: 204
4. Price per Night: 250

-**Output**:
Added room: 204 to Hotel ID 2

## Book Room
- **Command**: Book a room for a user (e.g., User ID 2 is Allan Wex, Room ID 2 is Room 101 in Ocean Breeze Hotel).
- **Steps**:
1. Choose an option (1-9): 3
2. User ID: 2
3. Room ID: 2

- **Output**:
Room 101 booked for Allan Wex

## Cancel Booking
- **Command**: Cancel a booking (e.g., Room ID 2).
- **Steps**:
1. Choose an option (1-9): 4
2. Room ID: 2
- **Output**:
Booking canceled for Room 101

## List Available Rooms
- **Commandnd**: Show all available rooms.
- **Steps**:
1. Choose an option (1-9): 5
- **Output**:

ID: 1, Room: 101, Hotel: Default Hotel, Price: $100.0, Status: Available
ID: 4, Room: 262, Hotel: Ocean Breeze Hotel, Price: $150.0, Status: Available


### Database Access 
Data is stored in hotel_reservation.db. To verify or modify it:
Access SQLite:
bash


### Step 1: Run SQL Queries to Confirm Data
You’ve already opened the database with:

1. sqlite3 hotel_reservation.db

2. List Tables:
   .tables

**Output**: 
 alembic_version  hotels  rooms  users

### Check Data:
3. List Hotels:

- SELECT * FROM hotels;
-**Output**:
1|Default Hotel|City Center
2|Ocean Breeze Hotel|Mombasa
3|Belmond Hotel Caruso|Ravello, Italy
4|Sunset Retreat|Bali

5. List Users:

- SELECT * FROM users;

-**Output**:

1|Amanda Ongeti|amandao@gmail.com
2|Allan Wex|allanwex@gmail.com
3|Mary Machuma|machmary173@gmail.com

- SELECT * FROM rooms;
1|1|101|100.0|0|1
4|2|262|150.0|1|
5|2|203|200.0|1|

### License
- This project is open-source and available under the MIT License.
