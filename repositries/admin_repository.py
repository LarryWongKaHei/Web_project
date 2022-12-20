from db.run_sql import run_sql
from repositries import classes_repository
from repositries import members_repository
from repositries import class_attend_repositry

# To check all the members who suppose to show up today
def print_all_class_member_today(class_today):
    classes_id = []
    for classes in class_today:
        classes_id.append(classes.id)
    classes_id = tuple(classes_id)
    sql = "SELECT * FROM class_attend WHERE classes_id IN %s"
    values = [classes_id]
    result = run_sql(sql, values)
    dict_list = []
    for item in result:
        new_dict = {classes_repository.select_by_id_return_name(item['classes_id']) : members_repository.select_by_id_return_name(item['member_id'])}
        dict_list.append(new_dict)
    return dict_list
    
    
        
