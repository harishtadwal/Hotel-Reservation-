from app import db

class Hotel(db.Model):
    __tablename__ = "hotels"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(120))
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    rating = db.Column(db.Float, default = 0)

    rooms = db.relationship(
        "Room",
        backref="hotel",
        lazy=True
    )