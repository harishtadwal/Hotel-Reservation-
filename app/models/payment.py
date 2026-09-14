from app import db


class Payment(db.Model):

    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    booking_id = db.Column(
        db.Integer,
        db.ForeignKey("bookings.id"),
        unique=True,
        nullable=False
    )

    amount = db.Column(db.Float, nullable=False)

    payment_method = db.Column(db.String(20), nullable=False)

    payment_status = db.Column(db.String(20), default="pending")

