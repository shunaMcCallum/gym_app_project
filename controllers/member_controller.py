from flask import Flask, render_template, request, redirect, Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

members_blueprint = Blueprint("members", __name__)

#  INDEX - SHOW ALL MEMBERS
@members_blueprint.route("/members")
def members():
    route_name = "members"
    members = member_repository.select_all()
    return render_template("members/index.html", route_name=route_name, members=members)

# SHOW ONE MEMBER
@members_blueprint.route("/members/<id>")
def member_show(id):
    route_name = "members"
    member = member_repository.select(id)
    bookings = member_repository.get_bookings_member(id)
    return render_template("members/show.html", route_name=route_name, member=member, bookings=bookings)

# ADD NEW MEMBER
@members_blueprint.route("/members/create")
def add_member():
    route_name = "members"
    return render_template("members/create.html", route_name=route_name)

# CREATE MEMBER
@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']

    member = Member(first_name, last_name, dob)
    member_repository.save(member)
    return redirect("/members")

# EDIT MEMBER
@members_blueprint.route("/members/<id>/update")
def edit_member(id):
    route_name = "members"
    member = member_repository.select(id)
    return render_template("/members/edit.html", route_name=route_name, member=member)

# UPDATE MEMBER
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    active = request.form['active']

    if active == "True":
        active = 1
    else:
        active = 0

    member = Member(first_name, last_name, dob, active, id)
    member_repository.update(member)

    return redirect(f"/members/{member.id}")

# DELETE MEMBER
@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")
