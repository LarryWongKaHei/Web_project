from flask import Flask, render_template, Blueprint, request, redirect, url_for, session
from repositries import members_repository
from models.members import Members


# Set a login blueprint to make it easier to debug.
Login_blueprint = Blueprint("Login", __name__)

@Login_blueprint.route("/logout")
def log_out_page():
    session.pop("Login")
    return render_template("members/logout.html")

@Login_blueprint.route("/checkin")
def check_in_page():
    members_repository.check_in(session["Login"])
    return render_template("members/checkin.html")

# Check in page (Future login page)
@Login_blueprint.route("/login")
def login_page():
    return render_template("login/new_login.html")

# Check in page function 
@Login_blueprint.route("/login", methods=["POST"])
def login():
    data = request.form
    name = data["name"]
    username = data["username"].lower()
    password = data["password"].lower()
    if name == "admin" and username == "admin" and password == "admin":
        return redirect("/admin")
    try:
        members_repository.check_in_login(name, username, password)
        session["Login"] = name
        member = members_repository.select_by_name(name)
        member_property_dict = members_repository.save_to_session(["name", "membership_level", "gender", "availability", "salary"], [member.name, member.membership_level, member.gender, member.availability, member.salary])
        session["member"] = member_property_dict
    except:
        raise 
    else:
        return render_template("members/login.html")


# The first signup page
@Login_blueprint.route("/signup")
def signup_page():
    return render_template("login/new_signup.html")

# The first signup page function
@Login_blueprint.route("/signup", methods=["POST"])
def signup():
    data = request.form
    name = data["name"]
    username = data["username"].lower()
    password = data["password"].lower()
    members_repository.sign_up(name, username, password)
    return redirect(url_for("Login.signup_page2", name=name))

# The second signup page
@Login_blueprint.route("/signup/<name>")
def signup_page2(name):
    return render_template("login/signup2.html", name=name)

# The second signup page function
@Login_blueprint.route("/signup/<name>", methods=["POST"])
def signup2(name):
    data = request.form
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    level = ["bronze", "silver", "gold", "platinum", "diamond"]
    gen = ["M", "F"]
    name = request.form["name"]
    for lv in level:
        if lv in data:
            membership_level = lv

    for genders in gen:
        if genders in data:
            gender = genders
    
    availability = []
    for day in days:
        if day in data:
            availability.append(day)
    salary = data["salary"]
    new_member = Members(name, membership_level, gender, availability, salary)
    members_repository.save(new_member)
    
    return redirect("/")
   
