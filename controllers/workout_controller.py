from flask import Flask, render_template, request, redirect, Blueprint
from models.workout import Workout
import repositories.workout_repository as workout_repository

workouts_blueprint = Blueprint("workouts", __name__)

# INDEX - SHOW ALL WORKOUTS
@workouts_blueprint.route("/workouts")
def workouts():
    route_name = "workouts"
    workouts = workout_repository.select_all()
    return render_template("workouts/index.html", route_name=route_name, workouts=workouts)

# SHOW ONE WORKOUT
@workouts_blueprint.route("/workouts/<id>")
def workout_show(id):
    route_name = "workouts"
    workout = workout_repository.select(id)
    bookings = workout_repository.get_bookings(workout)
    return render_template("workouts/show.html", route_name=route_name, workout=workout, bookings=bookings)

# ADD NEW WORKOUT
@workouts_blueprint.route("/workouts/create")
def create_workout():
    route_name = "workouts"
    return render_template("workouts/create.html", route_name=route_name)

# CREATE WORKOUT
@workouts_blueprint.route("/workouts", methods=['POST'])
def add_workout():
    name = request.form['name']
    date = request.form['date']
    description = request.form['description']
    duration = request.form['duration']
    capacity = request.form['capacity']

    workout = Workout(name, date, description, duration, capacity)
    workout_repository.save(workout)
    return redirect("/workouts")

# EDIT WORKOUT
@workouts_blueprint.route("/workouts/<id>/update")
def edit_workout(id):
    route_name = "workouts"
    workout = workout_repository.select(id)
    return render_template("workouts/edit.html", route_name=route_name, workout=workout)

# UPDATE WORKOUT
@workouts_blueprint.route("/workouts/<id>", methods=['POST'])
def update_workout(id):
    name = request.form['name']
    date = request.form['date']
    description = request.form['description']
    duration = request.form['duration']
    capacity = request.form['capacity']
    capacity_filled = request.form['capacity_filled']
    active = request.form['active']

    if active == "True":
        active = 1
    else:
        active = 0

    workout = Workout(name, date, description, duration, capacity, capacity_filled, active, id)
    workout_repository.update(workout)

    return redirect(f"/workouts/{workout.id}")

# DELETE WORKOUT
@workouts_blueprint.route("/workouts/<id>/delete", methods=['POST'])
def delete_workout(id):
    workout_repository.delete(id)
    return redirect("/workouts")
