# StayEase - Hotel Reservation System

StayEase is a hotel reservation web application built using Flask. It allows users to explore hotels, check room availability, book rooms, and manage their bookings.

The project also includes a separate staff panel where staff can manage guest check-ins and check-outs.

## Features

### User Side

* User registration and login
* Browse hotels without login
* Search hotels by name or location
* View available rooms
* Check room availability based on dates
* Book a room
* View my bookings
* View booking details
* Generate and view bills
* Responsive design for different screen sizes

### Staff Side

* Separate staff dashboard
* View all reservations
* Check-in guests
* Check-out guests
* Room status management

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* MySQL
* Flask-Login
* HTML
* CSS
* Jinja2
* Git & GitHub

## Project Structure

hotel_reservation_system/
│
├── app/
│   ├── models/
│   │   ├── user.py
│   │   ├── hotel.py
│   │   ├── room.py
│   │   ├── booking.py
│   │   └── payment.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── user.py
│   │   └── staff.py
│   │
│   ├── templates/
│   │   ├── auth/
│   │   ├── user/
│   │   └── staff/
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── __init__.py
│
├── migrations/
├── tests/
├── config.py
├── requirements.txt
├── run.py
└── .gitignore


## How It Works

### 1. User Registration

A new user can create an account by providing their name, email, phone number and password.

Passwords are stored using password hashing instead of storing them directly.

### 2. Browse Hotels

Users can browse hotels from the home page without logging in.

They can also search for hotels by:

* Hotel name
* Location

### 3. Check Room Availability

After selecting a hotel, users can select their check-in and check-out dates.

StayEase checks existing bookings and shows rooms that are available for the selected dates.

### 4. Book a Room

Login is required before booking a room.

The user selects:

* Check-in date
* Check-out date
* Number of guests

The total amount is calculated according to the room price and number of nights.

### 5. Manage Bookings

After booking, users can view their bookings from the **My Bookings** section.

They can see:

* Booking ID
* Hotel
* Room
* Check-in date
* Check-out date
* Number of guests
* Total amount
* Booking status

### 6. Staff Management

Staff members have access to a separate dashboard.

Staff can:

* View reservations
* Check guests in
* Check guests out
* Update room status

## Database

The project uses MySQL as the database.

Main tables:

users
hotels
rooms
bookings
payments

The main relationships are:

User
  ↓
Bookings
  ↓
Room
  ↓
Hotel


A hotel can have multiple rooms, and a user can have multiple bookings.

## Installation

### 1. Clone the repository

git clone https://github.com/your-username/hotel-reservation-system.git

Go inside the project:

cd hotel_reservation_system


### 2. Create a virtual environment

python -m venv venv


Activate it on Windows:

venv\Scripts\activate

### 3. Install dependencies


pip install -r requirements.txt


### 4. Configure MySQL

Create a MySQL database and update the database configuration in your environment/config file.

Example:

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=hotel_reservation

Do not upload your actual password or .env file to GitHub.

### 5. Run database migrations


flask --app run.py db upgrade


### 6. Run the application

python run.py


Open the application in your browser:


http://127.0.0.1:5000


## Room Availability

StayEase uses the booking dates to check whether a room is already reserved.

The application checks for overlapping bookings before creating a new reservation.

This prevents the same room from being booked by two users for overlapping dates.

## Screenshots

Screenshots can be added here later.

Example:

Home Page
Hotels Page
Room Availability
Booking Page
My Bookings
Staff Dashboard


## Future Improvements

Some features I plan to add in the future:

* Online payment integration
* Staff registration with Staff ID verification
* Hotel admin panel
* Email booking confirmation
* PDF bill generation
* Booking cancellation
* Better room filtering
* Hotel reviews and ratings
* More advanced availability management

## What I Learned

While building this project, I worked with:

* Flask application structure
* Flask Blueprints
* Flask-Login authentication
* SQLAlchemy relationships
* MySQL database integration
* Flask-Migrate and Alembic
* CRUD operations
* Jinja templates
* Form handling
* Booking availability logic
* Git and GitHub
* Responsive frontend design

## Author

**Harish Tadwal**

B.Tech CSE Student

GitHub: `harishtadwal`


## Project Status

This project is currently under development. More features and improvements will be added as I continue working on it.
