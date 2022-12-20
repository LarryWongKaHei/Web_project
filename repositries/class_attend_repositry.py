from db.run_sql import run_sql

# To save members id and classes id that joined class
def save(member, classes):
    sql = "INSERT INTO class_attend (member_id, classes_id) VALUES (%s, %s)"
    values = [member.id, classes.id]
    run_sql(sql, values)

        
def delete_all():
    sql = "DELETE FROM class_attend"
    values = []
    run_sql(sql, values)