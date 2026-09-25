from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(15))
    
    role = db.Column(db.String(20), default="user") 

    #Hotel assigned to staff member
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.id"), nullable=True)

    staff_id = db.Column(
        db.String(50),
        unique=True,
        nullable=True
    )

    bookings = db.relationship(
        "Booking",
        backref="user",
        lazy=True
    )

    hotel = db.relationship(
        "Hotel",
        backref="staff_members",
        lazy=True
    )