from flask import Flask, render_template, request, redirect, Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX - SHOW ALL BOOKINGS
@bookings_blueprint.route("/bookings")
def bookings():
    route_name = "bookings"
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", route_name=route_name, bookings=bookings)

# ADD NEW BOOKING
@bookings_blueprint.route("/bookings/create")
def add_booking():
    route_name = "bookings"
    members = member_repository.select_all_active()
    workouts = workout_repository.select_all_active()
    return render_template("bookings/create.html", route_name=route_name, members=members, workouts=workouts)

# ADD NEW BOOKING FROM MEMBER PAGE
@bookings_blueprint.route("/bookings/create/member/<id>")
def add_booking_for_member(id):
    route_name = "bookings"
    member = member_repository.select(id)
    workouts = workout_repository.select_all_active()
    return render_template("bookings/create_member.html", route_name=route_name, workouts=workouts, member=member)

# ADD NEW BOOKING FROM WORKOUT PAGE
@bookings_blueprint.route("/bookings/create/workout/<id>")
def add_booking_for_workout(id):
    route_name = "bookings"
    members = member_repository.select_all_active()
    workout = workout_repository.select(id)
    return render_template("bookings/create_workout.html", route_name=route_name, workout=workout, members=members)

# CREATE BOOKING
@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    workout_id = request.form['workout_id']

    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)

    booking = Booking(member, workout)
    booking_repository.save_with_check(booking)
    return redirect("/bookings")

# CREATE BOOKING FOR MEMBER RETURN TO MEMBER PAGE
@bookings_blueprint.route("/bookings/member/<id>", methods=['POST'])
def create_booking_for_member(id):
    route_name = "members"

    member_id = request.form['member_id']
    workout_id = request.form['workout_id']
    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)
    booking = Booking(member, workout)
    booking_repository.save_with_check(booking)

    member = member_repository.select(id)
    bookings = member_repository.get_bookings_member(id)

    return render_template("members/show.html", route_name=route_name, bookings=bookings, member=member)


# CREATE BOOKING FOR WORKOUT RETURN TO WORKOUT PAGE
@bookings_blueprint.route("/bookings/workout/<id>", methods=['POST'])
def create_booking_for_workout(id):
    route_name = "workouts"

    member_id = request.form['member_id']
    workout_id = request.form['workout_id']
    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)
    booking = Booking(member, workout)
    booking_repository.save_with_check(booking)

    bookings = workout_repository.get_bookings(workout)
    workout = workout_repository.select(id)

    return render_template("workouts/show.html", route_name=route_name, workout=workout, bookings=bookings)

# DELETE BOOKING
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

# DELETE BOOKING FROM MEMBER PAGE
@bookings_blueprint.route("/bookings/member/<id>/delete", methods=['POST'])
def delete_booking_member_page(id):
    member = booking_repository.get_member(id)
    booking_repository.delete(id)
    
    return redirect(f"/members/{member.id}")

# DELETE BOOKING FROM WORKOUT PAGE
@bookings_blueprint.route("/bookings/workout/<id>/delete", methods=['POST'])
def delete_booking_workout_page(id):
    workout = booking_repository.get_workout(id)
    booking_repository.delete(id)

    return redirect(f"/workouts/{workout.id}")