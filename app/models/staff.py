from app import db


class Staff(db.Model):
    __tablename__ = "staff"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    staff_id = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    hotel_id = db.Column(
        db.Integer,
        db.ForeignKey("hotels.id"),
        nullable=False
    )

    is_used = db.Column(
        db.Boolean,
        default=False
    )

    hotel = db.relationship(
        "Hotel",
        backref="staff_ids"
    )