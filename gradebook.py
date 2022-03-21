from enum import Enum
import uuid


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person():
    first_name = ''
    last_name = ''
    dob = ''
    alive = AliveStatus

    def __init__(self):
        pass

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name
        return new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
        return new_last_name

    def update_dob(self, new_dob):
        self.dob = new_dob
        return new_dob

    def update_status(self, new_status):
        self.alive = new_status
        return new_status


class Instructor(Person):
    instructor_id = uuid.uuid4()

    def __init__(self):
        pass


class Student(Person):
    student_id = uuid.uuid4()

    def __init__(self):
        pass


class ZipCodeStudent(Student):

    def __init__(self):
        pass


class College(Student):

    def __init__(self):
        pass


class Classroom:
    students = []
    instructors = []

    def __init__(self):
        pass


student1 = Student()
print(student1.student_id)
