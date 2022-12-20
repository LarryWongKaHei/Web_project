from db.run_sql import run_sql
from models.classes import Classes
from datetime import datetime


# Save a class into the classes table
def save(new_class):
    sql = """INSERT INTO classes (name, fee, gender, availability, duration, max_capacity) 
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"""
    values = [new_class.name, new_class.fee, new_class.tutor_gender, new_class.availability, new_class.duration, new_class.max_capacity]
    result = run_sql(sql, values)
    if result:
        new_class.id = result[0]['id']

# To Delete a class from classes table
def delete_by_id(class_id):
    sql = "DELETE FROM classes WHERE id = %s"
    values = [class_id]
    run_sql(sql, values)

# To selete everything from classes table
def select_all():
    classes = []
    sql = "SELECT * FROM classes"
    values = []
    result = run_sql(sql, values)
    for class_info in result:
        new_class = Classes(class_info['name'], class_info['fee'], class_info['gender'], class_info['availability'], class_info['duration'], class_info['max_capacity'], class_info['id'])
        classes.append(new_class)
    return classes

# To find the class by its name
def select_by_name(name):
    sql = "SELECT * FROM classes WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)
    result = result[0]
    the_class = Classes(result['name'], result['fee'], result['gender'], result['availability'], result['duration'], result['max_capacity'])
    return the_class

# To return this current weekday
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

# To check which classes will be today
def check_class_today():
    class_today = []
    all_class = select_all()
    current_weekday = return_current_weekday()
    for item in all_class:
        if current_weekday in item.availability:
            class_today.append(item)
    return class_today

# To return the class name with id input
def select_by_id_return_name(id):
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    result = result[0]
    return result['name']

# To Delete a class from classes table
def delete_by_name(class_name):
    sql = "DELETE FROM classes WHERE name = %s"
    values = [class_name]
    run_sql(sql, values)

# To update a class to the db
def update(name, fee, gender, availability, duration, max_capacity, classname):
    sql = "UPDATE classes SET name = %s, fee = %s, gender = %s, availability = %s, duration = %s, max_capacity = %s WHERE name = %s"
    values = [name, fee, gender, availability, duration, max_capacity, classname]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM classes"
    values = []
    run_sql(sql, values)


