from db.run_sql import run_sql
from models.workout import Workout
from models.member import Member
from models.booking import Booking
import repositories.member_repository as member_repository

def save(workout):
    sql = "INSERT INTO workouts (name, date, description, duration, capacity, capacity_filled, active) VALUES (?, ?, ?, ?, ?, ?, ?) RETURNING id"
    values = [workout.name, workout.date, workout.description, workout.duration, workout.capacity, workout.capacity_filled, workout.active]
    results = run_sql(sql, values)
    workout.id = results[0]['id']
    return workout


def sort_fuction(workout):
    return workout.date


def select_all():
    workouts = []
    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    for row in results:
        active = True if row['active'] == 1 else False
        workout = Workout(row['name'], row['date'], row['description'], row['duration'], row['capacity'], row['capacity_filled'], active, row['id'])
        workouts.append(workout)
    workouts.sort(key=sort_fuction)
    return workouts


def select_all_active():
    workouts = []
    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    for row in results:
        active = True if row['active'] == 1 else False
        if active == True:
            workout = Workout(row['name'], row['date'], row['description'], row['duration'], row['capacity'], row['capacity_filled'], active, row['id'])
            workouts.append(workout)
    workouts.sort(key=sort_fuction)
    return workouts


def select(id):
    workout = None
    sql = "SELECT * FROM workouts where id = ?"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        active = True if result['active'] == 1 else False
        workout = Workout(result['name'], result['date'], result['description'], result['duration'], result['capacity'], result['capacity_filled'], active, result['id'])
    return workout


def delete_all():
    sql = "DELETE from workouts"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM workouts where id = ?"
    values = [id]
    run_sql(sql, values)


def update(workout):
    sql = "UPDATE workouts SET (name, date, description, duration, capacity, capacity_filled, active) = (?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [workout.name, workout.date, workout.description, workout.duration, workout.capacity, workout.capacity_filled, workout.active, workout.id]
    run_sql(sql, values)


def get_members(workout):
    members = []

    sql = "SELECT members.* from members INNER JOIN bookings ON members.id = bookings.member_id WHERE workout_id = ?"
    values = [workout.id]
    results = run_sql(sql, values)

    for row in results:
        active = True if row['active'] == 1 else False
        member = Member(row['first_name'], row['last_name'], row['dob'], active, row['id'])
        members.append(member)
    return members


def get_bookings(workout):
    bookings = []

    sql = "SELECT * from bookings WHERE workout_id = ?"
    values = [workout.id]
    results = run_sql(sql, values)

    for row in results:
        member = member_repository.select(row['member_id'])
        workout1 = select(row['workout_id'])
        booking = Booking(member, workout1, row['id'])
        bookings.append(booking)
    return bookings


def update_capacity_filled(workout):
    workout.capacity_filled += 1

    sql = "UPDATE workouts SET (capacity_filled) = (?) WHERE id = ?"
    values = [workout.capacity_filled, workout.id]
    run_sql(sql, values)


def reduce_capacity_filled(workout):
    workout.capacity_filled -= 1

    sql = "UPDATE workouts SET (capacity_filled) = (?) WHERE id = ?"
    values = [workout.capacity_filled, workout.id]
    run_sql(sql, values)
