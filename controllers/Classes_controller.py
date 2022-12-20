from flask import Flask, render_template, Blueprint, redirect, session
from repositries import classes_repository
# Set a classes blueprint to make it easier to debug
classes_blueprint = Blueprint("classes", __name__)

# Create a show_classes route to show all the classes at the Gym
@classes_blueprint.route("/class/show_classes")
def show_all_classes():
    all_classes = classes_repository.select_all()
    return render_template("classes/all_classes.html", classes=all_classes)

# Create a show_class_detail to show a particular class detail
@classes_blueprint.route("/class/<class_name>")
def show_class_detail(class_name):
    the_class = classes_repository.select_by_name(class_name)
    return render_template("classes/the_class.html", the_class=the_class)

# About us page
@classes_blueprint.route("/class/about_us")
def about_us():
    return render_template("classes/about_us.html")

# Timetable page
@classes_blueprint.route("/class/aboutclasses/timetable")
def timetable():
    return render_template("/classes/time_table.html")

# Prices page
@classes_blueprint.route("/class/aboutclasses/prices")
def prices():
    return render_template("/classes/prices.html")

# Tutor_info page
@classes_blueprint.route("/class/aboutclasses/tutor_info")
def tutor_info():
    return render_template("/classes/tutor_info.html")
