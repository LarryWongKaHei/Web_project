from flask import Flask, render_template, Blueprint, session
from repositries import members_repository

# Set a members blueprint to make it easier to debug.
members_blueprint = Blueprint("members", __name__)

# Show all the advantage to be a members
# @members_blueprint.route("/members_privilege")
# def show_members_privilege():
#     return render_template

# To show check in successfully and redirect page
@members_blueprint.route("/checkin/<member_name>")
def checkin(member_name):
    members_repository.check_in(member_name)
    return render_template("members/checkin.html", checkin=True)

@members_blueprint.route("/profile")
def profile_page():
    return render_template("members/profile.html", member=session['member'])

