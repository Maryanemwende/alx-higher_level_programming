#!/usr/bin/python3
"""a class Student"""


class Student:
    """represents a class - Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes attributes for Student
        first_name is the first name of student
        last_name is the last name for student
        age is the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
