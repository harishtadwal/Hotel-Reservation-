from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user


from app import db
from app.models import User, Staff

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered!")
            return redirect(url_for("auth.register"))

        # Hash Password
        hashed_password = generate_password_hash(password)

        user = User(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful!")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            next_page = request.args.get("next")

            if next_page:
                return redirect(next_page)

            if user.role == "staff":
                return redirect(url_for("staff.dashboard"))

            return redirect(url_for("user.dashboard"))


        flash("Invalid email or password!")

    return render_template("auth/login.html")

@auth.route("/logout")
def logout():

    logout_user()

    flash("You have been logged out.")

    return redirect(url_for("auth.login"))

@auth.route("/staff/register", methods=["GET", "POST"])
def staff_register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        staff_id = request.form["staff_id"].strip().upper()

        # Check if email already exists
        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            flash("Email already registered!")
            return redirect(
                url_for("auth.staff_register")
            )

        # Verify Staff ID
        staff = Staff.query.filter_by(
            staff_id=staff_id
        ).first()

        if not staff:
            flash("Invalid Staff ID!")
            return redirect(
                url_for("auth.staff_register")
            )

        # Check whether Staff ID is already used
        if staff.is_used:
            flash("This Staff ID has already been used.")
            return redirect(
                url_for("auth.staff_register")
            )

        hashed_password = generate_password_hash(password)

        user = User(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password,
            role="staff",
            hotel_id=staff.hotel_id,
            staff_id=staff.staff_id
        )

        db.session.add(user)

        # Mark Staff ID as used
        staff.is_used = True

        db.session.commit()

        flash("Staff registration successful! Please login.")

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/staff_register.html"
    )