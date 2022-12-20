class Members:
    def __init__(self, name, membership_level, gender, availability, salary, status=False, id=None):
        self.name = name
        self.membership_level = membership_level
        self.gender = gender
        self.availability = availability
        self.salary = salary
        self.status = status
        self.id = id