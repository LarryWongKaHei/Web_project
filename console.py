from models.classes import Classes
from repositries import classes_repository

from models.members import Members
from repositries import members_repository

from repositries import class_attend_repositry

class_attend_repositry.delete_all()
classes_repository.delete_all()
members_repository.delete_all()

# Add classes to classes table
yoga = Classes('Yoga', 200, 'F', ['mon', 'wed', 'fri', 'sun'], 30, 2)
classes_repository.save(yoga)

pilates = Classes('Pilates', 200, 'F', ['tue', 'thu'], 45, 2)
classes_repository.save(pilates)

circuit_training = Classes('Circuit Training', 500, 'M', ['tue', 'fri', 'sun'], 20, 5)
classes_repository.save(circuit_training)

hiit = Classes('HIIT', 600, 'M', ['mon', 'tue', 'thu', 'fri'], 60, 4)
classes_repository.save(hiit)

# Add members to members table
larry = Members('Larry', 'platinum', 'M', ['mon', 'tue', 'thu', 'sun'], 1000)
members_repository.save(larry)

Tim = Members('Tim', 'bronze', 'M', ['tue', 'thu'], 1300)
members_repository.save(Tim)

Cindy = Members('Cindy', 'gold', 'F', ['thu'], 800)
members_repository.save(Cindy)

William = Members('William', 'platinum', 'M', ['tue', 'thu'], 2000)
members_repository.save(William)

# Simulate member joining a class
class_attend1 = class_attend_repositry.save(larry, yoga)

class_attend2 = class_attend_repositry.save(Tim, yoga)

class_attend3 = class_attend_repositry.save(William, hiit)
