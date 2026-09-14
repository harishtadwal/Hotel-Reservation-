from app import db

class Booking(db.Model):
    __tablename__="bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id"),
        nullable=False
    )

    check_in_time = db.Column(db.Date, nullable=False)

    check_out_time = db.Column(db.Date, nullable=False)

    guests = db.Column(db.Integer, nullable=False)

    total_amount = db.Column(db.Float, nullable=False)

    status = db.Column(db.String(20), default="confirmed")

    payment = db.relationship(
        "Payment",
        backref="booking",
        uselist=False
    )