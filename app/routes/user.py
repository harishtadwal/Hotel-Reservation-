from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime

from app import db
from app.models import Room, Booking, Payment, Hotel

user = Blueprint("user", __name__)

@user.route("/")
def home():

    hotels = Hotel.query.limit(6).all()

    return render_template(
        "home.html",
        hotels=hotels
    )

@user.route("/dashboard")
@login_required
def dashboard():
    return render_template("user/dashboard.html", user=current_user)

@user.route("/rooms")
@login_required
def rooms():
    rooms = Room.query.all()
    return render_template("user/rooms.html", rooms=rooms)

@user.route("/book/<int:room_id>", methods = ["GET", "POST"])
@login_required
def book_room(room_id):

    room = Room.query.get_or_404(room_id)

    if request.method == "POST":

        check_in = datetime.strptime(
            request.form["check_in"], "%Y-%m-%d"
        ).date()

        check_out = datetime.strptime(
            request.form["check_out"], "%Y-%m-%d"
        ).date()

        guests = int(request.form["guests"])

        #Validate dates 
        if check_out <= check_in:
            flash("Check-out date must be after the check-in date.")
            return redirect(url_for("user.book_room", room_id=room_id))

        #Check overlapping booking
        conflict = Booking.query.filter(
            Booking.room_id == room_id,
            Booking.status != "cancelled",
            Booking.check_in_time < check_out,
            Booking.check_out_time > check_in
        ).first()

        if conflict:
            flash("Room is not available for these dates.")
            return redirect(url_for("user.book_room", room_id=room_id))

        #Calculate nights
        nights = (check_out-check_in).days

        total = nights * room.price

        booking = Booking(
            user_id = current_user.id,
            room_id = room_id,
            check_in_time = check_in,
            check_out_time = check_out,
            guests = guests,
            total_amount = total,
            status = "confirmed"
        )

        db.session.add(booking)
        db.session.commit()

        flash("Room booked successfully!")

        return redirect(url_for("user.my_booking"))

    check_in = request.args.get("check_in")
    check_out = request.args.get("check_out")

    return render_template("user/booking.html", room=room, check_in=check_in,check_out=check_out)

@user.route("/my-bookings")
@login_required
def my_booking():

    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template("user/my_bookings.html", bookings=bookings)

@user.route("/booking/<int:booking_id>")
@login_required
def booking_details(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    if booking.user_id != current_user.id:
        return "Unauthorized", 403

    return render_template(
        "user/booking_details.html",
        booking=booking
    )

@user.route("/bill/<int:booking_id>")
@login_required
def bill(booking_id):
    booking = Booking.query.get_or_404(booking_id)


    if booking.user_id != current_user.id:
        return "Unauthorized", 403

    return render_template(
        "user/bill.html",
        booking=booking
    )

@user.route("/hotels")
def hotels():

    search = request.args.get("search", "")

    if search:
        hotels = Hotel.query.filter(
            Hotel.name.ilike(f"%{search}%") |
            Hotel.location.ilike(f"%{search}    %")
        ).all()
    else:
        hotels =Hotel.query.all()

    return render_template("user/hotels.html", hotels= hotels,search=search)

@user.route("/hotels/<int:hotel_id>")
def hotel_rooms(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)

    check_in = request.args.get("check_in")
    check_out = request.args.get("check_out")

    rooms = Room.query.filter_by(
        hotel_id=hotel_id,
    ).all()

    if check_in and check_out:

        check_in_time = datetime.strptime(
            check_in, "%Y-%m-%d"
        ).date()

        check_out_time = datetime.strptime(
            check_out, "%Y-%m-%d"
        ).date()

        booked_room_ids = db.session.query(
            Booking.room_id
        ).filter(
            Booking.status != "cancelled",
            Booking.check_in_time < check_out_time,
            Booking.check_out_time > check_in_time
        ).subquery()

        rooms = Room.query.filter(
            Room.hotel_id == hotel_id,
            ~Room.id.in_(booked_room_ids)
        ).all()

    return render_template(
        "user/hotel_rooms.html",
        hotel=hotel,
        rooms=rooms,
        check_in=check_in,
        check_out=check_out
    )

