from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person:
    def __init__(self, first_name, last_name, dob, AliveStatus):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus

    def update_first_name(self, first_name):
        self.first_name = first_name
        return first_name

    def update_last_name(self, last_name):
        self.last_name = last_name
        return last_name

    def update_dob(self, dob):
        self.dob = dob
        return dob

    def update_status(self, status):
        self.alive = status
        return status


class Instructor(Person):
    instructor_id = uuid4()

    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)


class Student(Person):
    student_id = uuid4()

    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)


class ZipCodeStudent(Student):

    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)


class College(Student):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)


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
        self.students.append(f'Student_{student.first_name},{student.last_name}, {student.dob},\
 {student.student_id}')
        return self.students

    def remove_student(self, student):
        self.students.remove(f'Student_{student.first_name},{student.last_name}, {student.dob},\
{student.student_id}')
        return self.students

    def print_instructors(self):
        print(f'{self.instructors}')

    def print_students(self):
        print(f'{self.students}')


instructor1 = Instructor(first_name='Allen', last_name='Chung', dob='9/27/91', alive=1)

classroom1 = Classroom()
classroom1.add_instructor(instructor1)
print(classroom1.print_instructors())
classroom1.remove_instructor(instructor1)
print(classroom1.print_instructors())

student1 = Student(first_name='Kira', last_name='Sy', dob='1/1/2000', alive=1)


classroom2 = Classroom()
classroom2.add_student(student1)
print(classroom2.print_students())
#classroom2.remove_student(student1)
#print(classroom2.print_students())
