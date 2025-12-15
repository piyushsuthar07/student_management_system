class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def display(self):
        return f"name is {self.name}, roll:{self.roll}, marks:{self.marks}"