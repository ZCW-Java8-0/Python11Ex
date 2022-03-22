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
        self.instructors.append(f'Instructor_{instructor.first_name},{instructor.last_name}, {instructor.dob},\
 {instructor.instructor_id}')
        return self.instructors

    def remove_instructor(self, instructor):
        self.instructors.remove(f'Instructor_{instructor.first_name},{instructor.last_name}, {instructor.dob},\
 {instructor.instructor_id}')
        return self.instructors

    def add_student(self, student):
        self.students.append(student.student_id)
        return self.students

    def remove_student(self):
        return self.students

    def print_instructors(self):
        print(f'{self.instructors}')

    def print_students(self):
        print(self.students)


instructor1 = Instructor(first_name='Allen', last_name='Chung', dob='9/27/91', alive=1)

instructor1.update_first_name('Allen')
instructor1.update_last_name('Chung')
instructor1.update_dob('9/27/01')
instructor1.update_status(1)

classroom1 = Classroom()
classroom1.add_instructor(instructor1)
print(classroom1.print_instructors())
classroom1.remove_instructor(instructor1)
print(classroom1.print_instructors())

