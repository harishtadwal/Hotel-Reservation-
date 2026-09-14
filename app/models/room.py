from app import db

class Room(db.Model):
    __tablename__="rooms"

    id = db.Column(db.Integer, primary_key=True)

    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.id"), nullable=False)

    room_number = db.Column(db.String(10), nullable=False)

    room_type = db.Column(db.String(50), nullable=False)

    price = db.Column(db.Float, nullable=False)

    capacity = db.Column(db.Integer, nullable=False)

    status = db.Column(db.String(20), default="available")

    description = db.Column(db.Text)

    image = db.Column(db.String(255))

    bookings = db.relationship(
        "Booking",
        backref="room",
        lazy=True
    )

    __table_args__ = (
    db.UniqueConstraint(
        "hotel_id",
        "room_number",
        name="unique_room_per_hotel"
    ),
)
    