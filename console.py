import pdb
import datetime
from models.member import Member
from models.workout import Workout
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository

# booking_repository.delete_all()
# member_repository.delete_all()
# workout_repository.delete_all()

# member1 = Member("Frasier", "Crane", datetime.datetime(1960, 10, 10))
# member_repository.save(member1)
# member2 = Member("Niles", "Crane", datetime.datetime(1963, 7, 7))
# member_repository.save(member2)

# workout1 = Workout("Spin Class", datetime.datetime(2022, 6, 6), "Spin class", 60, 10)
# workout_repository.save(workout1)
# workout2 = Workout("Boxing Class", datetime.date(2022, 9, 6), "Boxing class", 45, 2)
# workout_repository.save(workout2)

# booking1 = Booking(member1, workout1)
# booking_repository.save(booking1)
# booking2 = Booking(member2, workout2)
# booking_repository.save(booking2)
# booking3 = Booking (member1, workout2)
# booking_repository.save(booking3)
# booking4 = Booking(member2, workout1)
# booking_repository.save(booking4)

# member1 = Member("Frasier", "Crane", datetime.datetime(1960, 10, 10))
# member_repository.save(member1)
# member2 = Member("Niles", "Crane", datetime.datetime(1963, 7, 7))
# member_repository.save(member2)

# member = member_repository.select(1)
# print(member.__dict__)

# Testing Member select_all function returns all data from Members table:
members = member_repository.select_all()
for member in members:
    print(member.__dict__)

# Testing issue - workout name and description lost when updating
# workouts = workout_repository.select_all()
# for workout in workouts:
#     print(workout.__dict__)

# Testing issue with updating member information
# member1.active = False
# member_repository.update(member1)

# print(member1.__dict__)
# print("  ")

# members1 = member_repository.select_all()
# for x in members1:
#     print(x.__dict__)

# print("  ")

# member1.active = True
# member_repository.update(member1)


# members = member_repository.select_all()
# for x in members:
#     print(x.__dict__)

# Testing selecting only active members
# members = member_repository.select_all_active()
# for member in members:
#     print(member.__dict__)

# Testing saving workouts with capacity check
# workout = booking_repository.check_save_workout(booking2)
# print(workout)

# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# booking5 = Booking (member1, workout2)
# booking_repository.save_with_check(booking5)


# booking5 = Booking (member1, workout2)
# booking_repository.save_with_check(booking5)

# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# Testing members save and select
# members = member_repository.select_all()
# for member in members:
#     print(member.__dict__)

# Testing members delete
# member_repository.delete(10)

# Testing members update
# member1.first_name = "Daphne"
# member_repository.update(member1)

# members = member_repository.select_all()
# for member in members:
#     print(member.__dict__)

#  Testing show one member
# member = member_repository.select(41)
# print(member.__dict__)

# Testing workouts save and select
# workouts = workout_repository.select_all()
# for workout in workouts:
#     print(workout.__dict__)

# Testing workout capacities update and print
# workout = workout_repository.select(1)
# print(workout.__dict__)

# workout2 = workout_repository.select(2)
# print(workout2.__dict__)

# Testing deleting workouts and reducing capacity filled
# booking = booking_repository.select(1)
# print(booking.__dict__)

# workout = workout_repository.select(1)
# booking_repository.save(booking5)
# print(workout.__dict__)

# booking_repository.delete(1)
# print(workout.__dict__)

# workout = booking_repository.get_workout(2)
# print(workout.__dict__)

# Testing workouts delete
# workout_repository.delete(5)

# Testing workouts update
# workout1.name = "HIIT Workout"
# workout_repository.update(workout1)

# workouts = workout_repository.select_all()
# for workout in workouts:
#     print(workout.__dict__)

# Testing bookings save and select
# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# Testing bookings delete
# booking_repository.delete(14)

# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# Testing select one member's workouts
# member_workouts = member_repository.get_workouts(member1)
# for workout in member_workouts:
#     print(workout.__dict__)

# Testing select one workout's members
# workout_members = workout_repository.get_members(workout1)
# for member in workout_members:
#     print(member.__dict__)

# Testing select one workout's bookings
# bookings = workout_repository.get_bookings(workout1)
# for booking in bookings:
#     print(booking.member.first_name)


pdb.set_trace()