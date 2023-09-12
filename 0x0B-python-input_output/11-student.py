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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
        """
        for ky, vl in json.items():
            setattr(self, ky, vl)
