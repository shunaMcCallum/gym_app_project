from db.run_sql import run_sql
from models.member import Member
from models.workout import Workout
from models.booking import Booking
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository

def save(member):
    
    sql = "INSERT INTO members(first_name, last_name, dob, active) VALUES (?, ?, ?, ?) RETURNING id"
    values = [member.first_name, member.last_name, member.dob, member.active]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


def sort_function(member):
    return member.last_name


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        active = True if row['active'] == 1 else False
        member = Member(row['first_name'], row['last_name'], row['dob'], active, row['id'])
        members.append(member)
    members.sort(key=sort_function)
    return members


def select_all_active():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        active = True if row['active'] == 1 else False
        if active == True:
            member = Member(row['first_name'], row['last_name'], row['dob'], active, row['id'])
            members.append(member)
    members.sort(key=sort_function)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        active = True if result['active'] == 1 else False
        member = Member(result['first_name'], result['last_name'], result['dob'], active, result['id'])
    return member


def delete_all():
    sql = "DELETE from members"
    run_sql(sql)


def delete(id):
    bookings = get_bookings_member(id)
    for booking in bookings:
        booking_repository.delete(booking.id)
        
    sql = "DELETE FROM members WHERE id = ?"
    values = [id]
    run_sql(sql, values)



def update(member):
    sql = "UPDATE members SET (first_name, last_name, dob, active) = (?, ?, ?, ?) WHERE id = ?"
    values = [member.first_name, member.last_name, member.dob, member.active, member.id]
    run_sql(sql, values)


def get_workouts(member):
    workouts = []
    
    sql = "SELECT workouts.* FROM workouts INNER JOIN bookings ON workouts.id = workout_id WHERE member_id = ?"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        active = True if row['active'] == 1 else False
        workout = Workout(row['name'], row['date'], row['description'], row['duration'], row['capacity'], active, row['id'])
        workouts.append(workout)
    return workouts

def get_bookings_member(id):
    bookings = []
    
    sql = "SELECT * from bookings WHERE member_id = ?"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        member = select(row['member_id'])
        workout = workout_repository.select(row['workout_id'])
        booking = Booking(member, workout, row['id'])
        bookings.append(booking)
    return bookings