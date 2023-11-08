#!/usr/bin/python3
"""Module defines a class Student based on another"""


class Student:
    """Represents a class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student props"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retries a dictionary representation of a student instance"""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return (self.__dict__)

    def reload_from_json(self, json):
        for n, p in json.items():
            setattr(self, n, p)
