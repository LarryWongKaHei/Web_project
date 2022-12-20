from flask import render_template, Blueprint, request, redirect

from repositries import classes_repository
from models.classes import Classes

from repositries import members_repository
from repositries import class_attend_repositry
from repositries import admin_repository

admin_blueprint = Blueprint("admin", __name__)

# To set a admin homepage
@admin_blueprint.route("/admin")
def admin_homepage():
    classes = classes_repository.check_class_today()
    members = members_repository.select_all()
    members_classes = admin_repository.print_all_class_member_today(classes)


    return render_template("admin/index.html", classes=classes, members=members, dict_list=members_classes)

# Admin show all classes page
@admin_blueprint.route("/admin/show_classes")
def show_all_classes():
    classes = classes_repository.select_all()
    return render_template("admin/show_all_classes.html", classes=classes)

# Admin show class detail page
@admin_blueprint.route("/admin/show_classes/<class_name>")
def show_class(class_name):
    the_class = classes_repository.select_by_name(class_name)
    return render_template("admin/show_class_detail.html", classes=the_class)

# Function to have two function within one page*****
@admin_blueprint.route("/admin/show_classes/<class_name>", methods=['POST'])
def functions(class_name):
    if request.form['button'] == "Delete":
        classes_repository.delete_by_name(class_name)
        return redirect("/admin/show_classes")
    elif request.form['button'] == "Edit":
        classes = classes_repository.select_by_name(class_name)
        return render_template("admin/edit_class.html", classes=classes)

# Edit class function
@admin_blueprint.route("/admin/show_classes/edit/<class_name>", methods=['POST'])
def edit(class_name):
    data = request.form
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    the_class = classes_repository.select_by_name(class_name)
    new_day = []
    for day in days:
        if day in data:
            new_day.append(day)
    if not new_day:
        new_day = the_class.availability
        
    classes_repository.update(data['name'], data['fee'], data['gender'], new_day, data['duration'], data['capacity'], class_name)
    return redirect("/admin/show_classes")

# Add class page
@admin_blueprint.route("/admin/add_class")
def add_class_page():
    return render_template("/admin/add_class.html")

# Add class function
@admin_blueprint.route("/admin/add_class", methods=['POST'])
def add_class():
    data = request.form
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    new_day = []
    for day in days:
        if day in data:
            new_day.append(day)
    new_class = Classes(data['name'], data['fee'], data['gender'], new_day, data['duration'], data['capacity'])
    classes_repository.save(new_class)
    return redirect("/admin/show_classes")

# Show all members that signed up page
@admin_blueprint.route("/admin/show_members")
def show_all_members():
    members = members_repository.select_all()
    return render_template("admin/show_members.html", members=members)

# Show member's detail page
@admin_blueprint.route("/admin/show_member/<member_name>")
def show_member(member_name):
    member = members_repository.select_by_name(member_name)
    return render_template("admin/show_member.html", member=member)
