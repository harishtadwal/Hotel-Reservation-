from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Booking, Room

staff = Blueprint("staff", __name__)

@staff.route("/staff/dashboard")
@login_required
def dashboard():
    if current_user.role != "staff":
        return "Unauthorized", 403

    if current_user.hotel_id is None:
        return "Staff member is not assigned to a hotel.", 403


    # bookings = Booking.query.all()
    bookings = Booking.query.join(Room).filter(
    Room.hotel_id == current_user.hotel_id
    ).all()

    return render_template(
        "staff/dashboard.html",
        bookings=bookings
    )

@staff.route("/checkin/<int:booking_id>")
@login_required
def checkin(booking_id):

    if current_user.role != "staff":
        return "Unauthorized", 403

    if current_user.hotel_id is None:
        return "Staff member is not assigned to a hotel.", 403

    booking = Booking.query.join(Room).filter(
        Booking.id == booking_id,
        Room.hotel_id == current_user.hotel_id
    ).first_or_404()

    booking.status = "checked_in"
    booking.room.status = "occupied"

    db.session.commit()

    flash("Guest checked in successfully!")

    return redirect(url_for("staff.dashboard"))


@staff.route("/checkout/<int:booking_id>")
@login_required
def checkout(booking_id):

    if current_user.role != "staff":
        return "Unauthorized", 403

    if current_user.hotel_id is None:
        return "Staff member is not assigned to a hotel.", 403

    booking = Booking.query.join(Room).filter(
        Booking.id == booking_id,
        Room.hotel_id == current_user.hotel_id
    ).first_or_404()

    booking.status = "checked_out"
    booking.room.status = "available"

    db.session.commit()

    flash("Guest checked out successfully!")

    return redirect(url_for("staff.dashboard"))
