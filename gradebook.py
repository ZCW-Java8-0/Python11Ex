from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person:
    first_name = ''
    last_name = ''
    dob = ''
    alive = AliveStatus

    def __init__(self):
        pass

    def update_first_name(self, first_name):
        self.first_name = first_name
        return first_name

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
    instructor_id = uuid4()

    def __init__(self, first_name, last_name, dob, alive):
        super().__init__()


class Student(Person):
    student_id = uuid4

    def __init__(self, first_name, last_name, dob, alive):
        super().__init__()


class ZipCodeStudent(Student):

    def __init__(self, first_name, last_name, dob, alive):
        super().__init__()


class College(Student):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__()


class Classroom:
    students = []
    instructors = []

    def __init__(self):
        pass

    def add_instructor(self, instructor):
        self.instructors.append(instructor.instructor_id)
        return self.instructors

    def remove_instructor(self):
        return self.instructors

    def add_student(self):
        return self.students

    def remove_student(self):
        return self.students

    def print_instructors(self):
        print(f'Instructor: {self.instructors}')

    def print_students(self):
        print(self.students)


instructor1 = Instructor('Allen', 'Chung', '9/27/91', 1)

print(instructor1.update_first_name('Allen'))

classroom1 = Classroom()
classroom1.add_instructor(instructor1)
print(classroom1.print_instructors())
