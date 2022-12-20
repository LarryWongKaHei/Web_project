from db.run_sql import run_sql
from models.members import Members
from datetime import datetime
import json


# To Save a new member to members table
def save(new_member):
    sql = """INSERT INTO members (name, membership_level, gender, availability, salary, status) 
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"""
    values = [new_member.name, new_member.membership_level, new_member.gender, new_member.availability, new_member.salary, new_member.status]
    result = run_sql(sql, values)
    if result:
        new_member.id = result[0]['id']

# To Delete a member from members table
def delete_by_id(member_id):
    sql = "DELETE FROM members WHERE members.id = %s"
    values = [member_id]
    run_sql(sql, values)

# To search what class the member could join
def search_by_member(member):
    class_can_attend = []
    for date in member.availability:
        sql = "SELECT name FROM classes WHERE availability = %s"
        values = [date]
        result = run_sql(sql, values)
        result = result[0]
        for item in result:
            if item in class_can_attend:
                continue
            else:
                class_can_attend.append(item)
    return class_can_attend

# To return today's weekday
def return_current_weekday():
    # get today's date to get the current weekday
    todays_date = datetime.now()
    today_week_day = todays_date.weekday()

    # create a dictionary to connect the weekday variable to real weekday.
    week_day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    new_dict = {}
    for index, day in enumerate(week_day):
        new_dict[index] = day
    return new_dict[today_week_day]

# Check today's members
def check_today_member(class_today):
    classes_id = []
    for classes in class_today:
        classes_id.append(classes.id)
    classes_id = tuple(classes_id)

    sql = "SELECT * FROM members INNER JOIN class_attend ON members.id = class_attend.member_id WHERE class_attend.classes_id IN %s"
    values = [classes_id]
    result = run_sql(sql, values)
    members = []
    for member in result:
        the_member = Members(member['name'], member['membership_level'], member['gender'], member['availability'], member['salary'])
        members.append(the_member)
    return members

# Return the name of the member with id input
def select_by_id_return_name(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    result = result[0]
    return result['name']

# To return all members in a list from the members db
def select_all():
    sql = "SELECT * FROM members"
    values = []
    result = run_sql(sql, values)
    members = []
    for member in result:
        new_member = Members(member['name'], member['membership_level'], member['gender'], member['availability'], member['salary'], member['status'])
        members.append(new_member)
    return members

# To check in (Will show on the admin home page if checked in)
def check_in(member):
    sql = "UPDATE members SET status = %s WHERE name = %s"
    values = [True, member]
    run_sql(sql, values)

# To check the Log in details inserted
def check_in_login(name, username, password):
    with open('data.json', 'r') as f:
        data = json.load(f)
        if name in data:
            if username in data[name]:
                if password == data[name][username]:
                    return True
                else:
                    raise Exception("Wrong Password")
            else: 
                raise Exception("Wrong username or not exist")
        else:
            raise Exception("Name not registered")

                    

# To sign up a account
def sign_up(name, username, password):
    if not name or not username or not password:
        raise Exception("info can't be None")
    
    try:
        with open('data.json', "r") as f:
            data = json.load(f)
            for item, value in data.items():
                if username in value:
                    raise
    except:
        raise Exception("This username is used")

    new_data = {name : {username:password}}
    data.update(new_data)
    try:
        with open('data.json', 'w') as f:
            json.dump(data, f)
    except:
        raise Exception("Sign up failed")
    else:
        return True

# To return the member with name input
def select_by_name(name):
    sql = "SELECT * FROM members WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)
    result = result[0]
    the_member = Members(result['name'], result['membership_level'], result['gender'], result['availability'], result['salary'])
    return the_member

def save_to_session(property_list, value_list):
    session_dict = {}
    for property, value in zip(property_list, value_list):
        session_dict[property] = value
    return session_dict

def delete_all():
    sql = "DELETE FROM members"
    values = []
    run_sql(sql, values)



    

