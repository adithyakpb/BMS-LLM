class Person:
    def __init__(self, name, designation: str) -> None:
        """A person in BMS can be one of the following:
        1. Student
        2. Faculty
        3. HOD
        4. Principal
        This class contains all methods to define and manipulate properties of a person."""

        self.name = name
        self.designation = "" # enum: student, faculty, hod, director, dean, principal
        self.email = ""
        